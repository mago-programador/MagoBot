from message_config import messager
import os
from sender import sender

class Commands:
    
    
    def funcoes_internas(self):
        
        if messager.texto is not None:
            try:
                with open(f"{os.path.dirname(__file__)}\\whitelist.txt", "r") as file:
                    conteudo = file.read()
                    self.whitelist = conteudo.splitlines()
                
                if "/addw" in messager.texto:
                    mensagem = sender.texto
                    index = mensagem.split()
                    numero = index[1]
                    with open(f"{os.path.dirname(__file__)}\\whitelist.txt", "r") as file:
                        self.conteudo = file.read()
                        self.conteudo = self.conteudo.splitlines()
                        self.conteudo.append(numero)
                    with open(f"{os.path.dirname(__file__)}\\whitelist.txt", "w") as file:
                        for num in self.conteudo:
                            file.write(f"{num}\n")
                        sender.enviar_mensagem("Número adicionado com sucesso.")

                elif "/remw" in messager.texto:
                    mensagem = sender.texto
                    index = mensagem.split()
                    numero = index[1]
                    with open(f"{os.path.dirname(__file__)}\\whitelist.txt", "r") as file:
                        self.conteudo = file.read()
                        self.conteudo = self.conteudo.splitlines()
                        self.conteudo.remove(numero)
                    with open(f"{os.path.dirname(__file__)}\\whitelist.txt", "w") as file:
                        for num in self.conteudo:
                            file.write(f"{num}\n")
                        sender.enviar_mensagem("Número removido com sucesso.")
                    
                elif "/listw" in messager.texto:  
                    with open(f"{os.path.dirname(__file__)}\\whitelist.txt", "r") as file:
                        conteudo = file.read()
                        sender.enviar_mensagem(conteudo)
                        
            except Exception as e:
                print(e)
utiler = Commands()