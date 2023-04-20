from math import sqrt

a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))
c = int(input("Ingrese el valor de c: "))

x1 = 0
x2 = 0

if ((b**2)-(4*a*c)) < 0:
    print("No se puede realizar porque no se puede sacar raiz a un numero negativo")
else:
    x1 = (-b + sqrt((b**2)-(4*a*c)))/(2*a)
    x2 = (-b - sqrt((b**2)-(4*a*c)))/(2*a)
    print("La soluciones: \nx1=",x1, "\nx2=",x2,)

