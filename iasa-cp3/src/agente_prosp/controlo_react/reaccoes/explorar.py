
from comportamento import Comportamento
from resposta import Resposta

class Explorar(Comportamento):

    def activar(self, percepcao):
        #percepcao tem peso
        accao = choice([Mover('ESQ'),Mover('DIR'),Mover('FRT')])
        return Resposta(accao)
