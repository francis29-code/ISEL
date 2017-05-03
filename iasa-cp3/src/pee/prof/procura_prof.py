# -*- coding: latin-1 -*-
"""
Mecanismo de procura em profundidade
@author: Luís Morgado
"""

from pee.mecproc.mecanismo_procura import MecanismoProcura
from pee.mecproc.mem.memoria_lifo import MemoriaLIFO

class ProcuraProf(MecanismoProcura):
    """Mecanismo de procura em profundidade"""
    def _iniciar_mem_procura(self):
        return MemoriaLIFO()

