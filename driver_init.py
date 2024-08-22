from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Op
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os


class init_class:
    """
    Classe responsável pelo início e configuração do ChromeDriver.
    """

    def __init__(self):
        """Start Driver

    Neste método nós iniciamos o ChromeDriver e aplicamos configurações necessárias para o projeto.

    """
        try:
            
            print("\033[92mMagoBot v1.0\033[0m")
            print("\n")
            
            if not os.path.exists(f"{os.path.dirname(__file__)}\\database"):
                os.makedirs(f'{os.path.dirname(__file__)}\\database')
                print("Database criada")
                with open(f"{os.path.dirname(__file__)}\\database\\messages_data.json", "w") as file:
                    file.write("[]")
                print("JSON criado com sucesso")
                print("Database se faz necessária para armazenar o ID da mensagem")
                
            options = Op()
            options.add_experimental_option("detach", True)
            options.add_argument("--allow-running-insecure-content")
            options.add_argument("--allow-insecure-localhost")
            cookies_path = f"{os.path.dirname(__file__)}\\Cookies"
            options.add_argument(f"--user-data-dir={cookies_path}")
            options.add_argument("--no-first-run")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-webgl")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-renderer-backgrounding")
            options.add_argument("--disable-backgrounding-occluded-windows")
            options.add_argument("--disable-hang-monitor")
            options.add_experimental_option('prefs', {
                'excludeSwitches': ['enable-logging'],
                'download.default_directory': 'G:\\Meu Drive\\S.A.D\\{Banco de Dados}\\Faturamento e Cotas',
            })
            
            self.driver = webdriver.Chrome(options=options)
            
            self.driver.get("https://web.whatsapp.com/")
            
            self.wait = WebDriverWait(self.driver, 120)
            
            self.ActionChains = ActionChains(self.driver)
            
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='Lista de conversas']")))
            
        except Exception as excp:
            print(excp)
            
