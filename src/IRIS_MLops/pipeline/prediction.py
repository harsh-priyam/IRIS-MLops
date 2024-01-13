import joblib 
import numpy as np 
import pandas as pd 
from pathlib import Path 

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

    def predict(self, data):
        # Convert data to a pandas DataFrame
        columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
        df = pd.DataFrame(data, columns=columns)

        # Assuming 'model' is a sklearn model
        prediction = self.model.predict(df)

        return prediction