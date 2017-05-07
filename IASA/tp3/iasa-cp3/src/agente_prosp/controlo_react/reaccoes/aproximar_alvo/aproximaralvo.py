from aproximar_alvo_dir import AproximarAlvoDIR
from prioridade import Prioridade
from psa.actuador import FRT,ESQ,DIR

class AproximarAlvo(Prioridade):

    def __init__(self):
        listaDirecoes = [AproximarAlvoDIR(ESQ),AproximarAlvoDIR(FRT),AproximarAlvoDIR(DIR)]
        Prioridade.__init__(self,listaDirecoes)
