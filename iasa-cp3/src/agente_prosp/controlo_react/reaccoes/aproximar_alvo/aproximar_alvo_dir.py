from Reaccao import Reaccao


class AproximarAlvoDir(Reaccao):
    
    def __init__(self, direccao):
        self._direccao = direccao


    def _detectar_estimulo(self, percepcao):
        if percepcao[self._direccao].alvo:
            return percepcao[self._direccao].distancia


    def __gerar_resposta(self, estimulo):
        accao = Mover(self._direccao)
        prioridade = 1 / (1 + estimulo)
        return Resposta(accao, prioridade)
            
