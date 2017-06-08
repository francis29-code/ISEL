from controlo_delib.modelomundo import ModeloMundo
from controlo import Controlo

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
        aux = []
        for estado in self._modelo_mundo.estados():
            elemento = self._modelo_mundo.obter_elem(estado)
            if elemento == "alvo":
                aux.append(estado)

        self._objectivos = aux


    def _planear(self):
        #void
        self._planeador.planear(self._modelo_mundo,self._modelo_mundo.estado,self._objectivos)

    def _executar(self):
        #accao
        operador = self._planeador.obter_accao(self._modelo_mundo.estado)
        if operador is not None:
            #operador tem um accao que e recebido no agente prospector
            return operador

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

    #metodos auxiliares
    def operadoresMundo(self):
        return self._modelo_mundo.operadores()

    def estadoInicial(self):
        return self._modelo_mundo.estado

    def elementos(self):
        return self._modelo_mundo.dicionario_elementos()
