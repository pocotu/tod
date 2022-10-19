'''
Crear un modulo que calcule el interes compuesto, subtotal, total
y el total de intereses de un prestamo. El modulo debe recibir
'''

def interes_c():
    '''
    Calcula el interes compuesto de un prestamo
    '''
    monto = float(input("Ingrese el monto del prestamo: "))
    while monto < 0:
        print("El monto debe ser mayor a 0")
        monto = float(input("Ingrese el monto del prestamo: "))
    interes = float(input("Ingrese el interes anual: "))
    while interes < 0:
        print("El interes debe ser mayor a 0")
        interes = float(input("Ingrese el interes anual: "))
    tiempo = int(input("Ingrese el tiempo en meses: "))
    while tiempo < 0:
        print("El tiempo debe ser mayor a 0")
        tiempo = int(input("Ingrese el tiempo en meses: "))
    for i in range(1, tiempo+1):
        monto = monto * (1 + interes / 100)
        i = i + 1
    print("El monto total es: ", monto)
interes_c()