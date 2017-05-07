from Prioridade import Prioridade
from aproximar_alvo_dir import AproximarAlvoDir

class AproximarAlvo(Prioridade):
    
    def __init__(self):
        super(AproximarAlvo, self).__init__([AproximarAlvoDir("ESQ"),
                                             AproximarAlvoDir("FRT"),
                                             AproximarAlvoDir("DIR")])
