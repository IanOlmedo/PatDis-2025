from estado import EsperandoDinero

class MaquinaCafe:
    def __init__(self):
        self.estado = EsperandoDinero()  # Estado inicial

    def solicitar_cafe(self):
        self.estado.manejar(self)
