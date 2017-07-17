import sys
sys.path.append("../lib")
sys.path.append("../agente_prosp")

import psa
from agenteprospector import AgenteProspector
from controlo_delib.controlodelib import ControloDelib
from plan.plan_pdm.planpdm import PlanPDM as Planeador

psa.iniciar("amb/amb2.das")

planeador = Planeador()
controlo = ControloDelib(planeador)
agente = AgenteProspector(controlo)

psa.executar(agente)
