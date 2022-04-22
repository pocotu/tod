'''
Escribir un algoritmo que dado un texto determine el número de palabras que
tienen menos de 5 letras.
'''
# --- Leer el texto
Texto = input('Ingrese un texto: ')
# --- Dividir el texto en palabras
Palabras = Texto.split()
# --- Contar las palabras que tienen menos de 5 letras
NroPalabras = 0
for Palabra in Palabras:
    if len(Palabra) < 5:
        print(Palabra)
        NroPalabras += 1    
# --- Mostrar el resultado
print(NroPalabras)

