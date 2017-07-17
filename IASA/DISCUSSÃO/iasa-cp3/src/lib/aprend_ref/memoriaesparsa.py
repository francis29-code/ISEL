from aprend_ref.memoriaprend import MemoriAprend

class MemoriaEsparsa(MemoriAprend):

    def __init__(self, valor_omissao=0.0):
        self._valor_omissao = valor_omissao
        self.memoria ={}

    def actualizar(self,s,a,q):
        self.memoria[(s,a)]=q

    def obter(self,s,a):
        return self.memoria.get((s,a),self._valor_omissao)
