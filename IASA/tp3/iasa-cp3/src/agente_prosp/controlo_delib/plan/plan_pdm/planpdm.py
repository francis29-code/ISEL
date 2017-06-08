from controlo_delib.plan.plan_pdm.modelopdmplan import ModeloPDMPlan
from controlo_delib.plan.planeador import Planeador
from controlo_delib.pdm.pdm import PDM

class PlanPDM(Planeador):

    def __init__(self):
        self._gama = 0.95
        self._delta_max = 1.0
        self._utilidade = None
        self._politica = {}
        self._pdm = PDM(self._gama,self._delta_max)

    def planear(self,modelo_plan, estado_inicial, objectivos):
        # problemaplan = (estado_incial,estado_final,operadores)
        modelo = ModeloPDMPlan(modelo_plan,objectivos)
        self._utilidade, self._politica =  self._pdm.resolver(modelo)
        if not self._politica:
            self.teminar_plano()

    def obter_accao(self,s):
        #s estado
        #ir a utilidade ver quala a accao
        #devolve accao para aquele estado
        #e como apenas estamos assumir uma transicao
        return self._politica.get(s)

    def plano_pendente(self):
        return self._pdm

    def terminar_plano(self):
        #termina um plano
        self._pdm = {}
