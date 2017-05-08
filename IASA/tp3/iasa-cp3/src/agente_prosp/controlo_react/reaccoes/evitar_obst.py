
from ecr.reaccao import Reaccao
from psa.actuador import FRT, ESQ, DIR
from psa.accao import Mover
from ecr.resposta import Resposta

class EvitarObst(Reaccao):

    def _gerar_resposta(self, estimulo):
        accao = Mover(ESQ)
        prioridade = 1/(1+estimulo)
        return Resposta(accao,prioridade)

    def _detetar_estimulo(self, percepcao):
        if percepcao[FRT].contacto and percepcao[FRT].obstaculo:
            return True
