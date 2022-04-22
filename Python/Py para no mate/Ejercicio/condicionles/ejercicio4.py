saldo = 2000
print("1. Ingreso de dinero")
print("2. Retirar dinero")
print("3. Mostrar dinero")
print("4. Salir")

menu = int(input("Elija una opcion: "))
if menu == 1:
    ingresado = int(input("Dinero a ingresar: "))
    saldo += ingresado
    print(f"Nuevo saldo en la cuenta: {saldo}") 
elif menu == 2:
    retiro = int(input("Ingrese el monto a retirar: "))
    if retiro > saldo:
        print("Saldo insuficiente")
    else:
        saldo -= retiro
        print(f"Nuevo saldo: {saldo}")
elif menu == 3:
    print(f"Saldo disponible: {saldo}")
elif menu == 4:
    print("Retire su tarjerta")
else:
    print("Error entrada de datos")