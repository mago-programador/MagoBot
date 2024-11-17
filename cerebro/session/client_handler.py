import os
import cv2
import numpy as np
from PIL import Image
from cerebro.session.driver_init import InitDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


class WhatsAppClient:

    def __init__(self):

        InitDriverImport = InitDriver()  # Importação do objeto de "driver_init.py" dessa forma eu consigo manipular as variáveis que criei no primeiro script.
        self.driver = InitDriverImport.driver  # Importo a instância do webdriver
        self.wait = InitDriverImport.wait  # Importo a instância do WebDriverWait usado para aguardar a presença de algum elemento na página WEB.

        session_path = os.path.join("cerebro", "session", "session_data.txt")  # Arquivo básico para o MagoBot definir se já tem sessão ou não.

        if os.path.exists(session_path):  # Verifica a existência do arquivo de sessão.

            with open(session_path, 'r') as session_file:
                session_data = session_file.read()
                data = session_data.split("=")
                session_information = data[1]
                if session_information == "True":  # Se for verdadeiro, ele não irá tentar reconhecer o QR CODE.
                    print("Sessão ativa encontrada - pulando login")
                    while True:
                        try:

                            chat_list = self.driver.find_element(By.XPATH, "//div[@aria-label='Lista de conversas']")

                            if chat_list:

                                print("sessão iniciada com sucesso")

                                session_path = os.path.join("cerebro", "session", "session_data.txt")

                                with open(session_path, 'a+') as session_file:
                                    session_file.write("session=True")

                                return

                        except UnboundLocalError:
                            pass
                        except NoSuchElementException:
                            pass

        else:
            self.qrcode_whatsapp_extractor()  # Caso seja falso a variável presente no arquivo de sessão, é iniciado o método de reconhecimento do QR CODE.

    def qrcode_whatsapp_extractor(self):

        screenshot_path = os.path.join("cerebro", "session", "screenshot.png")  # Caminho para armazenar temporariamente o print do QR CODE na página WEB.

        while True:
            try:

                qr_content = self.driver.find_element(By.XPATH, "//canvas")  # Fica buscando em loop pelo QR CODE, e só sai do loop quando encontrar o QR CODE.
                if qr_content:
                    break

            except Exception:
                pass

        self.driver.save_screenshot(screenshot_path)  # Captura uma screenshot da página WEB para iniciar a captura do QR CODE.

        # Obtendo as coodernadas e o tamanho do QRCode para recortá-lo.
        location = qr_content.location
        size = qr_content.size
        left = location["x"]
        top = location["y"]
        right = left + size["width"]
        bottom = top + size["height"]

        # Abrir a captura da tela da WEB e passar os parâmetros de largura e altura e salvar o QRCode recortado.
        screenshot = Image.open(screenshot_path)
        qr_code_image = screenshot.crop((left, top, right, bottom))
        qr_code_path = os.path.join("cerebro", "session", "qr_code.png")
        qr_code_image.save(qr_code_path)

        # Carrega o QRCode, captura os pixels para comparação e exibe na tela o QRCode para leitura do usuário.
        qr = cv2.imread(qr_code_path)  # OpenCV carrega a imagem.
        qr_code = np.array(qr_code_image)  # Converte cada pixel da imagem em uma array e guarda essa informações para comparação.
        cv2.imshow("WhatsApp - QRCode", qr)  # Exibe o QRCode em uma janela do OpenCV.

        # Loop de verificação: verifica se há um novo QRCode.
        while True:

            # Essa condicional permite que o OpenCV exiba o QRCode sem parar o fluxo do código, o que geralmente ocorre quando se utiliza cv2.waitKey().
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Caso seja pressionado a tecla 'q' com a janela ativa, ele a fechará.
                break

            try:

                # Caso apareça a mensagem para recarregar o QRCode, ele clicará e fará novamente a leitura do QRCode.
                self.driver.find_element(By.XPATH, '//div[text()="Clique para recarregar o QR code"]/../..').click()
                self.qrcode_whatsapp_extractor()

            except NoSuchElementException:
                pass

            try:

                # Verifica se há um novo QRCode.
                new_qrcode = self.driver.find_element(By.XPATH, "//canvas")  # Elemento responsável pela imagem do QRCode na página WEB.

                if new_qrcode:

                    self.driver.save_screenshot(screenshot_path)  # Captura a imagem em cada volta do loop, mesmo ainda não tendo atualizado.

                    # Obtém localização e tamanho do QRCode para recortá-lo.
                    location = new_qrcode.location
                    size = new_qrcode.size
                    left = location["x"]
                    top = location["y"]
                    right = left + size["width"]
                    bottom = top + size["height"]

                    # Abre a imagem com uma instância do Pillow, recorta e carrega os pixels para comparação com o QRCode que está sendo exibido.
                    screenshot = Image.open(screenshot_path)
                    new_qr_code_image = screenshot.crop((left, top, right, bottom))
                    new_qr_code = np.array(new_qr_code_image)

                    if not np.array_equal(new_qr_code, qr_code):  # Caso haja diferença dos pixels, escaneia novamente o QRCode.

                        cv2.destroyAllWindows()  # Encerra a janela do QRCode que está sendo exibido.
                        print("\nqrcode atualizado, scaneie novamente\n")
                        self.qrcode_whatsapp_extractor()

            except (NoSuchElementException, AttributeError, UnboundLocalError, NoSuchElementException, StaleElementReferenceException):
                pass

            try:

                chat_list = self.driver.find_element(By.XPATH, "//div[@aria-label='Lista de conversas']")

                if chat_list:
                    cv2.destroyAllWindows()  # Encerra a janela do QRCode que está sendo exibido.
                    print("sessão iniciada com sucesso")

                    session_path = os.path.join("cerebro", "session", "session_data.txt")

                    with open(session_path, 'a+') as session_file:
                        session_file.write("session=True")

                    os.remove(screenshot_path)
                    os.remove(qr_code_path)
                    break

            except (UnboundLocalError, NoSuchElementException):
                pass
