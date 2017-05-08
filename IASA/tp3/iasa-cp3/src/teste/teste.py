
import sys
sys.path.append("../lib")
sys.path.append("../agente_prosp")
#######################ldkçdmlkclkcjkc kj
import psa
from agenteprospector import AgenteProspector
from controlo_react.controloreact import ControloReact
from controlo_react.reaccoes.recolher import Recolher as Comportamento



#-------------------------------------------------------
#activar
#Iniciar Plataforma
psa.iniciar("amb/amb1.das")

#Executar agente
psa.executar(AgenteProspector(ControloReact(Comportamento())))
