class SendMessage:

    def text(self):
        self.texto = None
        self.mensagem = None
        self.midia = None
        self.legenda = None
    
    def config(self):
        if self.texto == "ping":
            self.mensagem = "pong"
        elif self.texto == "comandos":
            self.mensagem = '''Exemplo de Comandos
Comando 1#enter
Comando 2
Comando 3#enter'''

messager = SendMessage()
