import cerebro


class MagoBotClient:
    """
    _MagoBotClient_

    Olá, seja bem-vindo ao MagoBot, talvez o MagoBot não seja o bot mais completo e avançado que você já viu na sua vida
    de dev, mais com certeza é um bot que você terá total controle caso estude-o bem.

    Nessa classe, eu importo algumas classes, métodos e atributos importantes, e no método (ou função) "config" é onde você vai configurar
    seu bot com os comandos que deseja receber e os comandos que quer que ele envie.

    Para utilizar é muito simples, basta você adicionar uma condicional da mensagem recebida, e utilizar uma das funções à baixo para
    adicionar uma resposta, seja em mensagem, mídia e por aí vai...

    Comandos que podem ser utilizados até o momento que escrevi essa linha:
    - self.send("conteúdo da mensagem") - geralmente recebe: strings, int, floats, listas, dicionários e etc... se você utilizar o objeto de alguma
    lib muito específico, obviamente provável que seja necessário você adptá-lo.

    - self.send_media(caminho, "legenda") - a legenda segue a mesma lógica do send, o caminho eu aconselho você utilizar a lib "os" para que não haja problemas de caminho

    Atenção: Em casos de dúvidas, acesse "README" para mais informações e funções.
    """

    def __init__(self):
        """
        Aqui não tem muito o que falar, eu importo a classe sender que e os atributos que serão utilizados para ler as mensagens e respondê-las.
        """
        self.magobot = cerebro.SenderMessages()

        self.send = self.magobot.send
        self.send_media = self.magobot.send_media
        self.atualizar_valores = self.magobot.importar_valores

    def main(self):
        """
        Aqui fica o loop principal, basicamente ele permite que o robô não pare e fique verificando e reverificando a presença de chats e mensagens.
        """

        while True:

            # Métodos necesśario para realizar a leitura da mensagem e retornar o atributo "mensagens"
            self.magobot.wait_chat_list()
            self.magobot.verify_unread_chats()
            self.magobot.read_messages()
            self.atualizar_valores()

            mensagens_recebidas = self.verify_messages()  # Usado para verificar se há ou não mensagem para serem lidas.

            if mensagens_recebidas:

                for msg in mensagens_recebidas:  # Caso haja mensagens para serem lidas, ele irá chamar o método de configuração de mensagens.
                    self.config(msg)

            self.magobot.reverify_unread_chats()

    def verify_messages(self):
        """
        Tratamento simples para erro de atributos, caso não haja mensagem para serem lidas, ele retornará uma lista vazia.
        """
        try:

            return self.magobot.mensagens

        except AttributeError:
            return []

    def config(self, mensagem):
        """
        Aqui meu grande amigo, é onde vocẽ configura o MagoBot. Basicamente essa "função" recebe o argumento mensagens herdado da main, e permite que você
        crie uma estrutura lógica de comando-resposta simples e escalável.

        Para deixar o código mais legível ao invés da velha estrutura if-elif-else, utilizamos a match-case introduzida no Python 3.10.
        Veja como é simples e linda de usar.
        """

        match mensagem:

            case "Cambio":
                self.send("Olá Mundo!")

            case "Jarvis":
                self.send("Olá senhor, como posso ajudar?")


MagoBot = MagoBotClient()
MagoBot.main()  # Chamando o método main para executar o bot.
