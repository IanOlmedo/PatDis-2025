from abc import ABC, abstractmethod

# 🏗️ Interfaz común para los manejadores
class Manejador(ABC):
    def __init__(self, siguiente=None):
        self.siguiente = siguiente  # Próximo manejador en la cadena

    @abstractmethod
    def manejar_solicitud(self, monto):
        pass