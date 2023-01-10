#### Anualidad vencida
def Anualidad_vencida():
    R = float(input("Ingrese el valor de la anualidad: "))
    i = float(input("Ingrese el valor de la tasa de interes: "))
    n = float(input("Ingrese el numero de periodos: "))
    vp = R*((1-(1+i)**(-n)))/i
    return vp

def Anualidad_anticipada():
    R = float(input("Ingrese el valor de la anualidad: "))
    i = float(input("Ingrese el valor de la tasa de interes: "))
    n = float(input("Ingrese el numero de periodos: "))
    p = int(input("Ingrese el tipo de periodo: "))
    sub_i = (i/p)/100
    sub_n = (n*p)
    vp = R*((((1+sub_i)**(sub_n))-1)/sub_i)*(1+sub_i)
    return vp

def Anualidad_diferida():
    R = float(input("Ingrese el valor de la Renta: "))
    i = float(input("Ingrese el valor de la tasa de interes: "))
    k = float(input("Ingrese el numero de plazo de anualidad: "))
    n = float(input("Ingrese el numero de periodos: "))
    vp = R*(1+i)**(-k)((1-(1+i)**(-n))/i)
    return vp

def Anualidad_perpetua():
    A = float(input("Ingrese el valor de la anualidad: "))
    i = float(input("Ingrese el valor de la tasa de interes: "))
    vp = A/i
    return vp

def Menu():
    print("1. Anualidad vencida")
    print("2. Anualidad anticipada")
    print("3. Anualidad diferida")
    print("4. Anualidad perpetua")
    print("5. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        print(Anualidad_vencida())
    elif opcion == 2:
        print(Anualidad_anticipada())
        #Anualidad_anticipada()
    elif opcion == 3:
        Anualidad_diferida()
    elif opcion == 4:
        Anualidad_perpetua()

Menu()

