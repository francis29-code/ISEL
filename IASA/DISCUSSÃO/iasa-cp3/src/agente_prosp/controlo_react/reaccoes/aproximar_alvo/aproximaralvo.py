from controlo_react.reaccoes.aproximar_alvo.aproximar_alvo_dir.aproximar_alvo_dir import AproximarAlvoDIR
from ecr.prioridade import Prioridade
from psa.actuador import FRT,ESQ,DIR

class AproximarAlvo(Prioridade):

    def __init__(self):
        listaDirecoes = [AproximarAlvoDIR(ESQ),AproximarAlvoDIR(FRT),AproximarAlvoDIR(DIR)]
        Prioridade.__init__(self,listaDirecoes)
