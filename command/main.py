from luz import Luz
from encenderluz import EncenderLuz
from apagarluz import ApagarLuz
from control_remoto import ControlRemoto

# 🚀 Uso del Patrón Command
luz = Luz()
encender = EncenderLuz(luz)
apagar = ApagarLuz(luz)

control = ControlRemoto()

# Encender la luz
control.configurar_comando(encender)
control.presionar_boton()  # 💡 La luz está encendida

# Apagar la luz
control.configurar_comando(apagar)
control.presionar_boton()  # 🌑 La luz está apagada

# Deshacer la última acción (volver a encender)
control.presionar_deshacer()  # 💡 La luz está encendida