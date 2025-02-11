from hacedor import AutoBuilder

class Director:
    def __init__(self, builder):
        self.builder = builder

    def construir_auto_basico(self):
        self.builder.set_motor("1.0")
        self.builder.set_marca("Fiat")
        self.builder.set_modelo("Uno")
        self.builder.set_puertas(4)

    def construir_auto_caro(self):
        self.builder.set_motor("2.0")
        self.builder.set_marca("Lamborginni")
        self.builder.set_modelo("Black")
        self.builder.set_puertas(2)