'''
funcion para calcular el interes compuesto, 
'''

# Interes simple mensual
def interes_S_M(monto, interes, tiempo):
    interes_t =  monto * (interes / 100) * tiempo
    monto_t = monto + interes_t
    return monto_t

# Interes compuesto mensual
def interes_C_M(monto, interes, tiempo):
    for i in range(1, tiempo+1):
        monto = monto * (1 + interes / 100)
        print("Monto total del {} mes es: {:.2f}".format(i, monto))
        i += 1
    print("")
    return monto


def main():
    ## Menu ##
    print("1. Interes simple mensual")
    print("2. Interes compuesto mensual")
    print("3. Salir")
    print("")
    opcion = int(input("Ingrese la opcion: "))
    while 1< opcion < 3:
        monto = float(input("Ingrese el monto del prestamo: "))
        while monto < 0:
            print("El monto debe ser mayor a 0")
            monto = float(input("Ingrese el monto del prestamo: "))
        interes = float(input("Ingrese el interes anual: "))
        while interes < 0:
            print("El interes debe ser mayor a 0")
            interes = float(input("Ingrese el interes anual: "))
        tiempo = int(input("Ingrese el tiempo en meses: "))
        print("=====================================")
        while tiempo < 0:
            print("El tiempo debe ser mayor a 0")
            tiempo = int(input("Ingrese el tiempo en meses: "))
        if opcion == 1:
            monto_t = interes_S_M(monto, interes, tiempo)
            print("El monto total es: {:.2f}".format(monto_t))
        elif opcion == 2:
            monto_t = interes_C_M(monto, interes, tiempo)
            print("El monto total es: {:.2f}".format(monto_t))
        else:
            print("Opcion incorrecta")
            print("Ingrese la opcion: ")
        print("")
        print("1. Interes simple mensual")
        print("2. Interes compuesto mensual")
        print("3. Salir")
        print("")
        opcion = int(input("Ingrese la opcion: "))
    print("Fin del programa")
        
    #monto = float(input("Ingrese el monto del prestamo: "))
    #while monto < 0:
    #    print("El monto debe ser mayor a 0")
    #    monto = float(input("Ingrese el monto del prestamo: "))
    #interes = float(input("Ingrese el interes anual: "))
    #while interes < 0:
    #    print("El interes debe ser mayor a 0")
    #    interes = float(input("Ingrese el interes anual: "))
    #tiempo = int(input("Ingrese el tiempo en meses: "))
    #while tiempo < 0:
    #    print("El tiempo debe ser mayor a 0")
    #    tiempo = int(input("Ingrese el tiempo en meses: "))
    #
    #print("=======================================")
    #print("El monto total a devolver es: {:.2f}".format(interes_C_M(monto, interes, tiempo)))
    #print("=======================================")
    #print("El monto total a devolver es: {:.2f}".format(interes_S_M(monto, interes, tiempo)))

main()