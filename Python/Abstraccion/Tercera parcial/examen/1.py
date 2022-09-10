class cInvestigacion():
    def __init__(self, IdEscuela, NroTrabajosInvestigacion, NroInvestigadoresDocente, NroInvestigadoresAlumno):
        self.IdEscuela = IdEscuela
        self.NroTrabajosInvestigacion = NroTrabajosInvestigacion
        self.NroInvestigadoresDocente = NroInvestigadoresDocente
        self.NroInvestigadoresAlumno = NroInvestigadoresAlumno

class cEscuela():
    def __init__(self, IdEscuela, Nombre, Facultad):
        self.IdEscuela = IdEscuela
        self.Nombre = Nombre
        self.Facultad = Facultad

ArregloEscuelas = [ cEscuela("IN","Ingeniería Informática","FTIC"), 
                    cEscuela("IS", "Ingeniería de Software", "FTIC"), 
                    cEscuela("CD", "Ciencia de Datos", "FTIC"), 
                    cEscuela("CO", "Contabilidad", "FCC"), 
                    cEscuela("MH", "Medicina Humana", "FCS"), 
                    cEscuela("OD", "Odontología", "FCS"),
                    cEscuela("EN", "Enfermería", "FCS")]

ArregloInvestigacion = [cInvestigacion("IN", 10, 21, 12),
                        cInvestigacion("IS", 8, 16, 16), 
                        cInvestigacion("CD", 16, 38, 22),
                        cInvestigacion("CO", 5, 12, 8),
                        cInvestigacion("MH", 8, 14, 0),
                        cInvestigacion("OD", 7, 14, 2),
                        cInvestigacion("EN", 5, 10, 0)]


# Determinar el número de investigadores docente y el número de investigadores alumno de una determinada facultad.
# mostrar investigadores docente de una facultad
def InvestigadoresDocente(Facultad):
    contador = 0
    for i in range(len(ArregloEscuelas)):
        if ArregloEscuelas[i].Facultad == Facultad:
            contador += ArregloInvestigacion[i].NroInvestigadoresDocente
    return contador

# mostrar investigadores alumno de una facultad
def InvestigadoresAlumno(Facultad):
    contador = 0
    for i in range(len(ArregloEscuelas)):
        if ArregloEscuelas[i].Facultad == Facultad:
            contador += ArregloInvestigacion[i].NroInvestigadoresAlumno
    return contador

print("Investigadores docente de la facultad de Ingeniería de Software: ",InvestigadoresDocente("FTIC"))
print("Investigadores alumno de la facultad de Ingeniería de Software: ",InvestigadoresAlumno("FTIC"))
print("Investigadores docente de la facultad de Ciencias de Datos: ",InvestigadoresDocente("FTIC"))
print("Investigadores alumno de la facultad de Ciencias de Datos: ",InvestigadoresAlumno("FTIC"))

# Mostrar las Escuelas de una determinada Facultad que tienen más de N investigadores docente.
def EscuelasFacultad(Facultad, N):
    for i in range(len(ArregloEscuelas)):
        if ArregloEscuelas[i].Facultad == Facultad and ArregloInvestigacion[i].NroInvestigadoresDocente > N:
            print(ArregloEscuelas[i].Nombre)
N = int(input("Introduce el número de investigadores docente: "))
print("Escuelas de la facultad de Ingeniería de Software que tienen más de ",N," investigadores docente: ")
EscuelasFacultad("FTIC", N)
print("Escuelas de la facultad de Ciencias de Datos que tienen más de ",N," investigadores docente: ")
EscuelasFacultad("FTIC", N)

