from director import Director
from gerente import Gerente
from ceo import CEO

gerente = Gerente(Director(CEO()))

# 📩 Enviar solicitudes
gerente.manejar_solicitud(500)    # Gerente aprueba
gerente.manejar_solicitud(3000)   # Director aprueba
gerente.manejar_solicitud(10000)  # CEO aprueba