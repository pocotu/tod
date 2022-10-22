"""
Escribir un algoritmo de calcule las decenas y unidades contenidas en un numero de 2 dígitos.
"""
# Leer numero de 2 digitos
numero = int(input("Ingrese el numero: "))

# Descomponer numero de decenas y unidades
Unidad = numero%10
Decena = (numero%100)//10
Centena = (numero//100)%10
UnidadMillar = numero//1000

# Mostrar resultados
print("El numero descompuesto es:")
print("Unidad: ",Unidad)
print("Decena: ",Decena)
print("Centena: ",Centena)
print("Unidade de millar: ",UnidadMillar)
