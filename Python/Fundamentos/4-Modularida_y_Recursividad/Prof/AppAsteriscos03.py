# Programa ejemplo de modularidad

# Módulo que muestra una línea de asteriscos
def Asteriscos(N):
    print('*'*N)

# Módulo que muestra un texto dentro de un recuadro de asteriscos
def TextoAsteriscos(Texto):
    Asteriscos(len(Texto))
    print(Texto)
    Asteriscos(len(Texto))

# Mostrar mensajes con líneas de asteriscos
TextoAsteriscos('UNSAAC')
TextoAsteriscos('Ingeniería Informática y de Sistemas')
TextoAsteriscos('CUSCO-PERÚ')
