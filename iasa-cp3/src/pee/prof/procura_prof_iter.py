# -*- coding: latin-1 -*-
"""
Procura em profundidade iterativa
@author: Lu�s Morgado
"""

from procura_prof import ProcuraProf

class ProcuraProfIter(ProcuraProf):
    """Procura em profundidade iterativa"""
    
    def resolver(self, problema, prof_max=1000, inc_prof=10):
        """Procurar solu��o com incremento de profundidade indicado
        @param problema: Problema associado
        @param prof_max: Profundidade m�xima da procura
        @param inc_prof: Incremento de profundidade por cada itera��o
        @return: Solu��o"""
        for prof in range(inc_prof, prof_max + 1, inc_prof):
            solucao = ProcuraProf.resolver(self, problema, prof)
            if solucao:
                return solucao
