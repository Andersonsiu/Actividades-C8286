import Pyro4

def main():
    predictor = TimeSeriesPredictor()
    daemon = Pyro4.Daemon()
    uri = daemon.register(predictor)
    ns = Pyro4.locateNS()
    ns.register("example.timeseriespredictor", uri)
    print("Server ready.")
    daemon.requestLoop()

if __name__ == "__main__":
    main()
