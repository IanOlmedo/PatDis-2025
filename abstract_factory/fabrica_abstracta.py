from abc import ABC, abstractmethod
from hamburguesa_factory import Hamburguesa
from bebida_factory import Bebida

class ComboFactory(ABC):
    @abstractmethod
    def crear_hamburguesa(self) -> Hamburguesa:
        pass

    @abstractmethod
    def crear_bebida(self) -> Bebida:
        pass