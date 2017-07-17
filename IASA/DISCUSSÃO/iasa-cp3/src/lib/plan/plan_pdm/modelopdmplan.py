from plan.modeloplan import ModeloPlan
from pdm.modelopdm import ModeloPDM

class ModeloPDMPlan(ModeloPlan,ModeloPDM):

    def __init__(self, modelo_plan,objectivos):
        self._modelo_plan = modelo_plan
        self._objectivos = objectivos
        self._rmax = 100
        self._S = []
        self._A = []
        self._T = {}
        self._R = {}
        # R = se o S onde o agente foi parar, for um dos objectivos, vai devolver RMAX
        self._iniciar_modelo(modelo_plan)

    def _iniciar_modelo(self,modelo_plan):
        self._S = modelo_plan.estados()
        # self._A = A(s) mas neste mundo, A e independente de s
        self._A = modelo_plan.operadores()
        for s in self._S:
            for a in self._A:
                self._gerar_modelo(s,a)

    def _gerar_modelo(self,s,a):
        sn = a.aplicar(s)
        if sn is None:
            self._T[(s,a)] = []
        else:
            #garantidamente apenas temos uma transicao
            #modelo determinista
            self._T[(s,a)] = [(1,sn)]
            self._R[(s,a,sn)] = self._gerar_recompensa(s,a,sn)

    def _gerar_recompensa(self,s,a,sn):
        r = -a.custo(s,sn)
        if sn in self._objectivos:
            r += self._rmax

        return r

    def estados(self):
        return self._S

    def operadores(self):
        return self._A

    def S(self):
        return self._S

    def A(self,s):
        return self._A

    def T(self,s,a):
        return self._T.get((s,a))

    def R(self,s,a,sn):
        return self._R.get((s,a,sn))
