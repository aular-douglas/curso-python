'''Realizar un progrma que conste de una clase llamada Estudiante, que tenga como atributo
el nombre y la nota del estudiante. Definir los metodos para inicializar sus atributos, imprimirlos
y mostrar un mesaje con el resultado de la nota y si ha aprobado o no'''

class Estudiante():
    def __init__(self , nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print("Nombre: {} \nNota: {}".format(self.nombre , self.nota))
    def resultados(self):
        if self.nota < 7:
            print("Has REPROBADO!")
        else:
            print("Has APROBADO!")

estudiante1 = Estudiante("Daniel" , 10)
estudiante1.imprimir()
estudiante1.resultados()

estudiante2 = Estudiante("Karla" , 5)
estudiante2.imprimir()
estudiante2.resultados()