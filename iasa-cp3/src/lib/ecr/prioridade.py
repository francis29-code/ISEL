
from comportcomp import ComportComp

class Prioridade(ComportComp):

    def __init__(self,listaComportamentos):
        self._comportamentos = listaComportamentos

    def selecionar_respostas(self, respostas):
        return max(respostas, key=lambda resposta: resposta.prioridade)
