# -*- coding: utf-8 -*-
"""
Mecanismo de procura A*
@author: Luís Morgado
"""

from procura_melhor_prim import ProcuraMelhorPrim

#_______________________________________________________________________________

class ProcuraAA(ProcuraMelhorPrim):
    """Mecanismo de procura A*, critério de ordem: f = g + h,
    com heurística admissível"""

    def f(self, no):
        return no.custo + self.problema.heuristica(no.estado)
