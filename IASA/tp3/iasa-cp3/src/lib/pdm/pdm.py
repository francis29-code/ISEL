
class PDM:

    def __init__(self,gama,delta_max):
        self._gama = gama
        self._delta_max = delta_max

    def utilidade(self, modelo):
        #modelo PDM
        U ={s:0 for s in modelo.S()}
        while True:
            Uant = U.copy()
            delta =0
            for s in modelo.S():
                U[s] = max(self.util_accao(s,a,Uant,modelo) for a in modelo.A(s))
                delta = max(delta, abs(U[s]-Uant[s]))

            if(delta < self._delta_max):
                break
        return U

    def util_accao(self,s,a,U,modelo):
        #s estado
        #a accao
        #U utilidade
        #modelo MODELO-PDM
        T = modelo.T
        R = modelo.R
        gama = self._gama
        return sum(p * (R(s,a,sn) + gama * U[sn]) for (p,sn) in T(s,a))


    def politica(self, U, modelo):
        #U utilidade
        #modelo MODELO-PDM
        politicas = {}
        for s in modelo.S():
            politicas[s] = max(modelo.A(s), key= lambda a: self.util_accao(s,a,U,modelo))
        return politicas

    def resolver(self,modelo):
        #modelo MODELO-PDM
        U = self.utilidade(modelo)
        P = self.politica(U,modelo)
        return U,P
