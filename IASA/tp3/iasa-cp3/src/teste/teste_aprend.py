import sys
sys.path.append("../lib")
sys.path.append("../agente_prosp")

import psa
from agenteprospector import AgenteProspector
from controlo_aprend.controloaprendref import ControloAprendRef as Controlo

psa.iniciar("amb/amb3.das")

agente = AgenteProspector(Controlo())

psa.executar(agente)
