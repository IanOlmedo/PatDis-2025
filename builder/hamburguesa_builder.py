from hamburguesa import Hamburguesa

class HamburguesaBuilder:
    def __init__(self):
        self.pan = "Pan clásico"
        self.carne = "Carne de res"
        self.queso = "Sin queso"
        self.lechuga = "Sin lechuga"
        self.tomate = "Sin tomate"
        self.cebolla = "Sin cebolla"
        self.salsa = "Sin salsa"

    def agregar_queso(self, tipo="Queso cheddar"):
        self.queso = tipo
        return self  # Retorna el builder para encadenar métodos

    def agregar_lechuga(self):
        self.lechuga = "Con lechuga"
        return self

    def agregar_tomate(self):
        self.tomate = "Con tomate"
        return self

    def agregar_cebolla(self):
        self.cebolla = "Con cebolla"
        return self

    def agregar_salsa(self, tipo="Mayonesa"):
        self.salsa = tipo
        return self

    def elegir_pan(self, tipo="Pan brioche"):
        self.pan = tipo
        return self

    def elegir_carne(self, tipo="Carne de pollo"):
        self.carne = tipo
        return self

    def construir(self):
        return Hamburguesa(self.pan, self.carne, self.queso, self.lechuga, self.tomate, self.cebolla, self.salsa)
