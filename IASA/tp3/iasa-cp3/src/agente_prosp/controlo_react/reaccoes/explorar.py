
from comportamento import Comportamento
from resposta import Resposta
import random
from psa.accao import Mover
from psa.actuador import FRT,ESQ,DIR


class Explorar(Comportamento):

    def activar(self, percepcao):
        #percepcao tem peso
        lista = [Mover(FRT),Mover(ESQ),Mover(DIR)]
        accao = random.choice(lista)
        return Resposta(accao)
