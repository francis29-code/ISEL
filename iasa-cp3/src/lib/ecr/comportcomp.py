from comportamento import Comportamento

class ComportComp(Comportamento):

    def __init__(self, listaComportamentos):
        self._comportamentos = listaComportamentos

    def activar(self, Percepcao):
        listaRespostas=[]
        for comportamento in _comportamentos:
            resposta = comportamento.activar(Percepcao)
            #lista de respostas
            listaRespostas.append(resposta)

        if(len(listaRespostas)>0):
            return self.selecionar_resposta(respostas)


    def selecionar_resposta(self, respostas):
        raise NotImplementedError
