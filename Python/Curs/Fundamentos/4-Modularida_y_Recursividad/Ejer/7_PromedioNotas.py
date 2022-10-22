'''
Escribir un programa modular para calcular el promedio de 3 notas
validando la nota, de modo que acepte un valor entre 0 y 20.
'''

# Modulo para leer una nota
def LeerNota():
    Nota = int(input("Ingrese nota: "))
    while (nota<0 or nota>20):
        print("Error al ingresar nota. FUERA DE RANGO")
        Nota = int(input("Ingrese nota: "))
    return Nota

# Programa principal
# Ingresar las notas
Nota1 = leerNota()
Nota2 = LeerNota()
Nota3 = LeerNota()

# Calcular el promedio
Promedio = (Nota1 + Nota2 + Nota3)/3

# Mostrar promedio
print('El promedio es: ',Promedio)
