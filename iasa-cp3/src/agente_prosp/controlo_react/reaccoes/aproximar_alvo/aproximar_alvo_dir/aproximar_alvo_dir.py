
from reaccao import Reaccao

class AproximarAlvoDIR(Reaccao):

    def __init__(self,direccao):
        self._direccao = direccao

    def __detetar_estimulo(self,percepcao):
        if percepcao[self._direccao].alvo:
            return percepcao[self._direccao].distancia

    def __gerar_resposta(self,estimulo):
        accao = Mover(self._direccao)
        #estimulo nunca 0
        prioridade = 1/(1+estimulo)
        return Resposta(accao,prioridade)
