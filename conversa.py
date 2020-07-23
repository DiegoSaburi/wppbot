class Conversa():
    def __init__(self,numero):
        self.numero = numero
        self.estado_atual = 1
        self.estado_anterior = None
        self.estado_futuro = 2
        self.enviado = False
        self.estado_final = 3
        self.resposta_user = None
    def __str__(self):
        return self.numero
    def mensagens(self):
        '''
        Retorna a mensagem de cada etapa
        '''
        mensagens = {
            1 : "MENSAGEM DE TESTE 1",
            2 : "MENSAGEM DE TESTE 2"
        }

        return mensagens[self.estado_atual]

    def check_state(self):
        '''
        Checa se há mudança de estado ou não, se sim ele muda o estado
        '''
        if self.enviado == True:
            self.estado_anterior = self.estado_atual
            self.estado_atual = self.estado_futuro
            if self.estado_futuro < 3:
                self.estado_futuro += 1
            

