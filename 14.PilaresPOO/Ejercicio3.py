'''Crear una clase Fabrica que tenga los atributos de llantas, color, precio; luego crear dos
clases mas que hereden de fabrica, las cuales son moto y carro. crear metods que muestren la cantidad de llantas,
color y precio de ambos transportes. por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos
de cada uno.'''

'''class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def mostrar_llantas(self):
        print(f"Cantidad de llantas: {self.llantas}")

    def mostrar_color(self):
        print(f"Color: {self.color}")

    def mostrar_precio(self):
        print(f"Precio: {self.precio}")


class Moto(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)


class Carro(Fabrica):
    def __init__(self, llantas, color, precio):
        super().__init__(llantas, color, precio)


if __name__ == '__main__':
    moto_1 = Moto(2, "Rojo", 5000)
    carro_1 = Carro(4, "Negro", 15000)

    print("Moto 1:")
    moto_1.mostrar_llantas()
    moto_1.mostrar_color()
    moto_1.mostrar_precio()

    print("\nCarro 1:")
    carro_1.mostrar_llantas()
    carro_1.mostrar_color()
    carro_1.mostrar_precio()'''


class Fabrica():
    def __init__(self , llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio
class Carro(Fabrica):
    def datos(self):
        print("\nLa cantidad de llantas del carro es de:",self.llantas)
        print("el color del carro es:",self.color)
        print("El precio del carro es de: $",self.precio)
class Moto(Fabrica):
    def datos(self):
        print("La cantidad de llantas de la moto es de:",self.llantas)
        print("El color de la moto es:",self.color)
        print("El precio de la moto es de: $",self.precio)

moto = Moto(2 , "Negro" , 4000)
moto.datos()

carro = Carro(4, "Blanco" , 5000)
carro.datos()

