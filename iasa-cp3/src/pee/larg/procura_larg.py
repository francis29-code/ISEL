# -*- coding: latin-1 -*-
"""
Mecanismo de procura em largura
@author: Luís Morgado
"""

from pee.mecproc.mecanismo_procura import MecanismoProcura
from pee.mecproc.mem.memoria_fifo import MemoriaFIFO

class ProcuraLarg(MecanismoProcura):
    """Mecanismo de procura em largura"""
    def _iniciar_mem_procura(self):
        return MemoriaFIFO()
