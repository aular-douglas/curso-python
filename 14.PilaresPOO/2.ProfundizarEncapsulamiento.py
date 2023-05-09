class A():
    def __init__(self):
        self._contador = 0
        self._contador = 0
    def incrementar(self):
        self._contador += 1
    def cuenta(self):
        return self._contador

a = A()

#print(a.cuenta)  # No se debe hacer de esta manera
#a.cuenta = 20
#print(a.cuenta)