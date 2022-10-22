"""
En el curso de F de programación la calificacion final se calcula de acuerdo a: 
-	Primer examen 25%
-	Segundo examen 25%
-	Tareas 20%
-	Examen final 30%
Escribir un algoritmo para determinar la califiacion de un estudiante.
"""

# Leer las notas
PrimerExamen = float(input("Ingrese el primer examen: "))
SegundoExamen = float(input("Ingrese el segundo examen: "))
Tareas = float(input("Ingrese la nota de las tareas: "))
ExamenFinal = float(input("Ingrese la nota del examen final: "))

# Calcular calificaciones
CalcularNotas = PrimerExamen*0.25+SegundoExamen*0.25+Tareas*0.2+ExamenFinal*0.3

# Mostrar resultados
print("La calificacion es= ",CalcularNotas)


