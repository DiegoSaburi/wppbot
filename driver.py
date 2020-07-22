from selenium import webdriver
from conversa import Conversa
from selenium.webdriver import Chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Driver (Chrome):
    def __init__(self, executable_path='chromedriver.exe', port=0, options=None, service_args=None, desired_capabilities=None, service_log_path=None, chrome_options=None, keep_alive=True):
        super().__init__(executable_path=executable_path, port=port, options=options, service_args=service_args, desired_capabilities=desired_capabilities, service_log_path=service_log_path, chrome_options=chrome_options, keep_alive=keep_alive)
        self.estado_atual = "busca"
        self.estado_anterior = None
        self.estado_futuro = "etapa 1"    

    @property
    def inicializar(self):
        self.get('https://web.whatsapp.com/')
        input("Por favor escaneie o qrcode, Pressione enter quando escanear")

    def send(self,numero,mensagem):
        conversa_xpath = f"//span[@title='{numero}']"
        button_class = '_1U1xa'
        text_box_class = '_3uMse'
        sleep(1.5)
        try:
            conversa = self.find_element_by_xpath(conversa_xpath)
            conversa.click()
            sleep(1.5)
            text_box = self.find_element_by_class_name(text_box_class)
            text_box.click()
            sleep(1.5)
            text_box.send_keys(mensagem)
            button = self.find_element_by_class_name(button_class)
            button.click()
            sleep(1.5)

            return True

        except TimeoutException:
            print("== Tempo de espera excedido(ultrapassado 2 segundos) ==")
            print("Possíveis motivos:")
            print("-> Sua conexão está lenta")
            print("-> Mensagem em branco")
            print("-> Não foi encontrado o botão de envio")

            return False
    
