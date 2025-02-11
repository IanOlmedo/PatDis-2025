from producto_concreto import PizzaPepperoni, PizzaQueso, PizzaVegetariana
from creador import Pizzeria

# 4️⃣ Implementamos fábricas específicas para cada tipo de pizza
class PizzeriaQueso(Pizzeria):
    def crear_pizza(self):
        return PizzaQueso()

class PizzeriaPepperoni(Pizzeria):
    def crear_pizza(self):
        return PizzaPepperoni()

class PizzeriaVegetariana(Pizzeria):
    def crear_pizza(self):
        return PizzaVegetariana()