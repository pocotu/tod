# Imagina que tenemos una clase llamada 'Estudiante' que nos ayuda a crear estudiantes.
class Estudiante:
    # Cuando creamos un estudiante, le damos un nombre y una edad.
    def __init__(self, nombre, edad):
        self.nombreEstudiante = nombre
        self.edadEstudiante = edad

# Ahora, vamos a hacer una lista de estudiantes. Cada estudiante tiene un nombre y una edad.
lista_estudiantes = [
    Estudiante("Juan", 20),
    Estudiante("Maria", 22),
    Estudiante("Carlos", 21)
]

# Vamos a revisar la lista de estudiantes uno por uno y mostrar su nombre y edad.
for estudiante in lista_estudiantes:
    print("Nombre: ", estudiante.nombreEstudiante)
    print("Edad: ", estudiante.edadEstudiante)
    print("--------")


# Definimos una clase llamada 'Perro' para crear perros
class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

# Creamos una lista de perros
lista_de_perros = [
    Perro("Buddy", "Golden Retriever"),
    Perro("Luna", "Labrador"),
    Perro("Rocky", "Bulldog")
]

# Usamos un bucle 'for' para mostrar los nombres y razas de los perros
for perro in lista_de_perros:
    print("Nombre del perro:", perro.nombre)
    print("Raza del perro:", perro.raza)
    print("--------")
