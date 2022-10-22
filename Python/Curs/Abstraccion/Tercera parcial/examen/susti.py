'''
Dada la condición de ACREDITADA de la Escuela profesional de Ingeniería Informática y de Sistemas, 
se debe automatizar en lo posible todos los procesos. Para tal efecto, al equipo de Informática se le pide automatizar 
la gestión de los egresados de la Escuela. 
En este sentido, uno de los integrantes implementó la siguiente clase:
- cEgresado, con los siguientes atributos: aIdEgresado, aAP, aAM, aNombres, aEspecialidad, aTrabajo y aPais.

Otro integrante del equipo informático registró objetos de la clase cEgresado en un arreglo.

A Ud. Se le pide escribir módulos para:

1.- Determinar cuántos egresados trabajan actualmente en el extranjero.

2.- Mostrar la relación de egresados de una determinada Especialidad que actualmente vienen trabajando en un determinado país.
'''

# Clase cEgresado con los atributos aIdEgresado, aAP, aAM, aNombres, aEspecialidad, aTrabajo y aPais
class cEgresado():
    def __init__(self, aIdEgresado, aAP, aAM, aNombres, aEspecialidad, aTrabajo, aPais):
        self.aIdEgresado = aIdEgresado
        self.aAP = aAP
        self.aAM = aAM
        self.aNombres = aNombres
        self.aEspecialidad = aEspecialidad
        self.aTrabajo = aTrabajo
        self.aPais = aPais
    
# Determinar cuántos egresados trabajan actualmente en el extranjero
def cuantosExtranjeros(cEgresado):
    contador = 0
    for i in range(len(cEgresado)):
        if cEgresado[i].aTrabajo == 'Extranjero':
            contador += 1
    return contador

# Mostrar la relación de egresados de una determinada Especialidad que actualmente vienen trabajando en un determinado país
def mostrarEgresados(cEgresado, aEspecialidad, aPais):
    for i in range(len(cEgresado)):
        if cEgresado[i].aEspecialidad == aEspecialidad and cEgresado[i].aPais == aPais:
            print('Egresados en el pais de {} ' '\n' 'Especialidad: {}' '\n' 'Nombre: {}' '\n' 'Apellido Paterno: {}' '\n' 'Apellido Materno: {}' '\n' '-----------------------------' '\n'.format(aPais, aEspecialidad, cEgresado[i].aNombres, cEgresado[i].aAP, cEgresado[i].aAM))

# Objetos de la clase cEgresado
cEgresado = [cEgresado(1, 'Perez', 'Zarate', 'Carlos', 'Inteligencia Articicial', 'Extranjero', 'Mexico'),
            cEgresado(2, 'Puma', 'Cano', 'Diana', 'Ciberseguridad', 'Extranjero', 'Brazil'), 
            cEgresado(3, 'Huillca', 'Lozano', 'David', 'Ingeniero de software', 'Extranjero', 'Mexico'), 
            cEgresado(4, 'Zegarra', 'Meza', 'Diego', 'Inteligencia Artificial', 'Local', 'Peru'), 
            cEgresado(5, 'Gonzales', 'Gonzalez', 'Eduardo', 'Ingeniero de software', 'Local', 'Peru')]

# Imprimir egresados que trabajan en el extranjero
print('Egresados que trabajan en el extranjero: {}'.format(cuantosExtranjeros(cEgresado)))

# Imprimir relacion de egresados de una determinada especialidad que actualmente vienen trabajando en un determinado país
mostrarEgresados(cEgresado, 'Inteligencia Artificial', 'Peru')