from reader import reader
from sender import sender
from message_config import messager
from database.commands import utiler
from functools import lru_cache

@lru_cache
def menu():
    while True:

        sender.masterizar(reader.flow())

        sender.masterizar(sender.flow_sender())

        sender.masterizar(messager.text())

        sender.ler_mensagem()

        sender.masterizar(messager.config())
        
        utiler.funcoes_internas()
        
        try:
            if reader.numero in utiler.whitelist:
                try:
                    sender.responder()
                except Exception:
                    pass
                
                try:
                    sender.responder_midia()
                except Exception as e:
                    print(e)
        except AttributeError:
            pass
menu()