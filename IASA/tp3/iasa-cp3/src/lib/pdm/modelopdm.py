
class ModeloPDM:

    def S(self):
        raise NotImplementedError

    def A(self, estado):
        raise NotImplementedError

    def T(self, s, a):
        #transicao -> tuplo(accao, estado_sucessor)
        raise NotImplementedError

    def R(self, s, a, sn):
        raise NotImplementedError
