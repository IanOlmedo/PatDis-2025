from servidor import Servidor

class ServidorReal(Servidor):
    def acceder(self, usuario):
        return f"🔓 Acceso concedido al usuario: {usuario}"
