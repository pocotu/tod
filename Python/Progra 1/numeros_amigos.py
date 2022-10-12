from re import X


a = int(input("Ingresa un numero: "))
b = int(input("Ingresa un numero: "))

x = 1
suma = 0
while x < a:
    if a % x == 0:
        suma = suma + x
    x = x + 1
if suma == b:
    print("Los numeros son amigos")
else:
    print("Los numeros no son amigos")



