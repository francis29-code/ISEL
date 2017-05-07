from comportamento import Comportamento

class ComportComp(Comportamento):

    def __init__(self, listaComportamentos):
        self._comportamentos = listaComportamentos

    def activar(self, percepcao):
        listaRespostas=[]
        for comportamento in self._comportamentos:
            resposta = comportamento.activar(percepcao)
            #lista de respostas
            if resposta is not None:
                listaRespostas.append(resposta)

        if(len(listaRespostas)>0):
            return self.selecionar_resposta(listaRespostas)


    def selecionar_resposta(self, respostas):
        raise NotImplementedError
