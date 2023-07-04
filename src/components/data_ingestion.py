from src.logger import logging
from src.exception import Custom_exception
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import pandas as pd
import os
import sys
# from src.components.data_transformation import DataTransformation, DataTransformationConfig
# from src.components.model_trainer import ModelTrainer, ModelTrainerConfig
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(module_path)


@dataclass
class DataIngestionConfig:
    train_data_path: str = None
    test_data_path: str = None
    raw_data_path: str = None

    def __init__(self):
        self.train_data_path = os.path.join('artifacts', 'train.csv')
        self.test_data_path = os.path.join('artifacts', 'test.csv')
        self.raw_data_path = os.path.join('artifacts', 'raw.csv')


class DataIngestion:
    def __init__(self) -> None:
        self.data_ingestion = DataIngestionConfig()

    def initiate_ingestion(self):
        try:
            df = pd.read_csv('./notebook./data./gemstone.csv')
            df.drop(['id'], axis=1, inplace=True)
            os.makedirs(os.path.dirname(
                self.data_ingestion.train_data_path), exist_ok=True)
            df.to_csv(self.data_ingestion.raw_data_path,
                      index=False, header=True)

            logging.info('train test split initiated')

            train_set, test_set = train_test_split(
                df, test_size=0.25, random_state=42)
            train_set.to_csv(self.data_ingestion.train_data_path,
                             index=False, header=True)
            test_set.to_csv(self.data_ingestion.test_data_path,
                            index=False, header=True)

            logging.info('data ingestion completed')
            return (
                self.data_ingestion.train_data_path,
                self.data_ingestion.test_data_path,
                df
            )
        except Exception as e:
            raise Custom_exception(str(e), sys.exc_info())


if __name__ == '__main__':
    object = DataIngestion()
    train_df, test_df, dataframe = object.initiate_ingestion()
    data_transformation = DataTransformation()
    data_transformation.DataTransformerObject(dataframe)
    train_arr, test_arr, _ = data_transformation.initate_data_transformation(
        train_df, test_df)
    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))


# output :
# test_model_score 0.9439536805787095
# train_model_score 0.9447042278427323
# LinearRegression()
# 0.9439536805787095
