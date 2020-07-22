class Conversa():
    def __init__(self,numero):
        self.numero = numero
        self.estado_atual = 1
        self.estado_anterior = None
        self.estado_futuro = 2
        self.enviado = False
        self.estado_final = 3
        self.resposta_user = None

    def mensagens(self):
        '''
        Retorna a mensagem de cada etapa
        '''
        mensagens = {
            1 : "*[mensagem de bot automatizado]*, igor vc é um cuzão",
            2 : "*[mensagem de bot automatizado]*, igor na real vc é brother"
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
            

