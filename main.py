from reader import reader
from sender import sender
from message_config import messager

while True:

    sender.masterizar(reader.flow())

    sender.masterizar(sender.flow_sender())

    sender.masterizar(messager.text())

    sender.ler_mensagem()

    sender.masterizar(messager.config())

    try:
        sender.responder()
    except Exception:
        pass
    
    try:
        sender.responder_midia()
    except Exception as e:
        print(e)