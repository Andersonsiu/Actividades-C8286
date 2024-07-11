import Pyro4

@Pyro4.expose
class TimeSeriesPredictorWithErrors(TimeSeriesPredictor):
    def load_data(self, data):
        try:
            df = pd.read_csv(io.StringIO(data))
            self.data = df
            return "Data loaded successfully"
        except Exception as e:
            return f"Error loading data: {e}"

    def train_model(self, target_column):
        try:
            X = self.data.drop(columns=[target_column])
            y = self.data[target_column]
            model = LinearRegression()
            model.fit(X, y)
            model_name = f"model_{target_column}"
            self.models[model_name] = model
            return f"Model {model_name} trained successfully"
        except Exception as e:
            return f"Error training model: {e}"

    def predict(self, model_name, new_data):
        try:
            if model_name not in self.models:
                return "Model not found"
            model = self.models[model_name]
            new_data_df = pd.read_csv(io.StringIO(new_data))
            predictions = model.predict(new_data_df)
            return predictions.tolist()
        except Exception as e:
            return f"Error making predictions: {e}"

# El resto del código permanece igual
