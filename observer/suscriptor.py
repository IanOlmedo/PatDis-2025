from abc import ABC, abstractmethod

# 👀 Interfaz Observer (Suscriptor)
class Suscriptor(ABC):
    @abstractmethod
    def actualizar(self, video):
        pass
