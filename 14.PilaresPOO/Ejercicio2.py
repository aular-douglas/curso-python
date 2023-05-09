'''Realizar un programa en el cual se declaren dos valores enteros por taclado utilizando
el metodo __init__. Calcular despues la suma, resta, multiplicacion y division. Utilizar un
metodo para cada una e imprimir los resultados obtenidos. Llmar a la clase calculadora'''

class Calculadora:
    def __init__(self):
        self.num1 = int(input("Ingrese el primer valor: "))
        self.num2 = int(input("Ingrese el segundo valor: "))

    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def multiplicacion(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 == 0:
            return "Error: no se puede dividir por cero"
        else:
            return self.num1 / self.num2

# Creamos una instancia de la clase Calculadora
calculadora = Calculadora()100

# Llamamos a los métodos de la clase para realizar las operaciones
print("La suma es:", calculadora.suma())
print("La resta es:", calculadora.resta())
print("La multiplicación es:", calculadora.multiplicacion())
print("La división es:", calculadora.division())