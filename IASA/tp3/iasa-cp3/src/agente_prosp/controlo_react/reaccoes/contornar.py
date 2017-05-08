from ecr.reaccao import Reaccao
from psa.actuador import FRT, ESQ, DIR
from psa.accao import Mover
from ecr.resposta import Resposta

class Contornar(Reaccao):

    def _gerar_resposta(self, estimulo):
        accao = Mover(FRT)
        prioridade = 1/(1+estimulo)
        return Resposta(accao,prioridade)

    def _detetar_estimulo(self, percepcao):
        if (percepcao[ESQ].obstaculo and percepcao[ESQ].contacto) or \
        (percepcao[DIR].obstaculo and percepcao[DIR].contacto):
            return True
