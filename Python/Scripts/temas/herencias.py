class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
    
    def arrancar(self):
        self.enmarcha = True
    
    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True
    
    def estado(self):
        print('Marca: ', self.marca, '\nModelo: ', self.modelo, '\nEn marcha: ', self.enmarcha, '\nAcelera: ',
            self.acelera, '\nFrena: ', self.frena)

class Moto(Vehiculos):
    Hcaballito = ""
    def caballito(self):
        self.Hcaballito = "Estoy haciendo el caballito"
    
    def estado(self):
        print('Marca: ', self.marca, '\nModelo: ', self.modelo, '\nEn marcha: ', self.enmarcha, '\nAcelera: ',
            self.acelera, '\nFrena: ', self.frena, '\n', self.Hcaballito) 

class Camioneta(Vehiculos):
    def carga(self, carga):
        self.cargado = carga
        if (self.cargado):
            return "La camioneta esta cargada"
        else:
            return "La camioneta no esta cargada"

moto1 = Moto('Honda', '2015')
moto1.caballito()
moto1.estado()

print("===================== Generando otro vehículo =====================")

camioneta1 = Camioneta('Toyota', '2011')
camioneta1.arrancar()
camioneta1.estado()
print(camioneta1.carga(True))


