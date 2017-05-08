
from ecr.comportcomp import ComportComp

class Prioridade(ComportComp):

    def __init__(self,listaComportamentos):
        self._comportamentos = listaComportamentos
        ComportComp.__init__(self, self._comportamentos)

    def selecionar_resposta(self, respostas):
        return max(respostas, key=lambda resposta: resposta.prioridade)
