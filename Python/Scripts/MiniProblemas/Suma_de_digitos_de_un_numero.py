n = float(input("Ingrese un numero de mas de dos digitos: "))
suma = 0
nEntero = n % 1
if nEntero == 0:
    while 0 < n:
        suma = suma + n%10
        n = n//10
    print("La suma de los digitos es: ",suma)
else:
    print("Ingrese un numero entero")

