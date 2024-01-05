import copy
import numpy as np

from horario import CostoHorario

class optimizadorGenetico:
    def __init__(self, tam_poblacion=30, prob_mutacion=0.3, elite=0.5, max_iteraciones=100):
        self.tam_poblacion = tam_poblacion
        self.prob_mutacion = prob_mutacion
        self.elite = elite
        self.ma_interaciones = max_iteraciones

    def Iniciar_poblacion(self, horarios, salonRango):
        self.poblacion = []

        for i in range(self.tam_poblacion):
            entidad = []

            for s in horarios:
                s.Inicializador_aleatorio(salonRango)
                entidad.append(copy.deepcopy(s))

            self.poblacion.append(entidad)
    
    def 