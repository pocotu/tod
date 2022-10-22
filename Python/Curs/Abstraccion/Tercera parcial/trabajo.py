"""
La Universidad como parte del proceso de automatización de la información académica, 
solicita la implementación de un software. Para lo cual a Ud. se le solicita lo siguiente:

1.- Implementar las siguientes clases:

- Escuela profesional, con los siguientes atributos: CodEscuela, NombreEscuela.
- Alumno, con los siguientes atributos: CodAlumno, AP, AM, Nombres, CodEscuela.
- Asignatura, con los siguientes atributos: CodAsignatura, Nombre, Categoría, Creditaje.
- Matrícula, con los siguientes atributos: Semestre, CodAsignatura, CodAlumno, Nota.

2.- Implementar una aplicación que permita:

- Registrar en arreglos de objetos de estas clases; considerando las validaciones necesarias. 
  Por ejemplo, que el código de Escuela profesional de un estudiante
  debe existir en el arreglo de Escuelas Profesionales; que el código de alumno de un 
  objeto de la clase matrícula debe existir en el arreglo de alumnos; etc.
- Mostrar la información de los arreglos.
- Procesar la información del arreglo de matrículas. Por ejemplo, mostrar e
  studiantes de una determinada asignatura en un determinado semestre.
"""

# Implementacion de clases
# Clase Escuela Profesional con atributos CodEscuela, NombreEscuela
class cEscuelaProfesional:
    # Metodo constructor
    def _init_(self, CodEscuela="", NombreEscuela=""):
        self.CodEscuela = CodEscuela
        self.NombreEscuela = NombreEscuela

        # Get y Set de CodEscuela
    def getCodEscuela(self):
        return self.CodEscuela

    def setCodEscuela(self, CodEscuela):
        self.CodEscuela = CodEscuela

    def getNombreEscuela(self):
        return self.NombreEscuela

    def setNombreEscuela(self, NombreEscuela):
        self.NombreEscuela = NombreEscuela

    def Leer(self):
        self.CodEscuela = input("Ingrese Codigo de Escuela: ")
        self.NombreEscuela = input("Ingrese Nombre de Escuela: ")

    def Mostrar(self):
        print("Codigo de Escuela: ", self.aCodEscuela)
        print("Nombre de Escuela: ", self.aNombreEscuela)
    
# Clase Alumno
class cAlumno:
    # Metodo constructor
    def _init_(self, CodAlumno="", AP="", AM="", Nombres="", CodEscuela=""):
        self.CodAlumno = CodAlumno
        self.AP = AP
        self.AM = AM
        self.Nombres = Nombres
        self.CodEscuela = CodEscuela
        # GET y SET PARA CODIGO
    def getCodAlumno(self):
        return self.CodAlumno
    def setCodAlumno(self, CodAlumno):
        self.CodAlumno = CodAlumno
    def getAP(self):
        return self.AP
    def setAP(self, AP):
        self.AP = AP
    def getAM(self):
        return self.AM
    def setAM(self, AM):
        self.AM = AM
    def getNombres(self):
        return self.Nombres
    def setNombres(self, Nombres):
        self.Nombres = Nombres
    def getCodEscuela(self):
        return self.CodEscuela
    def setCodEscuela(self, CodEscuela):
        self.CodEscuela = CodEscuela
    
    def Leer(self):
        self.CodAlumno = input("Ingrese Codigo de Alumno: ")
        self.AP = input("Ingrese Apellido Paterno: ")
        self.AM = input("Ingrese Apellido Materno: ")
        self.Nombres = input("Ingrese Nombres: ")
        self.CodEscuela = input("Ingrese Codigo de Escuela: ")
    
    def Mostrar(self):
        print("Codigo de Alumno: ", self.CodAlumno)
        print("Apellido Paterno: ", self.AP)
        print("Apellido Materno: ", self.AM)
        print("Nombres: ", self.Nombres)
        print("Codigo de Escuela: ", self.CodEscuela)
    
# Clase Asignatura
class cAsignatura:
    # Metodo constructor
    def _init_(self, CodAsignatura="", Nombre="", Categoria="", Creditaje=""):
        self.CodAsignatura = CodAsignatura
        self.Nombre = Nombre
        self.Categoria = Categoria
        self.Creditaje = Creditaje
        # GET y SET PARA CODIGO
    def getCodAsignatura(self):
        return self.CodAsignatura
    def setCodAsignatura(self, CodAsignatura):
        self.CodAsignatura = CodAsignatura
    def getNombre(self):
        return self.aNombre
    def setNombre(self, Nombre):
        self.Nombre = Nombre
    def getCategoria(self):
        return self.Categoria
    def setCategoria(self, Categoria):
        self.Categoria = Categoria
    def getCreditaje(self):
        return self.Creditaje
    def setCreditaje(self, Creditaje):
        self.Creditaje = Creditaje
    
    def Leer(self):
        self.CodAsignatura = input("Ingrese Codigo de Asignatura: ")
        self.Nombre = input("Ingrese Nombre de Asignatura: ")
        self.Categoria = input("Ingrese Categoria de Asignatura: ")
        self.Creditaje = input("Ingrese Creditaje de Asignatura: ")
    
    def Mostrar(self):
        print("Codigo de Asignatura: ", self.aCodAsignatura)
        print("Nombre de Asignatura: ", self.aNombre)
        print("Categoria de Asignatura: ", self.aCategoria)
        print("Creditaje de Asignatura: ", self.aCreditaje)
    
# Clase Matricula
class cMatricula:
    # Metodo constructor
    def _init_(self, CodAlumno="", CodAsignatura="", Semestre="", Anio=""):
        self.CodAlumno = CodAlumno
        self.CodAsignatura = CodAsignatura
        self.Semestre = Semestre
        self.Anio = Anio
        # GET y SET PARA CODIGO
    def getCodAlumno(self):
        return self.CodAlumno
    def setCodAlumno(self, CodAlumno):
        self.CodAlumno = CodAlumno
    def getCodAsignatura(self):
        return self.CodAsignatura
    def setCodAsignatura(self, CodAsignatura):
        self.CodAsignatura = CodAsignatura
    def getSemestre(self):
        return self.Semestre
    def setSemestre(self, Semestre):
        self.Semestre = Semestre
    def getAnio(self):
        return self.Anio
    def setAnio(self, Anio):
        self.Anio = Anio
    
    def Leer(self):
        self.CodAlumno = input("Ingrese Codigo de Alumno: ")
        self.CodAsignatura = input("Ingrese Codigo de Asignatura: ")
        self.Semestre = input("Ingrese Semestre: ")
        self.Anio = input("Ingrese Anio: ")
    
    def Mostrar(self):
        print("Codigo de Alumno: ", self.CodAlumno)
        print("Codigo de Asignatura: ", self.CodAsignatura)
        print("Semestre: ", self.Semestre)
        print("Anio: ", self.Anio)

# Registrar en arreglos de las clases, haciendo validaciones
def Registrar():
    # Creacion de objetos
    objEscuela = cEscuela()
    objAlumno = cAlumno()
    objAsignatura = cAsignatura()
    objMatricula = cMatricula()
    # Validaciones
            





