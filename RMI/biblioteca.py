import threading
import Pyro5.api

@Pyro5.api.expose
class Biblioteca:
    def __init__(self):
        self.libros = {
            "Libro1": True,
            "Libro2": True,
            "Libro3": False
        }
        self.usuarios = {
            "usuario1": "contraseña1",
            "usuario2": "contraseña2"
        }
        self.usuarios_autenticados = {}
        self.lock = threading.Lock()

    def autenticar(self, usuario, contraseña):
        if usuario in self.usuarios and self.usuarios[usuario] == contraseña:
            self.usuarios_autenticados[usuario] = True
            return True
        else:
            return False

    def verificar_autenticacion(self, usuario):
        if usuario in self.usuarios_autenticados and self.usuarios_autenticados[usuario]:
            return True
        else:
            raise ValueError("No autenticado")

    def prestar_libro(self, usuario, titulo_libro):
        self.verificar_autenticacion(usuario)
        with self.lock:
            if titulo_libro in self.libros and self.libros[titulo_libro]:
                self.libros[titulo_libro] = False
                return True
            return False

    def devolver_libro(self, usuario, titulo_libro):
        self.verificar_autenticacion(usuario)
        with self.lock:
            if titulo_libro in self.libros and not self.libros[titulo_libro]:
                self.libros[titulo_libro] = True
                return True
            return False

    def buscar_libro(self, usuario, titulo_libro):
        self.verificar_autenticacion(usuario)
        return titulo_libro if titulo_libro in self.libros else None

    def estado_libro(self, usuario, titulo_libro):
        self.verificar_autenticacion(usuario)
        if titulo_libro in self.libros:
            return "Disponible" if self.libros[titulo_libro] else "Prestado"
        return "Libro no encontrado"
