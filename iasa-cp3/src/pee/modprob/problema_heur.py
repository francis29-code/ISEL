# -*- coding: latin-1 -*-
"""
Definição de problema com heurística
@author: Luís Morgado
"""

from .problema import Problema

#_______________________________________________________________________________

class ProblemaHeur(Problema):
    """Definição geral de um problema com heurística"""
        
    def heuristica(self, estado):
        """Obter heurística de um estado
        @param estado: Estado a avaliar
        @return: Heurística do estado"""
        raise NotImplementedError  