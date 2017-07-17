
class Planeador:

    def planear(self,modeloPlan,estadoInicial,listaObjectivos):
        #void
        raise NotImplementedError

    def obter_accao(self,estado):
        #retorn um operador
        raise NotImplementedError

    def plano_pendente(self):
        #retorn booleano
        raise NotImplementedError

    def terminar_plano(self):
        #retorn void
        raise NotImplementedError
