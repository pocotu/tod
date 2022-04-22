# Programa ejemplo de modularidad

# Módulo que muestra una línea de asteriscos
def Asteriscos(N):
    print('*'*N)

# Programa principal

# Mostrar mensajes con líneas de asteriscos
Texto1 = 'UNSAAC'
Texto2 = 'Ingeniería Informática y de Sistemas'
Texto3 = 'CUSCO-PERÚ'
# -- Mostrar primer texto          
Asteriscos(len(Texto1))
print(Texto1)
Asteriscos(len(Texto1))
# -- Mostrar primer texto          
Asteriscos(len(Texto2))
print(Texto2)
Asteriscos(len(Texto2))
# -- Mostrar primer texto          
Asteriscos(len(Texto3))
print(Texto3)
Asteriscos(len(Texto3))
