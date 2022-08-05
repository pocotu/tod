'''
A un estudiante le pidieron escribir un módulo que 
efectúe la normalización de una colección de números reales. 
Para llevar a cabo esta normalización, se debe en primer lugar encontrar el 
número mayor de la colección; luego se divide cada número por dicho valor máximo, de forma
que los valores resultantes (normalizados) estén comprendidos en el intervalo
 del 0 al 1. El estudiante escribió el siguiente código.
'''

def Normalizacion(A):
    return [X / max(A) for X in A]    
Normalizacion([1,2,3,4,5])