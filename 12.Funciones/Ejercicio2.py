# Escribir una funcion que reciba un numero entero positivo y devuelva su factorial

#3= 1 * 2 * 3 factorial de un numero

#Dos formas de realizar el ejercicio.

'''def factorial():
    num = int(input("Ingresa tu numero entero y positivo: "))
    if num > 0:
        factorial = 1
        for i in range(1 , num + 1):
            factorial = factorial * i
        print(factorial)
    else:
        print("El numero es negativo y no podemos proceder: ")
factorial()'''

def factorial():
    from math import factorial
    num = int(input("Ingresa tu numero entero y positivo: "))
    if num > 0:
        print(factorial(num))
    else:
        print("El numero es negativo y no podemos proceder: ")
factorial()
