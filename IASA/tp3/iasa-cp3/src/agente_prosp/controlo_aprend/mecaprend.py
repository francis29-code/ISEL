from aprend_ref.memoriaesparsa import MemoriaEsparsa
from aprend_ref.selaccaoegreedy import SelAccaoEGreedy
from aprend_ref.aprendq import AprendQ

class MecAprend:

    def __init__(self,accoes):
        self._accoes = accoes
        epsilon = 0.01
        alpha = 0.5
        gama = 0.9
        self._mem_aprend = MemoriaEsparsa()
        self._sel_accao = SelAccaoEGreedy(self._mem_aprend,self._accoes,epsilon)
        self._aprend_ref = AprendQ(self._mem_aprend,self._sel_accao,alpha,gama)

    def aprender(self, s,a,r,sn):
        self._aprend_ref.aprender(s,a,r,sn)

    def selecionar_accao(self,s):
        return self._sel_accao.selecionar_accao(s)
