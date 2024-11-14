import os
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
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
                    return

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

        # Essa parte básica é apenas para converter de foto para apresentar o QR CODE no console.
        location = qr_content.location
        size = qr_content.size
        left = location["x"]
        top = location["y"]
        right = left + size["width"]
        bottom = top + size["height"]

        screenshot = Image.open(screenshot_path)
        qr_code_image = screenshot.crop((left, top, right, bottom))

        qr_code_data = decode(qr_code_image)

        if qr_code_data:
            qr_content = qr_code_data[0].data.decode("utf-8")

        else:
            print("QR Code não encontrado ou não legível")

        qr = qrcode.QRCode(
            version=1,
            border=1,
        )

        qr.add_data(qr_content)
        qr.make(fit=True)

        qr.print_ascii(invert=True)

        while True:

            try:
                new_qrcode = self.driver.find_element(By.XPATH, "//canvas")
                if new_qrcode:

                    self.driver.save_screenshot(screenshot_path)

                    location = new_qrcode.location
                    size = new_qrcode.size
                    left = location["x"]
                    top = location["y"]
                    right = left + size["width"]
                    bottom = top + size["height"]

                    screenshot = Image.open(screenshot_path)
                    qr_code_image = screenshot.crop((left, top, right, bottom))

                    qr_code_data = decode(qr_code_image)

                    if qr_code_data:
                        new_qrcode = qr_code_data[0].data.decode("utf-8")

                        if new_qrcode != qr_content:
                            print("\nqrcode atualizado, scaneie novamente\n")
                            self.qrcode_whatsapp_extractor()

                    else:
                        print("QR Code não encontrado ou não legível")
            except NoSuchElementException:
                pass
            except AttributeError:
                pass
            except UnboundLocalError:
                pass
            except NoSuchElementException:
                pass
            except StaleElementReferenceException:
                pass

            try:

                chat_list = self.driver.find_element(By.XPATH, "//div[@aria-label='Lista de conversas']")

                if chat_list:

                    session_path = os.path.join("cerebro", "session", "session_data.txt")

                    with open(session_path, 'a+') as session_file:
                        session_file.write("session=True")

                    os.remove(screenshot_path)
                    break
            except UnboundLocalError:
                pass
            except NoSuchElementException:
                pass
