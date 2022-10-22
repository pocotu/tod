'''
Modificar el programa anterior para mejorar
la reusabilidad de codigo
'''

# Módulo de asteriscos
def Asteriscos(Multiplicador):
    print('*' * Multiplicador)

# Módulo que muestra un texto dentro de un recuadro de asteriscos
def TextoAsteriscos(Texto):
    Asteriscos(len(Texto)+4)
    print(f"* {Texto} *")
    Asteriscos(len(Texto)+4)

# Mostrar mensajes con líneas de asteriscos
TextoAsteriscos('UNSAAC')
TextoAsteriscos('Ingeniería Informática y de Sistemas')
TextoAsteriscos('CUSCO-PERÚ')