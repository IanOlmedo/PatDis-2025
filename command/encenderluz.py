from comando import Comando

class EncenderLuz(Comando):
    def __init__(self, luz):
        self.luz = luz

    def ejecutar(self):
        self.luz.encender()

    def deshacer(self):
        self.luz.apagar()
