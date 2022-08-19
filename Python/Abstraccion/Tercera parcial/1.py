'''
crear un objeto de un alumno con 4 atributos y 2 metodos
'''

class Alumno:
    def __init__(self, nombre, apellido, edad, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.carrera = carrera
    def saludar(self):
        print('Hola, me llamo {} {} y tengo {} años y soy de la carrera de {}'.format(self.nombre, self.apellido, self.edad, self.carrera))

alumno1 = Alumno('Juan', 'Perez', 20, 'Ingenieria de sistemas')

Alumno.saludar(alumno1)
