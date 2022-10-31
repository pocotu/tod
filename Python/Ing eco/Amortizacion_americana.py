'''
Crear un programa para el sistema de amortizacion americana.

monto = 10000
tiempo meses = 6
interes anual = 30%

total a devolver = 11500
'''

def interes(monto, interes):
    interes = interes / 100
    interes = interes / 12
    interes = 1 + interes
    interes = interes ** tiempo
    total = monto * interes
    return total

def main():
    monto = float(input("Ingrese el monto: "))
    tiempo = int(input("Ingrese el tiempo en meses: "))
    interes = int(input("Ingrese el interes anual: "))
    total = interes(monto, interes)
    print("El total a devolver es: %.2f" % total)

main()