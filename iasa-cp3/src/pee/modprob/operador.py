# -*- coding: latin-1 -*-
"""
Interface Operador
@author: Luís Morgado
"""

#_______________________________________________________________________________

class Operador:
    """Interface Operador"""
        
    def aplicar(self, estado):
        """Aplicar operador a estado gerando um novo estado
	@param estado: Estado a aplicar operador
        @return: Novo estado"""
        raise NotImplementedError

    def custo(self, estado, estado_suc):
        """Custo de aplicação do operador
        @param estado: Estado antecessor
	@param estado_suc: Estado sucessor
	@return: Custo de aplicação do operador"""
        raise NotImplementedError
