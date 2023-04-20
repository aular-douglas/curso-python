#Pedir al usuario que ingrese 2 numeros, despues se debe mostrar el rango de esos dos numeros
#pero solo imprimiendo los numeros que sean impares

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

for i in range(num1 , num2 + 1):
    if i % 2 == 0:
        continue
    print(i)