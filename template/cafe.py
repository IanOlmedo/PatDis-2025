from bebida_caliente import BebidaCaliente


#subclase para completmentar a la clase padre
class Cafe(BebidaCaliente):
    def agregar_ingrediente(self):
        print("🌿 Agregando café molido...")

    def agregar_condimentos(self):
        print("🥛 Añadiendo azúcar y leche...")
