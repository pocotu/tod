class cEgresado:
    # Metodo constructor
    def _init_(self, aIdEgresado="", aAP="", aAM="", aNombres="", aEspecialidad=""):
        self.aIdEgresado = aIdEgresado
        self.aAP = aAP
        self.aAM = aAM
        self.aNombres = aNombres
        self.aEspecialidad = aEspecialidad

        # GET y SET PARA CODIGO
    def getIdEgresado(self):
        return self.aIdEgresado
    def setIdEgresado(self, IdEgresado):
        self.aIdEgresado = IdEgresado

    def getAP(self):
        return self.aAP
    def setAP(self, AP):
        self.aAP = AP

    def getAM(self):
        return self.aAM
    def setAM(self, AM):
        self.aAM = AM

    def getNombres(self):
        return self.aNombres
    def setNombres(self, Nombres):
        self.aNombres = Nombres

    def getEspecialidad(self):
        return self.aEspecialidad
    def setEspecialidad(self, Especialidad):
        self.aEspecialidad = Especialidad

    def Leer(self):
        self.aIdEgresado = input("Ingrese ID de egresado: ")
        self.aAP = input("Ingrese AP: ")
        self.aAM = input("Ingrese AM: ")
        self.aNombres = input("Ingrese Nombre: ")
        self.aEspecialidad = input("Ingrese Especialidad: ")

    def Mostrar(self):
        # print("\nMostrar datos: ")
        print("ID de egresado: ", self.aIdEgresado)
        print("AP: ", self.aAP)
        print("AM: ", self.aAM)
        print("Nombre: ", self.aNombres)
        print("Especialidad: ", self.aEspecialidad)

class cEgresadoTrabajo:
    # Metodo constructor
    def _init_(self, aNroRegistro="", aIdEgresado="", aTrabajo="", aInstitucion="", aPais="", aAnio=0):
        self.aNroRegistro = aNroRegistro
        self.aIdEgresado = aIdEgresado
        self.aTrabajo = aTrabajo
        self.aInstitucion = aInstitucion
        self.aPais = aPais
        self.aAnio = aAnio

        # GET y SET PARA CODIGO
    def getNroRegistro(self):
        return self.aNroRegistro
    def setNroRegistro(self, NroRegistro):
        self.aNroRegistro = NroRegistro

    def getIdEgresado(self):
        return self.aIdEgresado
    def setIdEgresado(self, IdEgresado):
        self.aIdEgresado = IdEgresado

    def getTrabajo(self):
        return self.aTrabajo
    def setTrabajo(self, Trabajo):
        self.aTrabajo = Trabajo

    def getInstitucion(self):
        return self.aInstitucion
    def setInstitucion(self, Institucion):
        self.aInstitucion = Institucion

    def getPais(self):
        return self.aPais
    def setPais(self, Pais):
        self.aPais = Pais

    def getAnio(self):
        return self.aAnio
    def setAnio(self, aAnio):
        self.aAnio = aAnio

    def Leer(self):
        self.aNroRegistro = input("Ingrese Nro de registro: ")
        self.aIdEgresado = input("Ingrese ID: ")
        self.aTrabajo = input("Ingrese trabajo: ")
        self.aInstitucion = input("Ingrese institucion: ")
        self.aPais = input("Ingrese pais: ")
        self.aAnio = input("Ingrese año: ")

    def Mostrar(self):
        # print("\nMostrar datos: ")
        print("Nro de registro: ", self.aNroRegistro)
        print("ID de egresado: ", self.aIdEgresado)
        print("Trabajo: ", self.aTrabajo)
        print("Institucion: ", self.aInstitucion)
        print("Pais: ", self.aPais)
        print("Año: ", self.aAnio)

#### ARREGLO ELECTRODOMESTICO ######
def agregarEgresado(lista, n):
    for i in range(0,n):
        print(f"\n Ingreso de datos {i+1}: ")
        #CREANDO OBJETO
        nEgresado = cEgresado()
        nEgresado.Leer()
        lista = lista + [nEgresado]
    return lista
def mostrarEgresado(lista, n):
    for i in range(0,n):
        print(f"\n Datos de Egresado {i+1}: ")
        lista[i].Mostrar()

def menu():
    print("\n MENU")
    print("  1: Agregar Egresado")
    print("  2: Mostrar Egresado")
    print("  0: Salir")

print( " ► EGRESADOS ◄")
n = int(input("Nro de Egresados: "))
lista = []
lista = agregarEgresado(lista, n)
mostrarEgresado(lista, n)

op = 1
while op != 0:
    # Mostrar menu
    menu()
    op = int(input(" Ingrese opcion: "))

    if op == 1:
        # Agregar electrodomestico
        print("Agregar electrodomestico")
        Egresado = cEgresado()
        Egresado.Leer()
        lista = lista + [Egresado]
        n = n + 1
    elif op == 2:
        mostrarEgresado(lista, n)

    elif op == 0:

        break
    else:
        print("Opcion no valida")
cEgresados = {

    "egre1": ["E01", "ap", "am", "Moto Moto", "Ingenieria de sistemas"],
    "egre2": ["E01", "ap", "am", "Chupetin", "Ingenieria de sistemas"]
}

cEgresadosTrabajo = {

    "egreT1": ["R01", "ET01", "TI", "Caja Cusco", "Peru","2022"],
    "egreT2": ["R02", "ET02", "Desarrolador de software", "Google", "Peru","2022"]
}

#print(cEgresados["egre1"])

for k, value in cEgresadosTrabajo.items():
  print("EgresadoTrabajo: ", k)
  print("Datos:", value)
print("\n")
for k, value in cEgresados.items():
  print("Egresado: ", k)
  print("Datos:", value)
print("\n")
print(cEgresadosTrabajo["egreT1"][4])
sum = 0

for i in cEgresadosTrabajo:
    if cEgresadosTrabajo[i][4] == "Peru":
        sum = sum+1
print(sum)