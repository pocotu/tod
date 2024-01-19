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
    
    def AgregarResta(self, valor, op, valorRango):
        if op > 0.5:
            if valor < valorRango:
                valor += 1
            else:
                valor -= 1
        else:
            if valor - 1 > 0:
                valor -= 1
            else:
                valor += 1
        
        return valor

    def Mutar(self, poblacion, salonRango):
        e = np.random.randint(0, self.elite, 1)[0]
        pos = np.random.randint(0, 2, 1)[0]
        ep = copy.deepcopy(poblacion[e])

        for p in ep:
            pos = np.random.randint(0, 3, 1)[0]
            operation = np.random.rand()

            if pos == 0:
                p.idSalon = self.AgregarResta(p.idSalon, operation, salonRango)
            if pos == 1:
                p.diaSemana = self.AgregarResta(p.diaSemana, operation, 5)
            if pos == 2:
                p.horario = self.AgregarResta(p.horario, operation, 3)
        
        return ep
    
    def Cruzar(self, poblacionElite):
        e1 = np.random.randint(0, self.elite, 1)[0]


    def Evolucion(self, horarios. salonRango):