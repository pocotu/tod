#comparando si hay coincidencia
palabra = input("Nombre 1: ")
palabra2 = input("Nombre 2: ")

if palabra[0] == palabra2[0] or palabra[-1] == palabra2[-1]:
    print(" si hay coincidencia")

else:
    print("No hay coincidencia")
