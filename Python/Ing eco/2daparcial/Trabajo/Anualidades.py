#### Anualidad vencida
def Anualidad_vencida():
    def valor_presente():
        while True:
            print("\n--- Valor presente de anualidad vencida ---")
            print("1. Hallar el valor presente teniendo la anualidad")
            print("2. Hallar la anualidad teniendo el valor presente")
            print("3. Regresar al menu anterior\n")
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                print("")
                A = float(input("Ingrese el valor de la anualidad: "))
                i = float(input("Ingrese el valor de la tasa de interes: "))
                print("## Convierta el periodo a meses si esta en años ##")
                n = float(input("Ingrese el numero de periodos: "))
                sub_i = (i/100)/12 # tasa de interes mensual y en decimal
                vp = A*((1-(1+sub_i)**(-n))/sub_i) # valor presente
                resultado = round(vp, 2)
                print("\n\033[1;31m El valor presente es: ", resultado, "\033[0m")
                valor_presente()
            elif opcion == 2:
                print("")
                vp = float(input("Ingrese el valor presente: "))
                i = float(input("Ingrese el valor de la tasa de interes: "))
                print("## Convierta el periodo a meses si esta en años ##")
                n = float(input("Ingrese el numero de periodos: "))
                sub_i = (i/100)/12 # tasa de interes mensual y en decimal
                A = (sub_i*vp)/(1-(1+sub_i)**(-n)) # anualidad
                resultado = round(A, 2)
                print("\n\033[1;31m La anualidad es: ", resultado, "\033[0m")
                valor_presente()
            elif opcion == 3:
                print("Regresando al menu anterior")
                break
            else:
                print("Opcion no valida")

    def valor_futuro():
        while True:
            print("\n--- Valor futuro de anualidad vencida ---")
            print("1. Hallar el valor valor futuro teniendo la anualidad")
            print("2. Hallar la anualidad teniendo el valor futuro")
            print("3. Regresar al menu anterior\n")
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                print("")
                A = float(input("Ingrese el valor de la anualidad: "))
                i = float(input("Ingrese el valor de la tasa de interes: "))
                print("## Convierta el periodo a meses si esta en años ##")
                n = float(input("Ingrese el numero de periodos: "))
                sub_i = (i/100)/12 # tasa de interes mensual y en decimal
                vf = A*((((1+sub_i)**(n))-1)/sub_i) # valor futuro
                resultado = round(vf, 2)
                print("\n\033[1;31m El valor futuro es: ", resultado, "\033[0m")
                valor_futuro()
            elif opcion == 2:
                print("")
                vf = float(input("Ingrese el valor futuro: "))
                i = float(input("Ingrese el valor de la tasa de interes: "))
                print("## Convierta el periodo a meses si esta en años ##")
                n = float(input("Ingrese el numero de periodos: "))
                sub_i = (i/100)/12 # tasa de interes mensual y en decimal
                A = (sub_i*vf)/((1+sub_i)**(n)-1) # anualidad
                resultado = round(A, 2)
                print("\n\033[1;31m La anualidad es: ", resultado, "\033[0m")
                valor_futuro()
            elif opcion == 3:
                print("Regresando al menu anterior")
                break
            else:
                print("Opcion no valida")

    while True:
        print("\n----- Anualidad vencida -----")
        print("1. Valor presente")
        print("2. Valor futuro")
        print("3. Regresar al menu anterior\n")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            valor_presente()
        elif opcion == 2:
            valor_futuro()
        elif opcion == 3:
            break
        else:
            print("Opcion no valida")

