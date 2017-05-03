import sys
import Controlo

class ControloReact(Controlo):

    def __init__(self):
        #recolher - comportamento
        self._reaccao = Recolher()

    def processar(self, Percepcao):
        #recolher tem varios comportamentos
        #evitar obstaculo
        #aproximar alvo
        #explorar
        accao = self._reaccao.activar(percepcao)

        return accao
