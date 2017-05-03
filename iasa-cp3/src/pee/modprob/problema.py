# -*- coding: latin-1 -*-
"""
Definição de problema de procura
@author: Luís Morgado
"""
    
#_______________________________________________________________________________

class Problema(object):
    """Definição geral de um problema de procura"""
    
    def __init__(self, estado_inicial, operadores):
        """Iniciar problema
        @param estado_inicial: Estado inicial do problema
        @param operadores: Operadores definidos para o problema"""
        self._estado_inicial = estado_inicial
        self._operadores = operadores

    @property
    def estado_inicial(self):
        """Obter estado inicial do problema"""
        return self._estado_inicial
        
    @property
    def operadores(self):
        """Obter operadores definidos para o problema"""
        return self._operadores

    def objectivo(self, estado):
        """Verificar se um estado satisfaz o objectivo
        @param estado: Estado a verificar
        @return: Indicação se estado satisfaz objectivo (sim/não)"""
        raise NotImplementedError
  
