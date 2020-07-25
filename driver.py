from selenium import webdriver
from conversa import Conversa
from selenium.webdriver import Chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

GLOBAL_DELAY = 1.5
class Driver (Chrome):
    def __init__(self, executable_path='chromedriver.exe', port=0, options=None, service_args=None, desired_capabilities=None, service_log_path=None, chrome_options=None, keep_alive=True):
        super().__init__(executable_path=executable_path, port=port, options=options, service_args=service_args, desired_capabilities=desired_capabilities, service_log_path=service_log_path, chrome_options=chrome_options, keep_alive=keep_alive)
        self.estado_atual = "busca"
        self.estado_anterior = None
        self.estado_futuro = "etapa 1"    

    @property
    def inicializar(self):
        '''
        Inicializa o bot abrindo o site do wpp
        '''
        self.get('https://web.whatsapp.com/')
        input("Por favor escaneie o qrcode, Pressione enter quando escanear")

    def unread_msg(self):
        cls_conversas = '_210SC' #classe das conversas (len = 17)
        cls_nome = '_3CneP' #classe com o nome da pessoa 
        cls_naoLido = '_31gEB' #classe presente em conversas não lidas
        cvrs = self.find_elements_by_class_name(cls_conversas) #achar conversas
        cvrs_nL = [pessoa for pessoa in cvrs if pessoa.find_elements_by_class_name(cls_naoLido) != []] #filtrar conversas não lidas
        nomes = [pessoa.find_element_by_class_name(cls_nome).text for pessoa in cvrs_nL] #separar o nome dessas conversas
        return nomes 
        
    def check_conversa(self, numero):
        global GLOBAL_DELAY
        conversa_xpath = f"//span[@title='{numero}']"

        try:
            Conversa = self.find_element_by_xpath(conversa_xpath)#achando conversa
            Conversa.click()
            sleep(GLOBAL_DELAY)

            return True
        except:
            print(f"=== Erro ao buscar {numero} ===")
            print("Possíveis motivos: ")
            print(f"-> Não existe conversa com {numero}")
            print("-> Sua conexão está lenta")

            return False

    def send(self,mensagem):
        '''
        Manda a mensagem para a conversa ja aberta no bot
        '''
        global GLOBAL_DELAY

        button_class = '_1U1xa'
        text_box_class = '_3uMse'
        sleep(GLOBAL_DELAY)
        try:
            text_box = self.find_element_by_class_name(text_box_class)#abrindo caixa de diálogo
            text_box.click()
            sleep(GLOBAL_DELAY)

            text_box.send_keys(mensagem)
            button = self.find_element_by_class_name(button_class)#escrevendo mensagem
            button.click()
            sleep(GLOBAL_DELAY)

            return True

        except TimeoutException:
            print("== Tempo de espera excedido(ultrapassado 2 segundos) ==")
            print("Possíveis motivos:")
            print("-> Sua conexão está lenta")
            print("-> Mensagem em branco")
            print("-> Não foi encontrado o botão de envio")

            return False
    def send_to(self,numero,mensagem):
        '''
            Manda a mensagem para o numero designado
        '''
        global GLOBAL_DELAY

        conversa_xpath = f"//span[@title='{numero}']"
        button_class = '_1U1xa'
        text_box_class = '_3uMse'
        sleep(GLOBAL_DELAY)
        try:
            conversa = self.find_element_by_xpath(conversa_xpath)#achando conversa
            conversa.click()
            sleep(GLOBAL_DELAY)

            text_box = self.find_element_by_class_name(text_box_class)#abrindo caixa de diálogo
            text_box.click()
            sleep(GLOBAL_DELAY)

            text_box.send_keys(mensagem)
            button = self.find_element_by_class_name(button_class)#escrevendo mensagem
            button.click()
            sleep(GLOBAL_DELAY)

            return True

        except TimeoutException:
            print("== Tempo de espera excedido(ultrapassado 2 segundos) ==")
            print("Possíveis motivos:")
            print("-> Sua conexão está lenta")
            print("-> Mensagem em branco")
            print("-> Não foi encontrado o botão de envio")

            return False
