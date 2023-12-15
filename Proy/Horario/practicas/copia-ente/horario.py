
import numpy as np

class Agenda:
    # Clase que representa una agenda de horarios para cursos, clases y docentes
    
    def __init__(self, idCurso, idClase, idDocente):
        self.idcurso = idCurso
        self.idClase = idClase
        self.idDocente = idDocente

        # Inializar matriz de horarios con ceros
        self.idSalon = 0
        self.diaSemana = 0
        self.horario = 0

    def Inicializador_aleatorio(self, salonRango):
        # Método que inicializa la agenda con horarios aleatorios dentro de un rango de salones
        # :param salonRango: Rango de salones disponibles
        
        self.idSalon = np.random.randint(1, salonRango + 1, 1)[0]
        self.diaSemana = np.random.randint(1, 6, 1)[0]
        self.horario = np.random.randint(1, 6, 1)[0]
    
# Esta función calcula el costo de horario para una población de horarios.
# Recibe dos parámetros: poblacion (una lista de horarios) y elite (el número de mejores horarios a seleccionar).
# La función recorre cada horario de la población y verifica si hay conflictos de horario entre las clases.
# Los conflictos se cuentan y se almacenan en una lista.
# Luego, se ordenan los conflictos de menor a mayor y se retorna el índice de los mejores horarios y su costo de conflictos.
def CostoHorario(poblacion, elite):
    conflictos = []
    n = len(poblacion[0])

    for p in poblacion:
        conflicto = 0

        for i in range(0, n - 1):
            for j in range(i + 1, n):
                # Verificar si hay conflicto de horario entre dos clases en el mismo salon y dia
                if p[i].idSalon == p[j].idSalon and p[i].diaSemana == p[j].diaSemana and p[i].horario == p[j].horario:
                    conflicto += 1

                # Verificar si hay conflicto de horario entre dos clases con el mismo docente en el mismo dia y horario
                if p[i].idDocente == p[j].idDocente and p[i].diaSemana == p[j].diaSemana and p[i].horario == p[j].horario:
                    conflicto += 1

                # Verificar si hay conflicto de horario entre dos clases con el mismo curso y docente en el mismo dia
                if p[i].idClase == p[j].idClase and p[i].idCurso == p[j].idCurso and p[i].diaSemana == p[j].diaSemana:
                    conflicto += 1

        conflictos.append(conflicto)
    
    indice = np.array(conflictos).argsort()  # Ordenar los conflictos de menor a mayor

    # Retornar los mejores horarios de la poblacion y su costo de conflictos de horario
    return indice[ :elite], conflictos[indice[0]]
