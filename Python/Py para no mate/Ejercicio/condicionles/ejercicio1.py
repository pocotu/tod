#ver si dos numeros son pares
numero = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

if (numero % 2 == 0) and (numero2 % 2 == 0):
    print("Los dos numeros son pares")

elif numero  % 2 == 0 and (numero2 % 2 != 0):
    print(f"Solo {numero} es par")

elif (numero % 2 != 0) and  numero2 % 2 == 0:
    print(f"Solo {numero2} es par")
else:
    print("Los dos numero no son pares")
