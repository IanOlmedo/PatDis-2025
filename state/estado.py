from abc import ABC, abstractmethod

# 🏗️ Interfaz Estado
class Estado(ABC):
    @abstractmethod
    def manejar(self, maquina):
        pass

class EsperandoDinero(Estado):
    def manejar(self, maquina):
        print("💰 Insertar dinero para comprar café.")
        maquina.estado = PreparandoCafe()  # Cambia al siguiente estado

# ☕ Estado 2: Preparando café
class PreparandoCafe(Estado):
    def manejar(self, maquina):
        print("⏳ Preparando el café...")
        maquina.estado = EntregandoCafe()  # Cambia al siguiente estado

# ☕ Estado 3: Entregando café
class EntregandoCafe(Estado):
    def manejar(self, maquina):
        print("✅ ¡Aquí tienes tu café! ☕ Disfrútalo.")
        maquina.estado = EsperandoDinero()  # Reinicia la máquina