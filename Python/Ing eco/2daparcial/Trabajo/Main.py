from Anualidades import Menu_anualidades
from Gradientes import Menu_gradientes
from VAN import Menu_VAN
from TIR import Menu_TIR
from Payback import Menu_payback
from Punto_equilibrio import Menu_punto_equilibrio


def main():
    while True:
        print("1. Anualidades")
        print("2. Gradientes")
        print("3. VAN")
        print("4. TIR")
        print("5. Payback")
        print("6. Punto de equilibrio")
        print("7. Salir\n")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            Menu_anualidades()
        elif opcion == 2:
            Menu_gradientes()
        elif opcion == 3:
            Menu_VAN()
        elif opcion == 4:
            Menu_TIR()
        elif opcion == 5:
            Menu_payback()
        elif opcion == 6:
            Menu_punto_equilibrio()
        elif opcion == 7:
            break

main()
