def char_mas_comun(string):
  # Creamos un diccionario vacío para almacenar la frecuencia de cada caracter
  frecuentes = {}
  for c in string:
    # Si el caracter ya está en el diccionario, incrementamos su valor en 1
    if c in frecuentes:
      frecuentes[c] += 1
    # Si no está, lo agregamos al diccionario con valor 1
    else:
      frecuentes[c] = 1
  
  # Buscamos el caracter con el valor máximo en el diccionario
  char_mas_comun = max(frecuentes, key=frecuentes.get)
  return char_mas_comun

def main():
  string = input("Ingresa una cadena de caracteres: ")
  print("El caracter más común es: ", char_mas_comun(string))

main()
