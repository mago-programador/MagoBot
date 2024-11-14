from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Op
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import os


class InitDriver:
    """
    Classe responsável pela inicialização e configuração do ChromeDriver.
    """

    def __init__(self):
        """Start Driver

        Neste método nós iniciamos o ChromeDriver, aplicamos configurações importantes para o projeto e
        criamos pastas e arquivos essenciais para o funcionamento do MagoBot.

        """
        try:

            print("\033[92mMagoBot v1.0\033[0m")  # Essa aqui é a minha marca kkk. O meu "eu estive aqui", fique à vontade para personalizá-lo.
            print("\n")
            print('iniciando...')

            # Caminhos importantes
            self.database = os.path.join("cerebro", "database")  # Caminho da pasta "database".
            self.message_database_path = os.path.join("cerebro/database", "messages_data.json")  # Caminho do arquivo onde fica armazenado o ID de cada mensagem.
            self.download_path = os.path.join("cerebro/database", "downloads")  # Caminho da pasta de downloads do MagoBot.

            # Condicionais para verificar a existência de caminhos importantes
            # Verifica a existência da pasta "database", caso não exista será criada.
            if not os.path.exists(self.database):
                os.makedirs(self.database)
                print("database criada")

            # Verifica a existência do arquivo JSON "messages_data", caso não exista será criado.
            # Caso haja dúvidas do seu propósito, ele basicamente armazena o ID de cada mensagem recebida,
            # fazendo assim que o bot não responda mais de uma vez a mesma mensagem.
            if not os.path.exists(self.message_database_path):
                with open(self.message_database_path, "a+") as file:
                    file.write("[]")
                    print("base de id's das mensagens - criada com sucesso")

            # Verifica a existência o arquivo texto "whitelist", usado para definir à quem o bot poderá
            # enviar mensagens, caso ele continue vazio, o bot responderá à todos que utilizarem os comandos definidos pelo usuário.
            if not os.path.exists(self.whitelist_path):
                with open(self.whitelist_path, "a+") as file:
                    print("whitelist - criada com sucesso")

            # Aqui se encontra todas as configurações que eu considero necessária para o bom funcionamento do bot.
            options = Op()  # Inicializa a instância "options" para configurar as opçoes do navegador.
            options.add_argument("--headless")  # Inicia o chrome webdriver em segundo plano.
            options.add_argument("--allow-running-insecure-content")  # Habilita o carregamento de conteúdo não seguro, em algumas máquinas essa opção evita erros.
            options.add_argument("--window-size=1920,1080")  # Seta o tamanho da janela, mesmo que em segundo plano, permitindo o carregamento dos elementos web.
            options.add_argument("--allow-insecure-localhost")  # Habilita conteúdo não seguro no localhost.
            cookies_path = f"{os.path.join('cerebro','session', 'cookies')}"  # Caminho padrão do script para armazenar a pasta "cookies".
            options.add_argument(f"--user-data-dir={cookies_path}")  # Seta o caminho da pasta onde ficará os cookies do navegador e guardará a sessão.
            options.add_argument("--no-first-run")  # Desabilita a tela inicial do navegador, que aparece quando o usuário abre o navegador.
            options.add_argument("--no-sandbox")  # Aumenta o desempenho do ambiente do navegador.
            options.add_argument("--disable-webgl")  # Desabilita o webgl responsável pela renderização gráfica, melhora o desempenho do bot.
            options.add_argument("--disable-gpu")  # Desativa o uso da GPU no bot, em algumas máquinas não se fará necessário, somente em casos de instabilidade mas já deixei como padrão.
            options.add_argument("--disable-renderer-backgrounding")  # Evita que o navegador limite o uso de recursos quando o whatsapp estiver ou sem segundo plano ou minimizado.
            options.add_argument("--disable-backgrounding-occluded-windows")  # Evita que janelas ocultas reduzam o consumo de recursos do navegador.
            options.add_argument("--disable-hang-monitor")  # Evita que o navegador "trave", quando o bot roda por muito tempo, pode acontecer de travar, ele desativa o monitor de travamento.
            options.add_experimental_option(
                "prefs",
                {
                    "excludeSwitches": ["enable-logging"],  # Exclui logs desnecessários, para não ficar poluindo o console.
                    "download.default_directory": self.download_path,  # É difinido o caminho caso seja feito o download de algum arquivo no MagoBot.
                },
            )

            # Instâncias co chromedriver
            self.driver = webdriver.Chrome(options=options)
            self.wait = WebDriverWait(self.driver, 120)
            self.ActionChains = ActionChains(self.driver)

            # Link do WhatsApp
            self.driver.get("https://web.whatsapp.com/")

        except Exception as excp:
            print(excp)
