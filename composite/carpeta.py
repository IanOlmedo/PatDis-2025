from componente import Componente

class Carpeta(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.contenido = []  

    def agregar(self, componente: Componente):
        self.contenido.append(componente)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"{self.nombre}")
        for item in self.contenido:
            item.mostrar(nivel + 1)