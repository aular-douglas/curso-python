'''Escribir una funcion que reciba una muestra de numeros en una tupla y devuelva su medida'''

def medida(*tupla):
    print(len(tupla))     #El len nuestra la cantidad de digitos que contiene la tupla
    for i in tupla:
        print(i)
    return len(tupla)
print(medida(2 , 3 , 4 , 10 , 20))