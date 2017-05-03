# -*- coding: utf-8 -*-
"""
Mecanismo de procura de custo uniforme
@author: Luís Morgado
"""

from procura_melhor_prim import ProcuraMelhorPrim

#_______________________________________________________________________________

class ProcuraCustoUnif(ProcuraMelhorPrim):
    """Mecanismo de procura de custo uniforme, critério de ordem: f = g"""
    
    def f(self, no):
        return no.custo
