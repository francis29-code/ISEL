from comportcomp import ComportComp

class Hierarquia(ComportComp):

    def __init__(self,listaComportamentos):
        self._comportamentos = listaComportamentos

    def selecionar_resposta(self, respostas):
        return respostas[0]
