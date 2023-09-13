import prettytable 

from Horario import Agenda
from alg_genetico import OptimizadorGenetico

def vis(VHorario):
    # funcion para visualizar el horario de clases de forma tabular
    etiqueta_colum = ['Hora', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']  # Etiquetas de las columnas (horas y dias)
    horas = ['7 am', '8 am', '9 am', '10 am', '11 am']  # Etiquetas de las filas (horas)
    
    tabla_valores = [[hora, "", "", "", "", ""]for hora in horas]  # Matriz de valores para la tabla [horas, lunes, martes, miercoles, jueves, viernes

    # Crea una tabla con las etiquetas y bordes
    # etiqueta_colum: etiquetas de las columnas
    # hrules: estilo de los bordes, prettytable.ALL: todos los bordes
    tabla = prettytable.PrettyTable(etiqueta_colum, hrules=prettytable.ALL)

    for s in VHorario:
        diaSemana = s.diaSemana
        horario = s.horario
        texto = 'curso: {} \n clase: {} \n salon: {} \n Profesor: {} \nDuracion: {} Horas'.format(s.idCurso, s.idClase, s.idSalon, s.idDocente, s.duracion)
        tabla_valores[diaSemana - 1][horario] = texto  # Agrega la informacion del horario en la matriz

    for row in tabla_valores:
        tabla.add_row(row)  # Agrega cada fila de la matriz a la tabla

    print(tabla)  # Imprime la tabla visual del horario

if __name__ == '__main__':
    horarios = []

    # Se crean instancias de Agenda con diferentes combinaciones de identificadores de curso, clase y docente
    horarios.append(Agenda("Algebra", 1201, "Docente 1", 2))
    horarios.append(Agenda("Algebra", 1201, "Docente 1", 2))
    horarios.append(Agenda("A.D.A.", 1201, "Docente 2", 2))
    horarios.append(Agenda("A.D.A.", 1201, "Docente 2", 2))
    horarios.append(Agenda("Avanzados", 1201, "Docente 3", 2))
    horarios.append(Agenda("Avanzados", 1201, "Docente 3", 2))
    horarios.append(Agenda("M. Discreta", 1201, "Docente 6", 2))
    horarios.append(Agenda("M. Discreta", 1201, "Docente 6", 2))

    horarios.append(Agenda("A.D.A.", 1202, "Docente 2", 2))
    horarios.append(Agenda("A.D.A.", 1202, "Docente 2", 1))
    horarios.append(Agenda("Programacion 1", 1202, "Docente 4", 2))
    horarios.append(Agenda("Programacion 1", 1202, "Docente 4", 2))
    horarios.append(Agenda("M. Discreta", 1202, "Docente 6", 2))
    horarios.append(Agenda("M. Discreta", 1202, "Docente 6", 2))

    horarios.append(Agenda("Avanzados", 1203, "Docente 3", 2))
    horarios.append(Agenda("Avanzados", 1203, "Docente 3", 1))
    horarios.append(Agenda("Programacion 1", 1203, "Docente 4", 2))
    horarios.append(Agenda("Programacion 1", 1203, "Docente 4", 2))
    horarios.append(Agenda("BioInformatica", 1203, "Docente 5", 2))
    horarios.append(Agenda("BioInformatica", 1203, "Docente 5", 2))
    horarios.append(Agenda("M. Discreta", 1203, "Docente 6", 1))
    horarios.append(Agenda("M. Discreta", 1203, "Docente 6", 2))
    

    ga = OptimizadorGenetico(tam_poblacion=50, elite=10, max_iteraciones=500)  # Se crea una instancia del Optimizador Genetico.

    resultado = ga.Evolucion(horarios, 3)  # Se ejecuta el algoritmo genetico para encontrar un horario optimo.

    horario_visualizado = []
    for r in resultado:
        if r.idClase == 1203:
            horario_visualizado.append(r)  # Se seleccionan los horarios especificos de la clase 1203.

    vis(horario_visualizado)  # Se visualiza el horario resultante.
