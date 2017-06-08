from aprend_ref.memoriaprend import MemoriaAprend

class MemoriaEsparsa(MemoriaAprend):

    def __init__(self, valor_omissao=0):
        self._valor_omissao = valor_omissao
        self._dicionario ={}

    def actualizar(self,s,a,q):
        self._dicionario[(s,a)]=q

    def obter(self,s,a):
        return self._dicionario.get((s,a),self._valor_omissao)
