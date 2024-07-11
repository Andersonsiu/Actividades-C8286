import Pyro4

def main():
    ns = Pyro4.locateNS()
    uri = ns.lookup("example.timeseriespredictor")
    predictor = Pyro4.Proxy(uri)
    predictor._pyroHmacKey = b"secret"
    
    # Autenticarse
    predictor._pyroBind()
    predictor._pyroAuth = ("admin", "secret")
    
    # Cargar datos
    with open("data.csv", "r") as f:
        data = f.read()
    print(predictor.load_data(data))
    
    # Entrenar modelo
    print(predictor.train_model("target"))
    
    # Realizar predicción
    with open("new_data.csv", "r") as f:
        new_data = f.read()
    predictions = predictor.predict("model_target", new_data)
    print("Predicciones:", predictions)

    # Guardar modelo
    print(predictor.save_model("model_target"))

    # Cargar modelo
    print(predictor.load_model("model_target"))

if __name__ == "__main__":
    main()
