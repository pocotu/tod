#6.	Implementar un programa que imprime la palabra más común de un texto:
#   o	Use el split() para quebrar el string en una lista de palabras.
#   o	Use las palabras como claves del diccionario
#   o	Convierta cada palabra para minúscula con la función lower.
#   o	Remueva los caracteres de puntuación de las palabras. 
#       Vea la constante puntuación https://docs.python.org/3.4/library/string.html#string.punctuation
import string
import re

def find_most_common_word(text):
  # Dividir el texto en una lista de palabras
  words = text.split()
  
  # Crear un diccionario para contar la frecuencia de cada palabra
  word_count = {}
  
  # Recorrer la lista de palabras y contar su frecuencia
  for word in words:
    # Convertir la palabra a minúsculas y remover caracteres de puntuación
    word = word.lower().strip(string.punctuation)
    
    # Aumentar el contador del diccionario para esta palabra
    if word in word_count:
      word_count[word] += 1
    else:
      word_count[word] = 1
  
  # Encontrar la palabra más común
  most_common_word = None
  highest_count = 0
  for word, count in word_count.items():
    if count > highest_count:
      most_common_word = word
      highest_count = count
  
  # Imprimir la palabra más común
  print(f"La palabra más común es '{most_common_word}' con una frecuencia de {highest_count}.")

# Leer el texto del usuario
text = input("Ingrese el texto: ")

# Encontrar la palabra más común en el texto
find_most_common_word(text)


