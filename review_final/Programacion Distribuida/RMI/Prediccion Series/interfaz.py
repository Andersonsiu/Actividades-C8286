//pip install Pyro4 scikit-learn pandas

import Pyro4
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import io

@Pyro4.expose
class TimeSeriesPredictor(object):
    def __init__(self):
        self.models = {}
    
    def load_data(self, data):
        df = pd.read_csv(io.StringIO(data))
        self.data = df
        return "Data loaded successfully"

    def train_model(self, target_column):
        X = self.data.drop(columns=[target_column])
        y = self.data[target_column]
        model = LinearRegression()
        model.fit(X, y)
        model_name = f"model_{target_column}"
        self.models[model_name] = model
        return f"Model {model_name} trained successfully"

    def predict(self, model_name, new_data):
        if model_name not in self.models:
            return "Model not found"
        model = self.models[model_name]
        new_data_df = pd.read_csv(io.StringIO(new_data))
        predictions = model.predict(new_data_df)
        return predictions.tolist()

    def save_model(self, model_name):
        if model_name not in self.models:
            return "Model not found"
        model = self.models[model_name]
        with open(f"{model_name}.pkl", "wb") as f:
            pickle.dump(model, f)
        return f"Model {model_name} saved successfully"

    def load_model(self, model_name):
        try:
            with open(f"{model_name}.pkl", "rb") as f:
                model = pickle.load(f)
            self.models[model_name] = model
            return f"Model {model_name} loaded successfully"
        except FileNotFoundError:
            return "Model file not found"
