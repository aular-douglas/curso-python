class animales():
    def habla(self):
        print("Yo soy un Animal")
    def descripcion(self):
        print("Yo soy una {}" .format(self.animal))

class Perro(animales):
    pass

class Abeja(animales):
    def __init__(self , animal):
        self.animal = animal
    pass

animal = animales()
animal.habla()

perro = Perro()
perro.habla()

Abeja = Abeja("Abeja")
Abeja.descripcion()