import numpy as np

# Horario de clases
class Horario:
    # Constructor
    def __init__(self, cursoID, claseID, profesorID):
        # Argumentos:
        # cursoID: int, id unico de curso
        # claseID: int, id unico de salon
        # profesor: int, id unico de docente
        self.cursoID = cursoID
        self.claseID = claseID
        self.profesorID = profesorID

        self.salonID = 0
        self.dia = 0
        self.hora = 0

    # Metodo para incializar los atributos
    def Random_atrib(self, salonRange):
        # Argumentos:
        # roomRange: int, numero de salones
        self.salonID = np.random.randint(1, salonRange+1, 1)[0]
        self.dia = np.random.randint(1, 6, 1)[0]
        self.hora = np.random.randint(1, 6, 1)[0]

# Funcion para ver el costo o numero de conflictos a la hora de crear un horario
def Costo_horario(poblacion, mejores_result):
    ## Calcula los conflictos de los horarios de clase.
    # Argumentos: 
    # Poblacion: list, poblacion de horarios de clase
    # mejores_result: int, numero mejor resultado
    conflictos = [0]
    n = len(poblacion[0]) # numero de horarios
    
    for x in poblacion:
        conflictos = 0
        for y in range(0, n-1):
            for z in range(y+1, n):
                # Verificar cursos en la misma hora y dia
                if 