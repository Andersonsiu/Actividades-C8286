import Pyro5.api
from biblioteca import Biblioteca

def main():
    # Iniciar el daemon de Pyro
    daemon = Pyro5.api.Daemon()
    
    # Conectar al nameserver de Pyro
    ns = Pyro5.api.locate_ns()
    
    # Crear una instancia de la clase Biblioteca
    biblioteca = Biblioteca()
    
    # Registrar la instancia con un nombre en el nameserver
    uri = daemon.register(biblioteca)
    ns.register("biblioteca", uri)
    
    print("Biblioteca lista. URI del objeto =", uri)
    
    # Iniciar el bucle de espera para procesar solicitudes
    daemon.requestLoop()

if __name__ == "__main__":
    main()

