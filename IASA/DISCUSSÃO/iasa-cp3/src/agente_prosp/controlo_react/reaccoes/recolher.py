from controlo_react.reaccoes.evitar_obst import EvitarObst
from controlo_react.reaccoes.explorar import Explorar
from controlo_react.reaccoes.aproximar_alvo.aproximaralvo import AproximarAlvo
from ecr.hierarquia import Hierarquia
from controlo_react.reaccoes.contornar import Contornar

class Recolher(Hierarquia):

    def __init__(self):
        listaComportamentos = [AproximarAlvo(),EvitarObst(),Explorar()]
        Hierarquia.__init__(self, listaComportamentos)
