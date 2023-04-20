diccionario = {"Guatemala": "Ciudad de Guatemala", "Honduras": "Tegucigalpa", "Nicaragua":
"Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia":
"Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais = input("Ingrese un pais para conocer su capital: ")
letra = pais.capitalize() in diccionario

if letra == True:
    print(diccionario[pais.capitalize()])
else:
    print("El pais no se encuentra en el diccionario")