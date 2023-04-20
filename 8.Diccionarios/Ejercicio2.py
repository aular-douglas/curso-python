diccionario = {
    1 : "casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"
}

opcionJugador = int(input("Ingresa el numero del Jugador: "))

if opcionJugador in diccionario:
    print(diccionario[opcionJugador])
else:
    print("No es un numero dentro del diccionario")
