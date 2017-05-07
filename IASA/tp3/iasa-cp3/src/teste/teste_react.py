import sys
sys.path.append("../lib/ecr")
sys.path.append("../agente_prosp")
sys.path.append("../agente_prosp/controlo_react")
sys.path.append("../agente_prosp/controlo_react/reaccoes")
sys.path.append("../agente_prosp/controlo_react/reaccoes/aproximar_alvo")

import psa

from AgenteProspector import AgenteProspector
from ControloReact import ControloReact
from recolher import Recolher as Comportamento

psa.iniciar("amb/amb1.das")

psa.executar(AgenteProspector(ControloReact(Comportamento())))
