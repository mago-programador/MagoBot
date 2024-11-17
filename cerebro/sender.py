# Importar instâncias
from cerebro.reader import ReaderMessages

# Bibliotecas de Automação de Navegador
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

# Bibliotecas Funcionais
import time


class SenderMessages:
    """
    _sender_

    classe utilizada para criar funções com o propósito de:
    - importar os atributos da reader;
    - enviar mensagens;
    - enviar mídias.
    """

    def __init__(self):
        """
        Método gerador de instância.
        """
        self.reader_import = ReaderMessages()

        self.driver = self.reader_import.driver
        self.wait = self.reader_import.wait

        # Métodos responsáveis pela leitura da mensagem
        self.wait_chat_list = self.reader_import.wait_chat_list
        self.verify_unread_chats = self.reader_import.verify_unread_chats
        self.read_messages = self.reader_import.read_messages
        self.reverify_unread_chats = self.reader_import.reverify_unread_chats

    def importar_valores(self):
        try:
            self.mensagens = self.reader_import.lista_mensagens
            self.numero = self.reader_import.numero
        except AttributeError:  # Nem sempre no loop o bot terá uma mensagem para ler, por isso basta passar direto e tentar ler na próxima vez.
            pass

    def send(self, mensagem):
        """
        Facilitar o envio de mensagens, basta chamá-lo e inserir a mensagem desejada
        Args:
            mensagem (_Any_): _Mensagem ao qual se deseja enviar._
        """
        mensagem = str(mensagem)
        split_msg = mensagem.splitlines()
        for line in split_msg:

            inputbox = self.driver.find_element(
                By.XPATH,
                '//div[@aria-placeholder="Digite uma mensagem"]/p',
            )

            if line:
                inputbox.send_keys(line)
            inputbox.send_keys(Keys.SHIFT, Keys.ENTER)
        # Para excluir a marca do MagoBot das mensagens basta apagar as linhas deste bloco
        inputbox.send_keys(Keys.SHIFT, Keys.ENTER)
        inputbox.send_keys(Keys.SHIFT, Keys.ENTER)
        inputbox.send_keys("ミ★ MagoBot 2.0 ★彡")
        # Apague até aqui

        send_button = self.driver.find_element(By.XPATH, "//span[@data-icon='send']")
        send_button.click()

    def send_media(self, caminho: str, legenda=str):
        """
        Facilita o envio de mídias no chat api web.
        Args:
            caminho (_str_): _Insira o caminho onde está o arquivo desejado_
            legenda : _Insira a legenda desejada_
        """

        self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//div[@aria-placeholder="Digite uma mensagem"]/p',
                )
            )
        )

        if legenda is not None:
            self.driver.find_element(
                By.XPATH,
                '//div[@aria-placeholder="Digite uma mensagem"]/p',
            ).send_keys(legenda)
        else:
            pass

        # Abrir ícone de anexos
        while True:
            try:
                wait_plus_icon = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='plus']"))
                )
                if wait_plus_icon:
                    break
                else:
                    pass
            except Exception:
                pass

        self.driver.find_element(By.XPATH, "//span[@data-icon='plus']").click()

        time.sleep(2)

        midias = [
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".bmp",
            ".tiff",
            ".tif",
            ".ico",
            ".webp",
            ".heif",
            ".heic",
            ".mp4",
            ".3gp",
            ".mov",
        ]

        midias_tupla = tuple(midias)

        # Localizar e inserir o arquivo no input
        try:
            while True:
                try:
                    if caminho.endswith(midias_tupla):
                        self.driver.find_element(
                            By.XPATH,
                            "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']",
                        ).send_keys(caminho)
                        break
                    else:
                        self.driver.find_element(
                            By.XPATH, "//input[@accept='*']"
                        ).send_keys(caminho)
                        break
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
        # Enviar o arquivo
        time.sleep(2)
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']"))
        )
        self.driver.find_element(By.XPATH, "//span[@data-icon='send']").click()
