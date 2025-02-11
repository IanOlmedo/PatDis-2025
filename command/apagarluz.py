from comando import Comando

class ApagarLuz(Comando):
    def __init__(self, luz):
        self.luz = luz

    def ejecutar(self):
        self.luz.apagar()

    def deshacer(self):
        self.luz.encender()