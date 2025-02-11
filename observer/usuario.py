from suscriptor import Suscriptor

# 🧑‍💻 Observador concreto
class Usuario(Suscriptor):
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, video):
        print(f"📢 {self.nombre} recibió la notificación: ¡Nuevo video disponible! ({video})")
