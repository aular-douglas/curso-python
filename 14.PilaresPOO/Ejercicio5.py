'''crear un progrma con tres clases Universidad, con atributos nombre (Donde se almacena el nombre de la
Universidad). Otra llamada Carrera, con los atributos especialidad (Endonde se guarda la especialidad de un
estudiante). Una yltima llamada estudiante, que tenga como atributo su nombre y edad. El programa debe
imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.'''

'''class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre


class Carrera:
    def __init__(self, especialidad):
        self.especialidad = especialidad


class Estudiante:
    def __init__(self, nombre, edad, universidad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.universidad = universidad
        self.carrera = carrera

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Especialidad: {self.carrera.especialidad}")
        print(f"Universidad: {self.universidad.nombre}")


if __name__ == '__main__':
    universidad = Universidad("Universidad Nacional")
    carrera = Carrera("Ingeniería de Sistemas")
    persona = Estudiante("Juan", 25, universidad, carrera)

    persona.mostrar_informacion()'''

class Universidad():
    def __init__(self,NombreUni):
        self.NombreUni = NombreUni
class Carrera():
    def carrera(self,especialidad):
        self.especialidad = especialidad
class Estudiante(Universidad,Carrera):
    def datos(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        print("Mi nombre es {},\nTengo {} años,\nMi especialidad es {}.\nEstudio en la universiddad {}".format(self.nombre , self.edad , self.especialidad , self.NombreUni))

persona = Estudiante("Don Bosco")
persona.carrera("Sistema")
persona.datos("carlos", 20)
