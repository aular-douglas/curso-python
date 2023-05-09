'''Crear una clase llamada Marino(), con un metodo que sea hablar, en donde muestre un mesaje que diga
 "Hola...". Luego, crear una clase pulpo() que Herede Marino, pero modificar el menesaje de hablar por
 "Soy un Pulpo. Por ultimo, crear una clase Foca(), heredada de Marino, pero que tenga un atributo nuevo
 llamado mensaje y que muestre ese mensaje como parametro.'''

'''class Marino:
    def hablar(self):
        print("Hola...")
class Pulpo(Marino):
    def hablar(self):
        print("Soy un Pulpo.")
class Foca(Marino):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)

marino = Marino()
pulpo = Pulpo()
foca = Foca("¡Hola, soy una foca!")

marino.hablar()  # Output: "Hola..."
pulpo.hablar()   # Output: "Soy un Pulpo."
foca.hablar()    # Output: "¡Hola, soy una foca!"'''

class Marino():
    def hablar(self):
        print("Hola...")
class Pulpo(Marino):
    def hablar(self):
        print("Soy un pulpo")
class Foca(Marino):
    def hablar(self,mensaje):
        self.mensaje = mensaje
        print(self.mensaje)

marino = Marino()
marino.hablar()

pulpo = Pulpo()
pulpo.hablar()

foca = Foca()
foca.hablar("Hola, soy una foca")


