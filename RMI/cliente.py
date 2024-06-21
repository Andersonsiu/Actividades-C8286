import threading
import Pyro5.api

def tarea_cliente(usuario, contraseña, titulo_libro):
    # Conectar al nameserver de Pyro
    ns = Pyro5.api.locate_ns()
    
    # Obtener la URI del objeto registrado
    uri = ns.lookup("biblioteca")
    biblioteca = Pyro5.api.Proxy(uri)
    
    if biblioteca.autenticar(usuario, contraseña):
        print(f"{usuario} autenticado exitosamente")

        print(f"{usuario} buscando {titulo_libro}: {biblioteca.buscar_libro(usuario, titulo_libro)}")

        print(f"{usuario} prestando {titulo_libro}: {biblioteca.prestar_libro(usuario, titulo_libro)}")
        print(f"{usuario} estado de {titulo_libro}: {biblioteca.estado_libro(usuario, titulo_libro)}")

        print(f"{usuario} devolviendo {titulo_libro}: {biblioteca.devolver_libro(usuario, titulo_libro)}")
        print(f"{usuario} estado de {titulo_libro}: {biblioteca.estado_libro(usuario, titulo_libro)}")
    else:
        print(f"{usuario} autenticación fallida")

def main():
    num_clients = 10
    threads = []
    for i in range(num_clients):
        usuario = f"usuario{i % 2 + 1}"
        contraseña = "contraseña1" if usuario == "usuario1" else "contraseña2"
        titulo_libro = "Libro1"
        thread = threading.Thread(target=tarea_cliente, args=(usuario, contraseña, titulo_libro))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()

