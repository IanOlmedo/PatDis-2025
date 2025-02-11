from manejador import Manejador



#manejador cocreto
class Director(Manejador):
    def manejar_solicitud(self, monto):
        if monto <= 5000:
            print(f"✅ Director aprueba la compra de ${monto}")
        elif self.siguiente:
            self.siguiente.manejar_solicitud(monto)