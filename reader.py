# Importar instância do driver
from driver_init import init_class

# Bibliotecas de Automação de Navegador
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Bibliotecas Funcionais
import os
import json


class reader_class():
    """
    Classe responsável pela leitura das mensagens.

    Raises:
        Exception: _Em caso de erros, resta você orar e procurar o erro kkk._
    """
    
    try:
        
        def __init__(self):
            """
            Método usado para importar os atributos do ChromeDriver.
            """
            init = init_class()
            import_init = init
            self.driver = init.driver
            self.wait = import_init.wait

        def wait_chat_list(self):
            """
            Método usado para verificar a presença da Lista de Conversa. É usado dentro do método fluxo no loop
            da main para dar continuidade na leitura das mensagens.
            """
            self.wait_list = WebDriverWait(self.driver, timeout=2)
            self.chat_list = self.wait_list.until(EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Lista de conversas']"))) # Aguarda a Lista de Conversa           
        
        def verify_unread_chats(self):    
            """_
            Usado para identificar a presença do ícone de mensagem não lida na lista de conversas do WhatsApp, ao qual
            está identificado no método "wait_chat_list".
            """
            # Condicional da lista de conversa
            if self.chat_list:
                
                # Identifica todas as conversas da lista
                self.iter_chats = self.chat_list.find_elements(By.XPATH, ".//div[@class='x10l6tqk xh8yej3 x1g42fcv']")   

                for self.chat in self.iter_chats:

                    # Verificar a presença do ícone não lido de self.chat
                    try:
                        
                        # Verificar em cada chat se há a presença do ícone de self.chat não lida
                        self.unread_messages_icon = self.chat.find_element(By.XPATH, ".//div[@class='_ahlk']/span")
                        
                        if self.unread_messages_icon:
                            self.chat.click()
                            return
                        
                        else:
                            raise Exception("Pulando click em chat")
                        
                    except NoSuchElementException:
                        self.unread_messages_icon = False
                        pass
                        
                    except Exception as erro:
                        pass
        
        def read_messages(self): # Método de identificação de arquivos estão aqui
            """
            Responsável pela leitura da mensagem em si. Ele identifica a parte do chat na api do WhatsApp no qual
            recebe e envia as mensagens, e itera cada linha. É usado também um arquivo json como forma de 
            reconhecer pelo ID da mensagem se ela já foi lida ou não, para que não haja conflito no projeto.
            """
            
            try:
                
                # Verifica a presença do chat
                self.chat_web_api = self.driver.find_element(By.XPATH, "//div[@role='application']")
                
            except NoSuchElementException:
                self.chat_web_api = False
                
            # Condicional para o chat
            
            if self.chat_web_api:
                
                # Rola para baixo o chat
                self.driver.execute_script("window.scrollBy(0, -500);")
                                
                try:
                    
                    # Localiza todas as linhas (mensagens) dentro do elemento pai
                    self.message = self.chat_web_api.find_elements(By.XPATH, ".//div[@role='row']/div")
                    
                    # Usado para identificar o atributo que será utilizado para encontrar o ID das mensagens
                    attribute_id = "data-id"
                    
                    # Bloco de captura de erros aguardar atributo "ID"
                    try:
                        
                        # Aguarda aparecer o elemento atributo "ID"
                        self.wait.until(EC.element_attribute_to_include((self.message, attribute_id)))
                        
                    except Exception as erro:
                        pass
                    
                    for self.id_extractor in self.message:
                        
                        # Obtem o ID da linha iterada
                        ID = self.id_extractor.get_attribute('data-id')
                        
                        # Extrai o número do emissor
                        self.split_id = ID.split('@')
                        
                        # Split para números pessoais
                        if len(self.split_id) == 2:
                            self.split_id_second_step = ID.split('@')[0]
                            self.numero = self.split_id_second_step.split('_')[1]
                            
                        # Split para número em grupos
                        elif len(self.split_id) == 3:
                            self.split_id_second_step = ID.split('@')[1]   
                            self.numero = self.split_id_second_step.split('_')[2]
                        
                        # Define a lista do banco de dados
                        bancoDados = []
                        
                        # Bloco captura de erros leitura do banco de dados
                        try:
                            
                            # Carrega o banco de dados
                            with open(f"{os.path.dirname(__file__)}\\database\\messages_data.json", "r") as f:
                                bancoDados = json.load(f)
                                
                        except json.JSONDecodeError as erro:
                            print("Erro ao ler banco de dados de ID's")
                            print(f"Detalhes do erro: {erro}")
                            pass
                        
                        # Extrai cada ID do objeto json e armazena os valores em uma lista para futura comparação
                        idsjson = [objeto["id"] for objeto in bancoDados]
                        
                        # Condição para caso ele encontre um novo ID que não está cadastrado no banco de dados
                        if ID not in idsjson:
                            
                            # Cadastro do ID no Banco de Dados
                            cadastroID = [{"id": ID}]

                            # Acrescenta ao final da lista o novo ID
                            bancoDados.extend(cadastroID)

                            # Escreve a nova lista com o novo valor no arquivo JSON
                            with open(f"{os.path.dirname(__file__)}\\database\\messages_data.json", "w") as data:
                                json.dump(bancoDados, data, indent=4)
                                data.write("\n")
                                
                            try:         
                                # Encontra o texto em si da self.mensagem para extração
                                self.texto = self.id_extractor.find_element(By.XPATH, ".//span[contains(@class, 'selectable-text')]/span").text # Extrai o Texto da Mensagem
                                self.texto = self.texto.lower()
                                
                                print(f"{self.numero}: {self.texto}")
                                
                                
                            except Exception as erro:
                                pass
                            
                            break
                        else:
                            pass
                    
                except Exception as erro:
                    print("Ocorreu um erro no Bloco de Código: 'Try 2.0'")
                    print(f"Detalhes do erro: {erro}")
                    pass                 
                                
        def reverify_unread_chats(self):
            """
            Usado para identificar chat não lido e dar continuidade ao loop de mensagens.
            """
            
            # Condicional caso encontre o ícone de self.mensagem não lida
            if self.unread_messages_icon:    
                
                try:
                    # Encontra o elemento clicável para abrir a self.mensagem
                    reverify_chats = self.chat.find_element(By.XPATH, ".//div[@class='_ak8l']")
                    
                    # Realiza o clique
                    reverify_chats.click()
                    
                    # Aguarda o carregamento das linhas
                    self.wait.until(EC.presence_of_all_elements_located((By.XPATH, ".//div[@role='row']/div")))
                
                except Exception as erro:
                    print("Erro no 'read_messages'")
                    print(f"Detalhes do erro: {erro}")                  

        def flow(self):
            """
            O "Flow" ou "Fluxo" é um submétodo usado para agrupar os métodos responsáveis pela leitura as das mensagens.
            """
            self.wait_chat_list()
            self.verify_unread_chats()
            self.read_messages()
            self.reverify_unread_chats()                 
        
    except Exception as excp:
        print(excp)
        
reader = reader_class()