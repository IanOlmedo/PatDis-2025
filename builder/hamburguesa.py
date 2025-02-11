
class Hamburguesa:
    def __init__(self, pan, carne, queso, lechuga, tomate, cebolla, salsa):
        self.pan = pan
        self.carne = carne
        self.queso = queso
        self.lechuga = lechuga
        self.tomate = tomate
        self.cebolla = cebolla
        self.salsa = salsa

    def __str__(self):
        return f"Hamburguesa con {self.pan}, {self.carne}, {self.queso}, {self.lechuga}, {self.tomate}, {self.cebolla} y {self.salsa}"
