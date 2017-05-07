import sys
from psa.agente import Agente

class AgenteProspector(Agente):

    def __init__(self, controlo):
        self._controlo = controlo

    def executar(self):
        percepcao = self.percepcionar()
        accao = self.processar(percepcao)
        self.actuar(accao)

        print "AgenteP Executar - void"

    def _percepcionar(self):
        print "AgenteP percepcionar - void"
        return self.sensor_multiplo.detectar()

    def _processar(self,percepcao):
        print "AgenteP processar - void"
        return self._controlo.processar(percepcao)

    def _actuar(self,accao):
        print "AgenteP actuar - void"
        if accao is not None:
            self.actuador.actuar(accao)
