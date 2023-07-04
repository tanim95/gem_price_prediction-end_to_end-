import os
import sys
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from dataclasses import dataclass
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from src.exception import Custom_exception
from src.logger import logging
from src.utils import save_obj


@dataclass
class DataTransformationConfig:
    preprocessor_file_path: str = os.path.join('artifacts', 'preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def DataTransformerObject(self, df):
        try:
            numerical_columns = df.select_dtypes(
                exclude=['object']).drop(columns='price')  # We need to drop the target column i.e 'price'
            categorical_columns = df.select_dtypes(include=['object'])
            num_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler(with_mean=False))
            ])
            cat_pipeline = Pipeline([
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('one_hot_encoder', OneHotEncoder()),
                ('scaler', StandardScaler(with_mean=False))
            ])
            logging.info('categorical columns standard scaling completed')
            logging.info('numerical columns encoding completed')
            preprocessor = ColumnTransformer(transformers=[
                ('num_pipeline', num_pipeline, numerical_columns.columns),
                ('cat_pipeline', cat_pipeline, categorical_columns.columns)
            ])
            return preprocessor

        except Exception as e:
            raise Custom_exception(str(e), sys.exc_info())

    def initate_data_transformation(self, train, test):
        train_df = pd.read_csv(train)
        test_df = pd.read_csv(test)
        logging.info('Reading train and test Data')
        preprocessing_obj = self.DataTransformerObject(train_df)
        target = 'price'
        input_train_data = train_df.drop(target, axis=1)
        target_feature_train = train_df[target]
        input_test_data = test_df.drop(target, axis=1)
        target_feature_test = test_df[target]
        logging.info('applying preprocessing object data')
        input_train_arr = preprocessing_obj.fit_transform(input_train_data)
        input_test_arr = preprocessing_obj.transform(input_test_data)
        train_ar = np.c_[input_train_arr, np.array(target_feature_train)]
        test_ar = np.c_[input_test_arr, np.array(target_feature_test)]
        logging.info('saved preprocessing object')
        save_obj(
            file_path=self.data_transformation_config.preprocessor_file_path,
            obj=preprocessing_obj
        )
        return (
            train_ar,
            test_ar,
            self.data_transformation_config.preprocessor_file_path
        )
