#bucle while
import math
numero = int(input("Escribe un numero: "))

while numero<0:
    print("Por favor ingresa un numero positivo: ")
    numero = int(input("Vuelve a ingresar un numero positivo: "))

print(f"El resultado de la raiz cuadrada es: {math.sqrt(numero):.2f}")