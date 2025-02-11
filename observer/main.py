from canal import CanalYouTube
from usuario import Usuario

# 🚀 Uso del patrón Observer
canal = CanalYouTube()

# 📌 Crear suscriptores
usuario1 = Usuario("Juan")
usuario2 = Usuario("María")

# 📌 Suscribirse al canal
canal.suscribir(usuario1)
canal.suscribir(usuario2)

# 📌 Publicar un nuevo video
canal.notificar("Cómo aprender Python en 10 minutos")

# 📌 Un usuario se desuscribe y se publica otro video
canal.desuscribir(usuario1)
canal.notificar("Patrón Observer en acción")