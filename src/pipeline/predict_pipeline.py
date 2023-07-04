import os
import sys
import pandas as pd
from src.exception import Custom_exception
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            data_scaled = preprocessor.transform(features)
            prediction = model.predict(data_scaled)
            return prediction

        except Exception as e:
            raise Custom_exception(e, sys)


class CustomData:
    def __init__(self,
                 cut: str,
                 color: str,
                 clarity: str,
                 carat: float,
                 depth: float,
                 table: float,
                 x: float,
                 y: float,
                 z: float):

        self.cut = cut
        self.color = color
        self.clarity = clarity
        self.carat = carat
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z

    def get_data_frame(self):
        try:
            custom_data_input_dict = {
                "cut": [self.cut],
                "color": [self.color],
                "clarity": [self.clarity],
                "carat": [self.carat],
                "depth": [self.depth],
                "table": [self.table],
                "x": [self.x],
                "y": [self.y],
                "z": [self.z],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise Custom_exception(e, sys)
