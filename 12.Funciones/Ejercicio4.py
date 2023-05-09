'''Escribir una funcion que calcule el valor total de una factura tras aplicarle el IVA. la funcion debe escribir la cantidad sin IVA
y el porcentaje de IVA a aplicar, y devolver el total de la factura. si se invica la funcion sin
pasarle el porcentaje de Iva, deberia aplicar un 21% '''

def total():
    monto = float(input("Ingresa el valor del producto que estas pagando: "))
    iva = int(input("Ingresa el valor del IVA: "))

    if iva != 0:
        if iva > 0:
            TotalPagar = ((monto * iva) / 100) + monto
            return TotalPagar
        else:
            return "El montode IVA es negativo. No podemos avanzar"
    else:
            TotalPagar = (monto * 0.21) + monto
            return TotalPagar
print("El total de su monto es: ", total())