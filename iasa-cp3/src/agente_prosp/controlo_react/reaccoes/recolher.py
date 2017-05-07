from evitar_obst import EvitarObst
from explorar import Explorar
from aproximaralvo import AproximarAlvo
from hierarquia import Hierarquia

class Recolher(Hierarquia):

    def __init__(self):
        listaComportamentos = [AproximarAlvo(),EvitarObst(),Explorar()]
        Hierarquia.__init__(self, listaComportamentos)
