# Calcula el promedio de una asignatura

# Leer el número de estudiantes
N = int(input('Ingresa el número de estudiantes: '))

# Calcular el promedio de todos los estudiantes
K = 0
SumaPromedios = 0
while K < N:
    # Incrementar contador
    K += 1
    # Leer promedio del K-ésimo estudiante
    Promedio = float(input('Promedio del estudiante '+str(K)+': '))
    # Acumular 
    SumaPromedios += Promedio
    print('SumaPromedios = ',SumaPromedios)

# Calcular promedio de la asignatura
PromedioAsignatura = SumaPromedios / N
# Mostrar el promedio de la asignatura
print('Promedio asignatura = ', PromedioAsignatura)  
