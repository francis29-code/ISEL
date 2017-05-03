# -*- coding: latin-1 -*-
"""
Defini��o de problema com heur�stica
@author: Lu�s Morgado
"""

from .problema import Problema

#_______________________________________________________________________________

class ProblemaHeur(Problema):
    """Defini��o geral de um problema com heur�stica"""
        
    def heuristica(self, estado):
        """Obter heur�stica de um estado
        @param estado: Estado a avaliar
        @return: Heur�stica do estado"""
        raise NotImplementedError  