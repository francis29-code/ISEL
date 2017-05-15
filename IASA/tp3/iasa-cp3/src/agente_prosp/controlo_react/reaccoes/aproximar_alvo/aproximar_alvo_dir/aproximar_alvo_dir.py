
from ecr.reaccao import Reaccao
from psa.actuador import FRT,ESQ,DIR
from psa.accao import Mover
from ecr.resposta import Resposta

class AproximarAlvoDIR(Reaccao):

    def __init__(self,direccao):
        self._direccao = direccao

    def _detetar_estimulo(self,percepcao):
        if percepcao[self._direccao].alvo:
            return percepcao[self._direccao].distancia #distancia do alvo

    def _gerar_resposta(self,estimulo):
        accao = Mover(self._direccao)
        prioridade = 1/(1+estimulo)
        return Resposta(accao,prioridade)
