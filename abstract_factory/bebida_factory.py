from abc import ABC, abstractmethod

class Bebida(ABC):
    @abstractmethod
    def servir(self):
        pass