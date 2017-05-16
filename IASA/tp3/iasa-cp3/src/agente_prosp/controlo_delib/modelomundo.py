
from controlo_delib.modeloplan import ModeloPlan
from psa.util import dirmov
from controlo_delib.operadormover import OperadorMover

class ModeloMundo(ModeloPlan):

    def __init__(self):
        #estado e um tuplo (X,Y)
        self.alterado = False
        #dicionario proveniente da percepcao do ambiente
        self._elementos = {}
        #posicao atual do agente
        self.estado = None
        #todos os estado do dicionario
        self._estados = None
        #instanciar operadores com todas as direcoes
        #sendo que self e o proprio modelo_mundo
        #sendo que move e um angulo
        self._operadores = [OperadorMover(self,move) for move in dirmov()]
        # for move in dirmov:
        #     self._operadores.append(OperadorMover(self,move))

    def obter_elem(self,estado):
        #string
        elemento = self._elementos.get(estado)
        if elemento is not None:
            #retorna string "ALVO" ou nao
            return elemento

    def actualizar(self,percepcao):
        #void
        #percepcao.imagem = dict()
        #imagem = 'alvo' 'obst' 'vazio'
        #posicoes como keys
        # percepcao.posicao = TUPLO (X,Y)
        if self._elementos != percepcao.imagem:
            self._elementos = percepcao.imagem
            self.estado = percepcao.posicao
            self.alterado = True
            self._estados = percepcao.imagem.keys()
        else:
            self.alterado = False
            self.estado = percepcao.posicao
            self._estados = percepcao.imagem.keys()


    def operadores(self):
        #lista de operadores do modelo_mundo
        return self._operadores

    def estados(self):
        #lista de tuplos do dicionario
        return self._estados

    @property
    def estado(self):
        return self.estado

    @property
    def alterado(self):
        return self.alterado
