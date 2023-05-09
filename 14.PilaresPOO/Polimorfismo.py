class Animales():
    def __init__(self , mensaje):
        self.mensaje = mensaje
    def hablar(self):
        print(self.mensaje)
class Perro(Animales):
    def hablar(self):
        print("Yo hago Guao!")
class Pez(Animales):
    def hablar(self):
        print("Yo no hablo")

perro = Perro("Guao!")
perro.hablar()

animal = Animales ("Miau!")
animal.hablar()

pez = Pez("Nada")
pez.hablar()