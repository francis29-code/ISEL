from ecr.reaccao import Reaccao
from psa.actuador import FRT, ESQ, DIR
from psa.accao import Mover
from ecr.resposta import Resposta

class Contornar(Reaccao):

    def _gerar_resposta(self, estimulo):
        return Resposta(Mover(FRT))

    def _detetar_estimulo(self, percepcao):
        return (percepcao[ESQ].contacto and percepcao[ESQ].obstaculo) \
        or (percepcao[DIR].contacto and percepcao[DIR].obstaculo)
