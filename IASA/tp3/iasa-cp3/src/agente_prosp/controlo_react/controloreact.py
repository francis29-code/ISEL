from controlo import Controlo

class ControloReact(Controlo):

    def __init__(self,Comportamento):
        #recolher - comportamento
        self._comportamento = Comportamento


    def processar(self, percepcao):
        #recolher tem varios comportamentos
        #evitar obstaculo
        #aproximar alvo
        #explorar
        accao = self._comportamento.activar(percepcao)

        return accao
