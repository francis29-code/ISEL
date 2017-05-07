
from reaccao import Reaccao
from psa.actuador import FRT,ESQ,DIR
from psa.accao import Mover
from resposta import Resposta

class AproximarAlvoDIR(Reaccao):

    def __init__(self,direccao):
        self._direccao = direccao

    def _detetar_estimulo(self,percepcao):
        if percepcao[self._direccao].alvo:
            return percepcao[self._direccao].distancia

    def _gerar_resposta(self,estimulo):
        accao = Mover(self._direccao)
        #estimulo nunca 0
        prioridade = 1/(1+estimulo)
        return Resposta(accao,prioridade)
