
class Resposta:

    def __init__(self, Accao, Prioridade=0):
        self._accao = Accao
        self._prioridade = Prioridade

    @property
    def accao(self):
        return self._accao

    @property
    def prioridade(self):
        return self._prioridade
