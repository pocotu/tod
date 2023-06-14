
# Interes simple mensual
def interes_S_M(monto, interes, tiempo):
    interes_t =  monto * (interes / 100) * tiempo
    monto_t = monto + interes_t
    return monto_t

# Interes compuesto anual
def interes_C_M(monto, interes, tiempo):
    interes = interes
    for i in range(1, tiempo+1):
        monto = monto * (1 + interes / 100)
        print("Monto total del {} mes: {:.2f}".format(i, monto))
        i += 1
    print("")
    return monto

# Interes simple anual
def interes_S_A(monto, interes, tiempo):
    interes_M = interes / 12
    interes =  monto * (interes_M / 100) * tiempo
    monto = monto + interes
    return monto

# Interes compuesto mensual
def interes_C_A(monto, interes, tiempo):
    interes_M = interes / 12
    for i in range(1, tiempo+1):
        monto = monto * (1 + interes_M / 100)
        print("Monto total del {} mes: {:.2f}".format(i, monto))
        i += 1
    print("")
    return monto


def main():
    ## Menu ##
    print("")
    print("1. Interes simple mensua")
    print("2. Interes compuesto anual")
    print("3. Interes simple anual")
    print("4. Interes compuesto mensual")
    print("5. Salir")
    print("")
    opcion = int(input("Ingrese opcion: "))
    print("")
    while 0 < opcion < 5:
        monto = float(input("Ingrese el monto del prestamo: "))
        while monto <= 0:
            print("El monto debe ser mayor a 0")
            monto = float(input("Ingrese el monto del prestamo: "))
        interes = float(input("Ingrese el interes mensual: "))
        while interes <= 0:
            print("El interes debe ser mayor a 0")
            interes = float(input("Ingrese el interes mensual: "))
        tiempo = int(input("Ingrese el tiempo: "))
        while tiempo <= 0:
            print("El tiempo debe ser mayor a 0")
            tiempo = int(input("Ingrese el tiempo: "))
        print("=====================================")
        while tiempo < 0:
            print("El tiempo debe ser mayor a 0")
            tiempo = int(input("Ingrese el tiempo: "))
        if opcion == 1:
            monto_t = interes_S_M(monto, interes, tiempo)
            print("Interes simple mensual")
            print("El monto total es: {:.2f}".format(monto_t))
        elif opcion == 2:
            monto_t = interes_C_M(monto, interes, tiempo)
            print("Interes compuesto mensual")
            print("El monto total es: {:.2f}".format(monto_t))
        elif opcion == 3:
            monto_t = interes_S_A(monto, interes, tiempo)
            print("Interes simple anual")
            print("El monto total es: {:.2f}".format(monto_t))
        elif opcion == 4:
            monto_t = interes_C_A(monto, interes, tiempo)
            print("Interes compuesto anual")
            print("El monto total es: {:.2f}".format(monto_t))
        else:
            print("Fin del programa")

        print("=====================================")
        print("")
        print("1. Interes simple mensual")
        print("2. Interes compuesto anual")
        print("3. Interes simple anual")
        print("4. Interes compuesto mensual")
        print("5. Salir")
        print("")
        opcion = int(input("Ingrese opcion: "))
        print("")
    print("Fin del programa")
        
main()
