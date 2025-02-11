from fabrica_abstracta import ComboFactory
from hamburguesa_factory import Hamburguesa
from bebida_factory import Bebida
from mchamburguesa import McHamburguesa
from mcbebida import McBebida

class McDonaldsFactory(ComboFactory):
    def crear_hamburguesa(self) -> Hamburguesa:
        return McHamburguesa()
    
    def crear_bebida(self) -> Bebida:
        return McBebida()