from controlo_delib.modelomundo import ModeloMundo
from controlo_react.controlo import Controlo

class ControloDelib(Controlo):

    def __init__(self,planeador):
        self._planeador = planeador
        self._modelo_mundo = ModeloMundo()
        #não está na arquitetura
        #não faz sentido planear sem objectivos
        self._objectivos = []

    def _reconsiderar(self):
        #booleano
        #se nao houver objectivos, se nao houver planos, se o mundo mudar
        if len(self._objectivos)==0 or self._planeador.plano_pendente() \
            or self._modelo_mundo.alterado:
            return True

        return False

    def _deliberar(self):
        #void
        # objectivos são gerados aqui
        for estado in self._modelo_mundo.estados():
            elemento = self._modelo_mundo.obter_elem(estado)
            if elemento == "alvo":
                self._objectivos.append(estado)

    def _planear(self):
        #void
        self._planeador.planear(self._modelo_mundo,self._modelo_mundo.estado,self._objectivos)

    def _executar(self):
        #accao
        operador = obter_accao(self._planeador.obter_accao(self._modelo_mundo.estado))
        if operador is not None:
            return operador.accao

    def processar(self,percepcao):
        #accao
        self._assimilar(percepcao)

        if (self._reconsiderar()):
            self._deliberar()
            self._planear()

        return self._executar()

    def _assimilar(self,percepcao):
        #atualiza o mundo apos assimilar
        self._modelo_mundo.actualizar(percepcao)
