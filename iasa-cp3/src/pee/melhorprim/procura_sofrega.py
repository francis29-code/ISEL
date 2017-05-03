# -*- coding: utf-8 -*-
"""
Mecanismo de procura sôfrega
@author: Luís Morgado
"""

from procura_melhor_prim import ProcuraMelhorPrim

#_______________________________________________________________________________

class ProcuraSofrega(ProcuraMelhorPrim):
    """Mecanismo de procura sôfrega, critério de ordem: f = h"""

    def f(self, no):
        return self.problema.heuristica(no.estado)
