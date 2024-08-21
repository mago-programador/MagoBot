from sender import sender


class message_config:

    def text(self):
        self.texto = sender.texto

    def config(self):
        if self.texto == "ping":
            sender.enviar_mensagem("Opa")

    def flow_message(self):
        self.text()
        self.config()

messager = message_config()
