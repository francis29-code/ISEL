
from reaccao import Reaccao

class EvitarObst(Reaccao):
    def __init__(self):
        self._direccao = ESQ

    def __gerar_resposta(self, estimulo):
        accao = Mover(self._direccao)
        prioridade = 1/(1+estimulo)
        return Resposta(accao,prioridade)


    def __detetar_estimulo(self, percepcao):
        if percepcao[self._direccao].contacto:
            percepcao[self._direccao].distancia
