"""
Modificar el programa anterior de modo que los textos
sean mostrados entre lineas de asteriscos de la misma
longitud que los textos
"""

# Modulo Asteriscos
def Asteriscos(A):
    print('*' * A)

# Modulo principal
# Definir los textos
Text1 = 'Unsaac'
Text2 = 'Ingenieria Informatica y de sistemas'
Text3 = 'Cusco - Peru'

# Mostrar primer texto
Asteriscos(len(Text1)+4)
print(f"* {Text1} *")
Asteriscos(len(Text1)+4)

# Mostrar sengundo texto
Asteriscos(len(Text2)+4)
print(f"* {Text2} *")
Asteriscos(len(Text2)+4)

# Mostrar tercer texto
Asteriscos(len(Text3)+4)
print(f"* {Text3} *")
Asteriscos(len(Text3)+4)
