# En la ONPE se tiene la relación de personas (DNI, Nombre, Ciudad) habilitadas para ser
# miembros de mesa almacenadas en una lista. Adicionalmente se tiene la relación de
# accesitarios almacenados en una pila. Hacer un algoritmo que:
# 1. Dado el DNI de una persona habilitada, la reemplace por un accesitario.
# 2. Generar una nueva lista con todas las personas habilitadas de la ciudad de “Cusco”

# Suponiendo que se tiene una lista de personas habilitadas "personas" y una pila de accesitarios "accesitarios"

personas = [{"DNI": "123", "Nombre": "Juan", "Ciudad": "Cusco"},
    {"DNI": "456", "Nombre": "Maria", "Ciudad": "Lima"},
    {"DNI": "789", "Nombre": "Pedro", "Ciudad": "Cusco"}]

accesitarios = [{"DNI": "12345678", "Nombre": "Juan", "Ciudad": "Cusco"},
    {"DNI": "45678901", "Nombre": "Maria", "Ciudad": "Lima"},
    {"DNI": "78901234", "Nombre": "Pedro", "Ciudad": "Cusco"}]

def reemplazar_persona_por_accesitario(dni):
    # Buscar la persona habilitada en la lista
    persona = next((p for p in personas if p["DNI"] == dni), None)
    if persona:
        # Reemplazar la persona habilitada con el accesitario de la cima de la pila
        index = personas.index(persona)
        personas[index] = accesitarios.pop()

def obtener_personas_de_ciudad(ciudad):
    return [p for p in personas if p["Ciudad"] == ciudad]

# para obtener las personas de Cusco
personas_de_cusco = obtener_personas_de_ciudad("Cusco")

# imprimir lista de personas antes de reemplazar
print(personas)

# para reemplazar a la persona con DNI 12345678 por un accesitario
reemplazar_persona_por_accesitario("12345678")
