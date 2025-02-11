# 🎛️ Invocador (el control remoto)
class ControlRemoto:
    def __init__(self):
        self.comando = None

    def configurar_comando(self, comando):
        self.comando = comando

    def presionar_boton(self):
        if self.comando:
            self.comando.ejecutar()

    def presionar_deshacer(self):
        if self.comando:
            self.comando.deshacer()
