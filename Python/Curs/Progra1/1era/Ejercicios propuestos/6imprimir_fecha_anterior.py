'''
Implementar una función diaAnterior, que reciba una fecha representada a través 
de tres enteros d, m y a y retorne fecha anterior. (Verificar que la fecha ingresada 
sea válida utilizando la función implementada en el ejercicio 4).
'''
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

# crear una funcion que reciba una fecha y retorne la fecha anterior usando la funcion validar_fecha
def diaAnterior(d, m, a):
    # Si es el primer dia del año y el mes es enero devolvemos el ultimo dia del
    # año anterior
    if m == 1 and d == 1:
        return "31/12/" + str(a - 1)
    # Si es el primer dia del mes y el mes es febrero devolvemos el ultimo dia de
    if m == 3 and d == 1:
        # Si el año es bisiesto devolvemos el ultimo dia de febrero
        if a % 4 == 0:
            return "29/02/" + str(a)
        # Si no es bisiesto devolvemos el ultimo dia de febrero
        else:
            return "28/02/" + str(a)
    # Si es el primer dia del mes y el mes es mayo devolvemos el ultimo dia de
    if m == 5 and d == 1:
        return "30/04/" + str(a)
    if m == 7 and d == 1:
        return "30/06/" + str(a)
    if m == 8 and d == 1:
        return "31/07/" + str(a)
    if m == 10 and d == 1:
        return "30/09/" + str(a)
    if m == 12 and d == 1:
        return "30/11/" + str(a)
    # Si es el primer dia del mes devolvemos el ultimo dia del mes anterior
    if d == 1:
        return "30/" + str(m - 1) + "/" + str(a)
    return str(d - 1) + "/" + str(m) + "/" + str(a)

def main():
    d = int(input("Ingrese el dia: "))
    while d < 1 or d > 31:
        d = int(input("Ingrese el dia: "))
    m = int(input("Ingrese el mes: "))
    while m < 1 or m > 12:
        m = int(input("Ingrese el mes: "))
    a = int(input("Ingrese el año: "))
    while a < 1:
        a = int(input("Ingrese el año: "))
    print(diaAnterior(d, m, a))

main()