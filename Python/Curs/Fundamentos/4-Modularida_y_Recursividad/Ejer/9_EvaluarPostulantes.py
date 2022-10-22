'''
En una escuela de alta especializacion en informatica se evaluan a los postulantes
a, c/u se les toma 4 examenes, cada examen tiene una puntuacion de 0 a 100.
Para calcular el promedio se descartan la nota mas alta y la mas baja considerando
solo las 2 notas intermedias.
Escribir un programa modular que calcule el promedio de un postulante.
'''

# Modulo para validar nota
def LeerNroEntero(Texto,Minimo,Maximo):
    Nro = int(input(Texto))
    while (Nro<Minimo or Nro>Maximo):
        print("Error. Fuera de rango")
        Nro = int(input(Texto))
    return Nro

# Modulo para determinar numero Mayor de dos numeros
def MayorDos(A,B):
    if A > B:
        return A
    else:
        return B

# Modulo para determinar numero menor de dos numeros
def MenorDos(A,B):
    if A < B:
        return A
    else:
        return B
    
# leer nota de alumnos
Nota1 = LeerNroEntero('Ingrese la nota 1: ', 0, 100)
Nota2 = LeerNroEntero('Ingrese la nota 2: ', 0, 100)
Nota3 = LeerNroEntero('Ingrese la nota 3: ', 0, 100)
Nota4 = LeerNroEntero('Ingrese la nota 4: ', 0, 100)

# Determinar nota mayor
NotaMayor = MayorDos(MayorDos(Nota1,Nota2), MayorDos(Nota3, Nota4))

# Determinar nota menor
NotaMenor = MenorDos(MenorDos(Nota1,Nota2), MenorDos(Nota3, Nota4))

# Determinar Promedio
Promedio = (Nota1 + Nota2 + Nota3 + Nota4 - NotaMayor - NotaMenor)/2

# Escribir promedio
print('El promedio es: ',Promedio)