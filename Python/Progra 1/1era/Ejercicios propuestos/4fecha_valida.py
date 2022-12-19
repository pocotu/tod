'''
Implementar una funcion para determinar si una fecha es válida. La fecha es 
representada por tres números enteros dia, mes y anio. Luego, escriba un modulo
que solicite al usuario una fecha e indique por pantalla si la misma es válida o no.
'''
# Lista con meses, dias y anios bisiestos
def validar_fecha(dia, mes, año):
    # anio normal
    A_N = [31,28,31,30,31,30,31,31,30,31,30,31]
    # anio bisiesto
    A_B = [31,29,31,30,31,30,31,31,30,31,30,31]
    # Si el año es bisiesto
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        if dia > A_B[mes-1]:
            return "La fecha no es valida"
        else:
            return "La fecha es valida"
    # Si el año no es bisiesto
    else:
        if dia > A_N[mes-1]:
            return "La fecha no es valida"
        else:
            return "La fecha es valida"


def main():
    dia = int(input("Ingrese el dia: "))
    while dia < 1 or dia > 31:
        print("El dia debe ser entre 1 y 31")
        dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    while mes < 1 or mes > 12:
        print("El mes debe ser entre 1 y 12")
        mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el anio: "))
    while anio < 0:
        print("El anio debe ser positivo")
        anio = int(input("Ingrese el anio: "))
    print(validar_fecha(dia, mes, anio))

main()