from abc import ABC, abstractmethod

# 🎛️ Interfaz Command
class Comando(ABC):
    @abstractmethod
    def ejecutar(self):
        pass

    @abstractmethod
    def deshacer(self):
        pass