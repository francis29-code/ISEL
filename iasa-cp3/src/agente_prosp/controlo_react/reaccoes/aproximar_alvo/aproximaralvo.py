from aproximar_alvo_dir import AproximarAlvoDIR
from prioridade import Prioridade

class AproximarAlvo(Prioridade):

    def __init__(self):
        listaDirecoes = [AproximarAlvoDIR('ESQ'),AproximarAlvoDIR('FRT'),AproximarAlvoDIR('DIR')]
        AproximarAlvoDIR.__init__(self,listaDirecoes)
