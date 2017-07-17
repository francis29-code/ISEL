'''
teste_react.py

import sys
sys.path.append("../lib/ecr")
sys.path.append("../agente_prosp")

import psa

from agente prospector import AgenteProspector

from controlo_react.controlo_react import ControloReact
from controlo_react.reaccoes import Recolher as Comportamento

psa.iniciar("amb/amb1.das")

psa.executar(AgenteProspector(ControloReact(Comportamento())))

'''


import sys
sys.path.append("../lib/ecr")
sys.path.append("../agente_prosp")

import psa

from psa.agente import Agente

from psa.actuador import ESQ
from psa.actuador import FRT
from psa.actuador import DIR

from psa.accao import Rodar
from psa.accao import Mover
from psa.accao import Avancar




class AgenteTeste(Agente):
    def executar(self):
        self.actuador.actuar(Avancar())


psa.iniciar("amb/amb1.das")

psa.executar(AgenteTeste())
