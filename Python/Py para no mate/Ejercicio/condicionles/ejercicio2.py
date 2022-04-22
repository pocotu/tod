#determinar que numero es mayor
numero = int(input("Ingrese un mumero: "))
numero2 = int(input("Ingrese un segundo mumero: "))
numero3 = int(input("Ingrese un tercer mumero: "))

if numero >= numero2 and numero >= numero3:
    print(f"El {numero} es mayor que todos")
elif numero2 >= numero and numero2>= numero3:
    print(f"El {numero2} es mayor que todos")
elif numero3 >= numero and numero3 >= numero2:
    print(f"El {numero3} es el mayor")
