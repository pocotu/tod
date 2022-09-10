def sumar(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print()
        print('No se puede dividir entre 0')
        print()
        menu() 

def menu():
    print("""
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir
    """)
    opcion = input(input("Introduce la opción: "))

    while opcion != 5:
        if opcion == 1:
            print(sumar(a, b))
            break
        elif opcion == 2:
            print(resta(a, b))
            break
        elif opcion == 3:
            print(multiplicacion(a, b))
            break
        elif opcion == 4:
            print(division(a, b))
            break
        elif opcion == 5:
            break
        else:
            print()
            print("Opción incorrecta")
            print()
            opcion = int(input("Introduce la opción: "))

a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
menu()

