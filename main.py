from selenium import webdriver
from driver import Driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from conversa import Conversa

wppbot = Driver()
wppbot.inicializar

alice = Conversa('Sei Lá N Sei Explicar ♥️♥️♥️♥️')
igor = Conversa('Igor Arrombado Filho Da Puta Escroto De Merda Da Desgraça')
conversas = [alice,igor]

while conversas != []:
    for conversa in conversas:
        print("Número da conversa: ", conversa.numero)
        print("Estado atual: ", conversa.estado_atual)
        print("==================")
        check_envio = wppbot.send(conversa.numero, conversa.mensagens())
        conversa.enviado = check_envio #checando se a mensagem foi enviada
        conversa.check_state()
        print("Estado atual: ", conversa.estado_atual)
        print("==================")

        if conversa.estado_final == conversa.estado_atual:
            conversas.remove(conversa)