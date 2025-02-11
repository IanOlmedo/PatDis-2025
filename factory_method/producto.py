from abc import ABC, abstractmethod

# 1️⃣ Definimos la clase base Pizza
class Pizza(ABC):
    @abstractmethod
    def preparar(self):
        pass