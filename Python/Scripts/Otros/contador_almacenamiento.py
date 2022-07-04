""" Funciones y condicionales: calcula_almacenamiento.py
  Por about.me/carlosgbr
  Versión 1
  Para Python 3.0 y superior
  Entrada: 
  Salida: 
  Se ilustra el uso de funciones y la estructura if en Python
"""
"""
ENUNCIADO: Si un sistema de archivos tiene un tamaño de bloque de 4096 bytes, 
esto significa que un archivo compuesto por un solo byte seguirá usando 4096 
bytes de almacenamiento. Un archivo compuesto por 4097 bytes usará 
4096 * 2 = 8192 bytes de almacenamiento. Sabiendo esto, ¿puede completar los 
espacios en la función calcula_almacenamiento a continuación, que calcula el tamaño 
de almacenamiento necesario para un tamaño de archivo determinado?
"""
def calcula_almacenamiento(tamanoarchivo):
    tamano_bloque = 4096
    # Use la división de piso para calcular cuántos bloques están completamente ocupados
    bloques_completos = tamanoarchivo // tamano_bloque
    # Use el operador de módulo para verificar si hay algún resto
    residuo_parcial_bloque = tamanoarchivo % tamano_bloque
    # Dependiendo de si hay un resto o no, devuelva el número correcto.
    if residuo_parcial_bloque > 0:
        return bloques_completos * tamano_bloque + tamano_bloque
    return bloques_completos * tamano_bloque

print(calcula_almacenamiento(1))    # Debiera ser 4096
print(calcula_almacenamiento(4096)) # Debiera ser 4096
print(calcula_almacenamiento(4097)) # Debiera ser 8192
print(calcula_almacenamiento(6000)) # Debiera ser 8192