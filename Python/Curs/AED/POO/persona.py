# crea una clase persona con atributos nombre, 
# DNI y fecha de nacimiento
# un metodo que muestre por pantalla los datos de la persona
# con constructor y metodo get y set y herecia de la clase persona
# crear una clase alumno que herede de persona y tenga como atributos
# la matricula y el curso
# todo comentado

class Persona:
    def __init__(self, nombre, dni, fecha_nacimiento):
        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento

    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("DNI: ", self.dni)
        print("Fecha de nacimiento: ", self.fecha_nacimiento)

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_dni(self):
        return self.dni

    def set_dni(self, dni):
        self.dni = dni

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento


class Alumno(Persona):
    def __init__(self, nombre, dni, fecha_nacimiento, matricula, curso):
        super().__init__(nombre, dni, fecha_nacimiento)
        self.matricula = matricula
        self.curso = curso

    def mostrar(self):
        super().mostrar()
        print("Matricula: ", self.matricula)
        print("Curso: ", self.curso)

    def get_matricula(self):
        return self.matricula

    def set_matricula(self, matricula):
        self.matricula = matricula

    def get_curso(self):
        return self.curso

    def set_curso(self, curso):
        self.curso = curso


persona1 = Persona("Juan", "12345678A", "01/01/2000")
persona1.mostrar()
print("Nombre: ", persona1.get_nombre())
print("DNI: ", persona1.get_dni())
print("Fecha de nacimiento: ", persona1.get_fecha_nacimiento())




