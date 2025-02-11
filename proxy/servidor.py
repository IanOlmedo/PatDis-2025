from abc import ABC, abstractmethod

# 📌 Interfaz común
class Servidor(ABC):
    @abstractmethod
    def acceder(self, usuario):
        pass