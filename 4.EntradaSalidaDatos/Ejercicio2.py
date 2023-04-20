practica1 = float(input("Ingrese el valor de la practica 1:"))
practica2 = float(input("ingrese el valor de la practica 2:"))
practica3 = float(input("ingrese el valor de la practica 3:"))
ExamenParcial = float(input("ingrese el valor del examen parcial:"))
ExamenFinal = float(input("ingrese el valor del examen final:"))

PromedioPractica = (practica1 + practica2 + practica1)/3
PromedioFinal  = (PromedioPractica + 2*ExamenParcial + 3*ExamenFinal)/6

print("El promedio de practica del estudiante es de:\n" , PromedioPractica, "\n y el promedio final es de:\n ",PromedioFinal)