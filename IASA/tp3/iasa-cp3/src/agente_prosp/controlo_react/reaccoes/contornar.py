from reaccao import Reaccao
from psa.actuador import FRT, ESQ, DIR
from psa.accao import Mover
from resposta import Resposta

class Contornar(Reaccao):

    def _gerar_resposta(self, estimulo):
        accao = Mover(FRT)
        prioridade = 1/(1+estimulo)
        return Resposta(accao,prioridade)


    def _detetar_estimulo(self, percepcao):
        if percepcao[ESQ].obstaculo or percepcao[DIR].obstaculo:
            return percepcao[FRT].distancia
