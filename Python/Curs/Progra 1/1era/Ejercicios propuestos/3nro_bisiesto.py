'''
Implementar una función que nos permita determinar si un número es Bisiesto o no
'''
def es_bisiesto(anio):
    if anio < 0:
        return "El año debe ser positivo"
    # Un año es bisiesto si es divisible por 4 y no es divisible por 100 o es divisible por 400
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def main():
    anio = int(input("Ingrese un año: "))
    while anio < 0:
        anio = int(input("Ingrese un año: "))
    print(es_bisiesto(anio))

main()