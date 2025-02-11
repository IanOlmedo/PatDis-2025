from abc import ABC, abstractmethod

class Pizzeria(ABC):
    @abstractmethod
    def crear_pizza(self):
        pass

    def ordenar_pizza(self):
        pizza = self.crear_pizza()
        return pizza.preparar()