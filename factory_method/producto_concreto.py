from producto import Pizza

# 2️⃣ Creamos las clases concretas de pizzas
class PizzaQueso(Pizza):
    def preparar(self):
        return "Preparando Pizza de Queso"

class PizzaPepperoni(Pizza):
    def preparar(self):
        return "Preparando Pizza de Pepperoni"

class PizzaVegetariana(Pizza):
    def preparar(self):
        return "Preparando Pizza Vegetariana"