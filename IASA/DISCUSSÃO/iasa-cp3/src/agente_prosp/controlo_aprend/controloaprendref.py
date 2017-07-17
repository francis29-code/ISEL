from controlo import Controlo
from controlo_aprend.mecaprend import MecAprend
from psa.util import dirmov
from psa.accao import Mover
import psa

class ControloAprendRef(Controlo):

    def __init__(self):
        self._rmax = 100.0
        self._s = None
        self._a = None
        self._mec_aprend = MecAprend([Mover(ang,ang_abs = True) for ang in dirmov()])

    def processar(self, percepcao):
        
        sn = percepcao.posicao
        an = self._mec_aprend.selecionar_accao(sn)

        if self._s is not None and self._a is not None:
            self._mec_aprend.aprender(self._s, self._a, self._gerar_reforco(percepcao), sn)

        self._a = an
        self._s = sn
        self.mostrar()
        return self._a

    def _gerar_reforco(self,percepcao):
        if percepcao.carga:
            return self._rmax
        if percepcao.colisao:
            return -(self._rmax)

        return -(percepcao.custo_mov)

    def mostrar(self):
        vis = psa.vis(1)
        vis.limpar()
        vis.aprendref(self._mec_aprend)
