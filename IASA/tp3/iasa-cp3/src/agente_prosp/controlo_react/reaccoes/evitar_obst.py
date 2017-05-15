
from ecr.reaccao import Reaccao
from psa.actuador import FRT, ESQ, DIR
from psa.accao import Mover
from ecr.resposta import Resposta

class EvitarObst(Reaccao):

    def _gerar_resposta(self, estimulo):
        return Resposta(Mover(ESQ))

    def _detetar_estimulo(self, percepcao):
        return percepcao[FRT].contacto and percepcao[FRT].obstaculo
