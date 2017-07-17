from controlo_delib.modelomundo import ModeloMundo
from controlo import Controlo
import psa

class ControloDelib(Controlo):

    def __init__(self,planeador):
        self._planeador = planeador
        #instancia um modelo do mundo
        self._modelo_mundo = ModeloMundo()
        #nao esta na arquitetura
        #nao faz sentido planear sem objectivos
        self._objectivos = []

    def _reconsiderar(self):
        #booleano
        #se nao houver objectivos, se nao houver planos, se o mundo mudar
        return not self._objectivos or not self._planeador.plano_pendente() \
            or self._modelo_mundo.alterado

    def _deliberar(self):
        #void
        # objectivos sao gerados aqui
        obj = [estado for estado in self._modelo_mundo.estados() if self._modelo_mundo.obter_elem(estado) == 'alvo']
        self._objectivos = obj


    def _planear(self):
        #void
        if(self._objectivos):
            self._planeador.planear(self._modelo_mundo,self._modelo_mundo.estado,self._objectivos)
        else:
            self._planeador.terminar_plano()

    def _executar(self):
        #accao
        operador = self._planeador.obter_accao(self._modelo_mundo.estado)
        if operador is not None:
            #operador tem um accao que e recebido no agente prospector
            return operador.accao

    def processar(self,percepcao):
        #accao
        self._assimilar(percepcao)

        if (self._reconsiderar()):
            self._deliberar()
            self._planear()

        self.mostrar()

        return self._executar()

    def _assimilar(self,percepcao):
        #atualiza o mundo apos assimilar
        self._modelo_mundo.actualizar(percepcao)

    def mostrar(self):
        vis = psa.vis(1)
        vis.limpar()
        self._planeador.mostrar(self._modelo_mundo.estado,vis)
        self._modelo_mundo.mostrar(vis)
        if(self._objectivos):
            vis.marcar([self._objectivos[0]])
