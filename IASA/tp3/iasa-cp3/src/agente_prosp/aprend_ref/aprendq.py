from controlo_delib.aprend_ref.aprend_ref import AprendRef

class AprendQ(AprendRef):

    def __init__(self,mem_aprend,sel_accao,alfa,gama):
        #heranca
        AprendRef.__init__(mem_aprend,sel_accao,alfa,gama)
        self._alfa = alfa
        self._gama = gama
        self._mem_aprend = mem_aprend
        self._sel_accao = sel_accao

    def aprender(self,s,a,r,sn):
        an = self._sel_accao.max_accao(sn)
        qsa = self._mem_aprend.obter(s,a)
        qsnan = self._mem_apred.obter(sn,an)
        q = qsa +  self._alfa * (r + self._gama * qsnan - qsa)
        self._mem_aprend.actualizar(s,a,q)
