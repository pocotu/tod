### Invertir el orden de los digitos de un numero de tres digitos ###

# Leer un numero entero de tres digitos #
numero = int(input("Ingrese un numero entero de 3 digitos: "))

# Invertir el numero #
numeroInvertido = 0

numeroInvertido = numeroInvertido * 10 + numero % 10
numero = numero // 10

numeroInvertido = numeroInvertido * 10 + numero % 10
numero = numero // 10

numeroInvertido = numeroInvertido * 10 + numero % 10


# Escribir el numero con el orden de los digitos invertidos
print("Numero invertido es: ",numeroInvertido)
