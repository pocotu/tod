'''
Implementar una función diaPosterior, que reciba una fecha representada a través 
de tres enteros d, m y a y retorne fecha posterior. (Verificar que la fecha ingresada 
sea válida utilizando la función implementada en el ejercicio 4)
'''

def diaPosterior(d, m, a):
    # Si es el ultimo dia del año y el mes es diciembre devolvemos el primer dia del
    if m == 12 and d == 31:
        return "01/01/" + str(a + 1)
    # Si es el ultimo dia del mes y el mes es febrero devolvemos el primer dia de
    if m == 2 and d == 28:
        if a % 4 == 0:
            return "29/02/" + str(a)
        else:
            return "01/03/" + str(a)
    # Si es el ultimo dia del mes y el mes es abril devolvemos el primer dia de
    if m == 4 and d == 30:
        return "01/05/" + str(a)
    if m == 6 and d == 30:
        return "01/07/" + str(a)
    if m == 9 and d == 30:
        return "01/10/" + str(a)
    if m == 11 and d == 30:
        return "01/12/" + str(a)
    # Si es el ultimo dia del mes devolvemos el primer dia del mes siguiente
    if d == 31:
        return "01/" + str(m + 1) + "/" + str(a)
    return str(d + 1) + "/" + str(m) + "/" + str(a)

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
    print(diaPosterior(d, m, a))

main()