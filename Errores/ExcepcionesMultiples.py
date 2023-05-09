'''while True:
    try:
        num1 = int(input("Ingresa un numero: "))
        resultado = 100 / num1
        print(resultado)
        break
    except ZeroDivisionError:
        print("No se puede Dividir entre cero")'''

'''while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        print("Tu edad es: ", edad)
        break
    except ValueError:
        print("Has colocado un valor erroneo")'''

while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        print("Tu edad es: ",edad)
        break
    except KeyboardInterrupt:
        print("\nHas cancelado la ejecucion")
        break