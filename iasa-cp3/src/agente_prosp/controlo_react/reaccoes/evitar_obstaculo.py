from Reaccao import Reaccao

class Evitar(Reaccao):


    def __init__(self):
        self._direccao = "ESQ"


    def _detectar_estimulo(self, percepcao):
        if percepcao[self._direccao].contacto:
            return percepcao[self._direccao].distancia


    def __gerar_resposta(self, estimulo):
        accao = Mover(self._direccao)
        prioridade = 1 / (1 + estimulo)
        return Resposta(accao, prioridade)
