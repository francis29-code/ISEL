import sys
sys.path.append("../lib/ecr")
sys.path.append("../agente_prosp")
sys.path.append("../agente_prosp/controlo_react")
sys.path.append("../agente_prosp/controlo_react/reaccoes")
sys.path.append("../agente_prosp/controlo_react/reaccoes/aproximar_alvo")
sys.path.append("../agente_prosp/controlo_react/reaccoes/aproximar_alvo/aproximar_alvo_dir")
import psa

from agenteprospector import AgenteProspector
from controloreact import ControloReact
from recolher import Recolher as Comportamento

#-------------------------------------------------------
#activar
#Iniciar Plataforma
psa.iniciar("amb/amb1.das")

#Executar agente
psa.executar(AgenteProspector(ControloReact(Comportamento())))
