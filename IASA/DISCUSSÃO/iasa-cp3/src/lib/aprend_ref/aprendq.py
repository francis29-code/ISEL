from aprend_ref.aprendref import AprendRef

class AprendQ(AprendRef):

    def __init__(self,mem_aprend,sel_accao,alfa,gama):
        AprendRef.__init__(self,mem_aprend,sel_accao)
        self._alfa = alfa
        self._gama = gama

    def aprender(self,s,a,r,sn):
        Q = self._mem_aprend.obter(s, a)
        A_next = self._sel_accao.max_accao(sn)
        Q_next = self._mem_aprend.obter(sn, A_next)
        Q_final = Q + self._alfa*(r+(self._gama*Q_next)-Q)
        self._mem_aprend.actualizar(s,a,Q_final)
