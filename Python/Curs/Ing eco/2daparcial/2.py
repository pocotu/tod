#### Anualidad vencida
def Anualidad_vencida():
    def valor_presente():
        A = float(input("Ingrese el valor de la anualidad: "))
        i = float(input("Ingrese el valor de la tasa de interes: "))
        n = float(input("Ingrese el numero de periodos: "))
        sub_i = (i/100)/12
        sub_n = n*12
        vp = A*((1-(1+sub_i)**(-sub_n))/sub_i) # valor presente
        return vp
    def valor_futuro():
        while True:
            print("1. Hallar el valor valor futuro teniendo la anualidad")
            print("2. Hallar la anualidad teniendo el valor futuro")
            print("3. Regresar al menu principal")
            print("4. Salir")
            print("")
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                A = float(input("Ingrese el valor de la anualidad: "))
                i = float(input("Ingrese el valor de la tasa de interes: "))
                n = float(input("Ingrese el numero de periodos: "))
                sub_i = (i/100)/12
                sub_n = n*12
                vf = A*((((1+sub_i)**(sub_n))-1)/sub_i) # valor futuro
                print("El valor futuro es: ", vf)
                valor_futuro()
            elif opcion == 2:
                vf = float(input("Ingrese el valor futuro: "))
                i = float(input("Ingrese el valor de la tasa de interes: "))
                n = float(input("Ingrese el numero de periodos: "))
                sub_i = (i/100)/12
                sub_n = n*12
                A = (sub_i*vf)/((1+sub_i)**(sub_n)-1)
                print("La anualidad es: ", A)
                valor_futuro()
            elif opcion == 3:
                print("Regresando al menu principal")
                menu()
            elif opcion == 4:
                print("Saliendo del programa")
                break
            else:
                print("Opcion no valida")

    while True:
        print("1. Valor presente")
        print("2. Valor futuro")
        print("3. Regresar al menu principal")
        print("4. Salir")
        print("")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            # redondear el resultado a 2 decimales
            resultado = round(valor_presente(), 2)
            # imprimir en color rojo el resultado con el codigo de escape ANSI
            # \033[1;31;40m y cerrar el color con \033[0m
            print("\033[1;31m El valor presente es: ", resultado, "\033[0m")
        elif opcion == 2:
            valor_futuro()
        elif opcion == 3:
            print("Regresando al menu principal")
            menu()
        elif opcion == 4:
            # cerrar todo el programa
            print("Saliendo del programa")
            break
        else:
            print("Opcion no valida")
## 1478.80232

#### Anualidad anticipada
def Anualidad_anticipada():
    R = float(input("Ingrese el valor de la anualidad: "))
    i = float(input("Ingrese el valor de la tasa de interes: "))
    n = float(input("Ingrese el numero de periodos: "))
    p = int(input("Ingrese el tipo de periodo: "))
    sub_i = (i/p)/100
    sub_n = (n*p)
    vp = R*((((1+sub_i)**(sub_n))-1)/sub_i)*(1+sub_i)
    return vp

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

def menu():
    while True:
        print("1. Anualidad vencida")
        print("2. Anualidad anticipada")
        print("3. Anualidad diferida")
        print("4. Anualidad perpetua")
        print("5. Salir")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            Anualidad_vencida()
        elif opcion == 2:
            resultado = round(Anualidad_anticipada(), 2)
            print("El valor presente es: ", resultado)
        elif opcion == 3:
            resultado = round(Anualidad_diferida(), 2)
            print("El valor presente es: ", resultado)
        elif opcion == 4:
            resultado = round(Anualidad_perpetua(), 2)
            print("El valor presente es: ", resultado)
        elif opcion == 5:
            print("Programa finalizado")
            break
        else:
            print("Opcion no valida")

menu()