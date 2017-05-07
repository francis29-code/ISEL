from comportcomp import ComportComp

class Hierarquia(ComportComp):

    def __init__(self,listaComportamentos):
        self._comportamentos = listaComportamentos
        ComportComp.__init__(self, self._comportamentos)

    def selecionar_resposta(self, respostas):
        return respostas[0]
