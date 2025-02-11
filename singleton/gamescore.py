
class GameScore:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.puntaje = 0
        return cls.instance

    def sumar_puntos(self, puntos):
        self.puntaje += puntos

    def resetear_puntaje(self):
        self.puntaje = 0

    def __str__(self):
        return f"Puntaje actual: {self.puntaje}"