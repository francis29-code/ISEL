
from aprend_ref.selaccao import SelAccao
from random import random,choice

class SelAccaoEGreedy(SelAccao):

    def __init__(self,mem_aprend,accoes,epsilon):

        self._mem_aprend = mem_aprend
        self._accoes = accoes
        self._epsilon = epsilon

    def selecionar_accao(self,s):
        valor_aleatorio = random()

        if(valor_aleatorio <= epsilon):
            return self.explorar(s)
        else:
            return self.max_accao(s)

    def max_accao(self,s):
        return max(self._accoes, key = lambda: self._mem_aprend.obter(s,self._accoes.get(s)) )

    def explorar(self,s):
        return choice(self._accoes)
