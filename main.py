from reader import reader
from sender import sender
from message_config import messager

while True:

    sender.masterizar(reader.flow())

    sender.masterizar(sender.flow_sender())

    sender.masterizar(messager.flow_message())
