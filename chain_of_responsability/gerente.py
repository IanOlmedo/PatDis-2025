from manejador import Manejador


#manejador cocreto
class Gerente(Manejador):
    def manejar_solicitud(self, monto):
        if monto <= 1000:
            print(f"✅ Gerente aprueba la compra de ${monto}")
        elif self.siguiente:
            self.siguiente.manejar_solicitud(monto)