#### Anualidad anticipada
def Anualidad_anticipada():
    def valor_presente():
        while True:
            print("\n--- Valor presente de anualidad anticipada ---")
            print("1. Hallar el valor presente teniendo la anualidad")
            print("2. Hallar la anualidad teniendo el valor presente")
            print("3. Regresar al menu anterior\n")
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                print("")
                A = float(input("Ingrese el valor de la anualidad: "))
                i = float(input("Ingrese el valor de la tasa de interes: "))
                print("## Convierta el periodo a meses si esta en años ##")
                n = float(input("Ingrese el numero de periodos: "))
                sub_i = (i/100)/12 # tasa de interes mensual y en decimal
                vp = A*(1+((1-(1+sub_i)**(-(n-1)))/(sub_i)))
                resultado = round(vp, 2) # redondeo a 2 decimales
                print("\n\033[1;31m El valor presente es: ", resultado, "\033[0m")
                valor_presente()
            elif opcion == 2:
                print("")
                vp = float(input("Ingrese el valor presente: "))
                i = float(input("Ingrese el valor de la tasa de interes: "))
                print("## Convierta el periodo a meses si esta en años ##")
                n = float(input("Ingrese el numero de periodos: "))
                sub_i = (i/100)/12 # tasa de interes mensual y en decimal
                A = (vp/(1+((1-((1+sub_i)**(-(n-1))))/(sub_i))))
                resultado = round(A, 2)
                print("\n\033[1;31m La anualidad es: ", resultado, "\033[0m")
                valor_presente()
            elif opcion == 3:
                print("Regresando al menu anterior")
                break
            else:
                print("Opcion no valida")

    def valor_futuro():
        while True:
            print("\n--- Valor futuro de anualidad anticipada ---")
            print("1. Hallar el valor valor futuro teniendo la anualidad")
            print("2. Hallar la anualidad teniendo el valor futuro")
            print("3. Regresar al menu anterior\n")
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                print("")
                A = float(input("Ingrese el valor de la anualidad: "))
                i = float(input("Ingrese el valor de la tasa de interes: "))
                print("## Convierta el periodo a meses si esta en años ##")
                n = float(input("Ingrese el numero de periodos: "))
                sub_i = (i/100)/12
                vf = A*(((((1+sub_i)**(n+1))-1)/(sub_i))-1)
                resultado = round(vf, 2)
                print("\n\033[1;31m El valor futuro es: ", resultado, "\033[0m")
                valor_futuro()
            elif opcion == 2:
                print("")
                vf = float(input("Ingrese el valor futuro: "))
                i = float(input("Ingrese el valor de la tasa de interes: "))
                print("## Convierta el periodo a meses si esta en años ##")
                n = float(input("Ingrese el numero de periodos: "))
                sub_i = (i/100)/12
                A = vf/(((((1+sub_i)**(n+1))-1)/(sub_i))-1)
                resultado = round(A, 2)
                print("\n\033[1;31m La anualidad es: ", resultado, "\033[0m")
                valor_futuro()
            elif opcion == 3:
                print("Regresando al menu anterior")
                break
            else:
                print("Opcion no valida")

    while True:
        print("\n----- Anualidad anticipada -----")
        print("1. Valor presente")
        print("2. Valor futuro")
        print("3. Regresar al menu anterior\n")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            valor_presente()
        elif opcion == 2:
            valor_futuro()
        elif opcion == 3:
            break
        else:
            print("Opcion no valida")

#### Anualidad diferida
def Anualidad_diferida():
    R = float(input("Ingrese el valor de la Renta: "))
    i = float(input("Ingrese el valor de la tasa de interes: "))
    k = float(input("Ingrese el numero de plazo de anualidad: "))
    n = float(input("Ingrese el numero de periodos: "))
    vp = R*(1+i)**(-k)((1-(1+i)**(-n))/i)
    return vp

#### Anualidad perpetua
def Anualidad_perpetua():
    A = float(input("Ingrese el valor de la anualidad: "))
    i = float(input("Ingrese el valor de la tasa de interes: "))
    vp = A/i
    return vp

def Menu_anualidades():
    while True:
        print("\n1. Anualidad vencida")
        print("2. Anualidad anticipada")
        print("3. Anualidad diferida")
        print("4. Anualidad perpetua")
        print("5. Regresar al menu principal\n")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            Anualidad_vencida()
        elif opcion == 2:
            Anualidad_anticipada()
        elif opcion == 3:
            resultado = round(Anualidad_diferida(), 2)
            print("El valor presente es: ", resultado)
        elif opcion == 4:
            resultado = round(Anualidad_perpetua(), 2)
            print("El valor presente es: ", resultado)
        elif opcion == 5:
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    Menu_anualidades()