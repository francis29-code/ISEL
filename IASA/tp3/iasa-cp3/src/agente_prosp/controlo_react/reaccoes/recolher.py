from evitar_obst import EvitarObst
from explorar import Explorar
from aproximaralvo import AproximarAlvo
from hierarquia import Hierarquia
from contornar import Contornar

class Recolher(Hierarquia):

    def __init__(self):
        listaComportamentos = [Explorar(),EvitarObst(),AproximarAlvo(),Contornar()]
        Hierarquia.__init__(self, listaComportamentos)
