from archivo import Archivo
from carpeta import Carpeta


archivo1 = Archivo("documento.txt")
archivo2 = Archivo("imagen.png")
archivo3 = Archivo("video.mp4")

carpeta1 = Carpeta("Mis Documentos")
carpeta1.agregar(archivo1)
carpeta1.agregar(archivo2)

carpeta2 = Carpeta("Multimedia")
carpeta2.agregar(archivo3)

carpeta_principal = Carpeta("Raíz")
carpeta_principal.agregar(carpeta1)
carpeta_principal.agregar(carpeta2)

# 📂 Mostrar toda la estructura
carpeta_principal.mostrar()