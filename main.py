from reader import reader
from sender import sender
from message_config import SendMessage

messager = SendMessage()

while True:

    sender.masterizar(reader.flow())

    sender.masterizar(sender.flow_sender())

    sender.masterizar(messager.text())

    sender.ler_mensagem()

    sender.masterizar(messager.config())

    sender.responder()
