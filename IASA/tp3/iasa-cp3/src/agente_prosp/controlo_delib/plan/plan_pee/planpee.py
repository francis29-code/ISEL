from controlo_delib.plan.planeador import Planeador
from controlo_delib.plan.pla_pee.problemaplan import ProblemaPlan

class PlanPEE(Planeador):

    def __init__(self,mec_pee):
        #qualquer procura larg,prof,profit,AA,sofrega,custounif
        self._mec_pee = mec_pee
        #plano é um conjunto de operadores que fazem parte de uma solução
        #visto que as soluções do agente são movimentos no espaço AMB
        self._plano = None

    def planear(self,modelo_plan,estado_inicial,objectivos):
        #metodo utilizado no planear do controlo delib, de modo a obter um conjunto de
        #acoes/operadores
        problema = ProblemaPlan(estado_inicial,objectivos[0],modelo_plan.operadores())
        #conjunto de passos_solucao que na verdade são operadores com acçoes
        solucao = self._mec_pee.resolver(problema)
        if solucao is not None:
            #se existir solucao para o estado final,
            #é subentendido que existe um plano de acoes
            self._plano = [passo_solucao.operador for passo_solucao in solucao[1:]]

    def obter_accao(self,estado):
        #nao necessita do estado
        #visto a ser um um controlo_delib
        #mas retira-se do plano
        operador = self._plano[0]
        self._plano.pop(0)
        #retorna um operador para ser utilizado no controlo_delib
        #de modo a aceder à ações presente no operador
        return operador

    def plano_pendente(self):
        #se não existem operadores no plano, não existem planos de ações pendentes
        return len(self._plano)==0

    def terminar_plano(self):
        #termina plano, passam a não existir operadores
        self._plano = []
