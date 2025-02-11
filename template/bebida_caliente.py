from abc import ABC, abstractmethod

# 🍵 Clase base con el método plantilla
class BebidaCaliente(ABC):
    def preparar(self):
        """Método plantilla: define el proceso general"""
        self.hervir_agua()
        self.agregar_ingrediente()
        self.servir_en_taza()
        self.agregar_condimentos()

    def hervir_agua(self):
        print("💧 Hirviendo agua...")

    @abstractmethod
    def agregar_ingrediente(self):
        """Cada subclase definirá su propio ingrediente"""
        pass

    def servir_en_taza(self):
        print("☕ Sirviendo en una taza...")

    def agregar_condimentos(self):
        """Puede ser opcional, se puede sobrescribir en las subclases"""
        pass