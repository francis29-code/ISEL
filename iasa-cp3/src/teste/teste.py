import sys
sys.path.insert(0,str(sys.path[0])+"\\..\\..\\src")
import psa
from psa.agente import Agente
from psa.accao import Avancar

path = str(sys.path[0])+"\\"

#_ protected
#__ privado
# nenhum publico
class AgenteTeste(Agente):
    def executar(self):
        self.actuador.actuar(Avancar())

psa.iniciar(path+'amb/amb1.das')
psa.executar(AgenteTeste())
