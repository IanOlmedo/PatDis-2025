
from fabrica_abstracta import ComboFactory
from hamburguesa_factory import Hamburguesa
from bebida_factory import Bebida
from  kinghamburguesa import BKHamburguesa
from kingbebida import BKBebida

class BurgerKingFactory(ComboFactory):
    def crear_hamburguesa(self) -> Hamburguesa:
        return BKHamburguesa()
    
    def crear_bebida(self) -> Bebida:
        return BKBebida()