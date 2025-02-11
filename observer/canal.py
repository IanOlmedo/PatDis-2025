from abc import ABC, abstractmethod

# 📡 Sujeto (el canal)
class CanalYouTube:
    def __init__(self):
        self._suscriptores = []  # Lista de observadores

    def suscribir(self, suscriptor):
        self._suscriptores.append(suscriptor)

    def desuscribir(self, suscriptor):
        self._suscriptores.remove(suscriptor)

    def notificar(self, video):
        print(f"\n🎬 Nuevo video publicado: {video}")
        for suscriptor in self._suscriptores:
            suscriptor.actualizar(video)