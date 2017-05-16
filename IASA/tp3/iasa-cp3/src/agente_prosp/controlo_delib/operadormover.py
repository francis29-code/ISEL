from psa.accao import Mover
from psa.util import dist,mover
from pee.modprob.operador import Operador

class OperadorMover(Operador):

    def __init__(self,modelo_mundo,ang):
        self._ang = ang
        self.accao = Mover(ang)
        self._modelo_mundo = modelo_mundo

    @property
    def accao(self):
        return self.accao

    def aplicar(self,estado):
        #mover(posicao(xy),angulo):novaPosicao(XY)
        #so e valido se mover se a posicao a que se quiser mover for != de obst
        novo_estado = mover(estado,self._ang)
        if novo_estado is not None and self._modelo_mundo.obter_elem(estado) != 'obst':
            return novo_estado

    def custo(self,estado,novo_estado):
        #dist(duasposicao): distancia euclidiana de duas posicoes
        return dist(estado,novo_estado)
