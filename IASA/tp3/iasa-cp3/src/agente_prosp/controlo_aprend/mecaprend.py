from aprend_ref.memoriaesparsa import MemoriaEsparsa
from aprend_ref.selaccaogreedy import SelAccaoGreedy
from aprend_ref.aprendq import AprendQ

class MecAprend:

    def __init__(self,accoes):
        self._accoes = accoes
        self._mem_aprend = MemoriaEsparsa()
        self._sel_accao = SelAccaoGreedy(self._mem_aprend,self._accoes,0.01)
        self._aprend_ref = AprendQ(self._mem_aprend,self._sel_accao,0.5,0.9)

    def aprender(self, s,a,r,sn):
        self._aprend_ref.aprender(s,a,r,sn)

    def selecionar_accao(self,s):
        self._sel_accao.selecionar_accao(s)
