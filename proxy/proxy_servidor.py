from servidor import Servidor
from servidor_real import ServidorReal

class ProxyServidor(Servidor):
    def __init__(self):
        self._servidor_real = ServidorReal()
        self.usuarios_autorizados = ["admin", "gerente"]

    def acceder(self, usuario):
        if usuario in self.usuarios_autorizados:
            return self._servidor_real.acceder(usuario)
        else:
            return f"⛔ Acceso denegado para el usuario: {usuario}"
