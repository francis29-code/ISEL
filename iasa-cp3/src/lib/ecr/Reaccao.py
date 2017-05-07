from comportamento import Comportamento

class Reaccao(Comportamento):

    def activar(self, percepcao):
        estimulo = self.__detetar_estimulo(percepcao)
        if estimulo is not None and estimulo is not False:
            resposta = self.__gerar_resposta(estimulo)
            return resposta

    def __gerar_resposta(self, estimulo):
        raise NotImplementedError

    def __detetar_estimulo(self, percepcao):
        raise NotImplementedError
