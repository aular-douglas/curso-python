#imprimir por pantalla los numeros del 1 al 10, luego pedir al usuario dos
# numeros y mostrar el rango de numeros entre ambas cifras

for i in range(1 , 11):
    print(i)

num1 = int(input("Ingresa la primera cifra: "))
num2 = int(input("Ingresa la segunda cifra: "))

for i in range(num1 , num2 + 1):
    print(i)