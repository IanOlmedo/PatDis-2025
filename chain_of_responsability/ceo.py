from manejador import Manejador


#manejador cocreto
class CEO(Manejador):
    def manejar_solicitud(self, monto):
        print(f"✅ CEO aprueba la compra de ${monto}")