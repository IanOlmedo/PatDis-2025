from abc import ABC, abstractmethod

# 1️⃣ Interfaces para los productos (Hamburguesa y Bebida)
class Hamburguesa(ABC):
    @abstractmethod
    def preparar(self):
        pass
