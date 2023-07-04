import os
import sys
import dill
import pickle
from src.exception import Custom_exception
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


def save_obj(file_path, obj):
    try:
        path = os.path.dirname(file_path)
        os.makedirs(path, exist_ok=True)
        with open(file_path, 'wb') as file:
            dill.dump(obj, file)
    except Exception as e:
        raise Custom_exception(str(e), sys.exc_info())


def load_object(file_path):
    try:
        with open(file_path, "rb") as file:
            return pickle.load(file)

    except Exception as e:
        raise Custom_exception(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    report = {}

    for i in range(len(list(models))):
        model = list(models.values())[i]
        perameter = param[list(models.keys())[i]]

        gs = GridSearchCV(model, perameter, cv=10)
        gs.fit(X_train, y_train)

        model.set_params(**gs.best_params_)
        model.fit(X_train, y_train)

        y_train_pred = model.predict(X_train)
        y_test_pred = model.predict(X_test)
        test_model_score = r2_score(y_test, y_test_pred)
        print('test_model_score', test_model_score)
        train_model_score = r2_score(y_train, y_train_pred)
        print('train_model_score', train_model_score)
        report[list(models.keys())[i]] = test_model_score

    return report
