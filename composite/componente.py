from abc import ABC, abstractmethod


class Componente(ABC):
    @abstractmethod
    def mostrar(self, nivel=0):
        pass
    