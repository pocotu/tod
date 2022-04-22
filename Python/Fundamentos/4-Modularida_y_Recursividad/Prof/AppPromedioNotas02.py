# Módulo para leer un número entero
def LeerNroEntero(Texto, Minimo, Maximo):
    Nro = int(input(Texto))
    while (Nro < Minimo) or (Nro > Maximo):
        print('Error. Número fuera de rango...')
        Nro = int(input(Texto))
    return Nro

# Ingresar las notas
Nota1 = LeerNroEntero('Ingrese la primera nota: ',0,20)
Nota2 = LeerNroEntero('Ingrese la segunda nota: ',0,20)
Nota3 = LeerNroEntero('Ingrese la tercera nota: ',0,20)

# Calcular el promedio
Promedio = (Nota1 + Nota2 + Nota3) / 3.0

# Mostrar promedio
print('El promedio es: ',Promedio)
