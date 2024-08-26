# Importar instâncias
from reader import reader
from message_config import messager

# Bibliotecas de Automação de Navegador
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import gc
import os

# Bibliotecas Funcionais
import time

class sender_class:
    

    
    def __init__(self):
        """
        Método gerador de instância.
        """
        self.reader_import = reader
    
    def import_reader(self):
        """
        Submétodo usado para importar variáveis do método read_messages.py.
        """
        self.driver = self.reader_import.driver
        self.texto = self.reader_import.texto
        self.numero = self.reader_import.numero
        self.wait = self.reader_import.wait
    
    def flow_sender(self):
        """
        Agrupa todos os métodos necessários para poder funcionar o sender.
        """
        try:
            self.import_reader()
        except Exception:
            pass
    
    def enviar_mensagem(self, mensagem):
        """
        Facilitar o envio de mensagens, basta chamá-lo e inserir a mensagem desejada
        Args:
            mensagem (_Any_): _Mensagem ao qual se deseja enviar._
        """
        mensagem = str(mensagem)
        mensagem_tratada = mensagem.splitlines()
        for line in mensagem_tratada:
            inputbox = self.driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
            if "#enter" in line:
                new_line = line.split("#enter")
                msg = "".join(new_line)
                inputbox.send_keys(msg)
                inputbox.send_keys(Keys.SHIFT, Keys.ENTER)
                inputbox.send_keys(Keys.SHIFT, Keys.ENTER)
                inputbox.send_keys("ミ★ MagoBot 1.0 ★彡")  
                enviar = self.driver.find_element(By.XPATH, "//span[@data-icon='send']")
                enviar.click()

            else:
                inputbox.send_keys(line)
                inputbox.send_keys(Keys.SHIFT, Keys.ENTER)
        inputbox.send_keys(Keys.SHIFT, Keys.ENTER)
        inputbox.send_keys("ミ★ MagoBot 1.0 ★彡")   
        enviar = self.driver.find_element(By.XPATH, "//span[@data-icon='send']")
        enviar.click()

    def enviar_midia(self, caminho: str, legenda=None):
        """
        Facilita o envio de mídias no chat api web.
        Args:
            caminho (_str_): _Insira o caminho onde está o arquivo desejado_
            legenda : _Insira a legenda desejada_
        """

        self.wait.until(EC.element_to_be_clickable((By.XPATH, 
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')))
        
        if legenda is not None:
            self.driver.find_element(By.XPATH, 
            '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(legenda)
        else:
            pass
        
        # Abrir ícone de anexos
        while True:
            try:
                wait_plus_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='plus']")))
                if wait_plus_icon:
                    break
                else:
                    pass
            except Exception:
                pass
        
        self.driver.find_element(By.XPATH, "//span[@data-icon='plus']").click()
        
        time.sleep(2)
        
        midias = [
            ".jpg", ".jpeg", ".png", ".gif", ".bmp",
            ".tiff", ".tif", ".ico", ".webp", ".heif", ".heic",
            ".mp4", ".3gp", ".mov"
        ]
        
        midias_tupla = tuple(midias)
        
        # Localizar e inserir o arquivo no input
        try:
            while True:
                try:
                    if caminho.endswith(midias_tupla):
                        self.driver.find_element(By.XPATH,
                        "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']").send_keys(caminho)  
                        break 
                    else:
                        self.driver.find_element(By.XPATH,
                        "//input[@accept='*']").send_keys(caminho)
                        break
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
        # Enviar o arquivo
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']")))
        self.driver.find_element(By.XPATH, "//span[@data-icon='send']").click()
        
    
    def masterizar(self, funcao):
        try:
            funcao
        except Exception:
            pass
        finally:
            gc.collect()
        
    def ler_mensagem(self):
        try:
            messager.texto = reader.texto
        except AttributeError:
            pass
        
    def responder(self):
        try:
            if messager.mensagem is not None:
                self.enviar_mensagem(messager.mensagem)
        except AttributeError:
            pass
        except NameError:
            pass
                    
    def responder_midia(self):
        try:
            if messager.midia is not None:
                self.enviar_midia(messager.midia, messager.legenda)
        except AttributeError:
            pass
        except NameError:
            pass
                                    
                    
sender = sender_class()