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

# Relación de egresados de una determinada Especialidad
def relacionEgresados(cEgresado, Especialidad):
    for i in range(len(cEgresado)):
        if cEgresado[i].aEspecialidad == Especialidad:
            return cEgresado[i].aNombres + " " + cEgresado[i].aAP + " " + cEgresado[i].aAM

# Objetos de la clase cEgresado
cEgresado = [cEgresado(1, 'Perez', 'Zarate', 'Carlos', 'Inteligencia Articicial', 'Extranjero', 'Mexico'),
            cEgresado(2, 'Puma', 'Cano', 'Diana', 'Ciberseguridad', 'Extranjero', 'Brazil'), 
            cEgresado(3, 'Huillca', 'Lozano', 'David', 'Ingeniero de software', 'Extranjero', 'Mexico'), 
            cEgresado(4, 'Zegarra', 'Meza', 'Diego', 'Inteligencia Artificial', 'Local', 'Peru'), 
            cEgresado(5, 'Gonzales', 'Gonzalez', 'Eduardo', 'Ingeniero de software', 'Local', 'Peru')]

# 1 Imprimir egresados que trabajan en el extranjero
print('Egresados que trabajan en el extranjero: {}'.format(cuantosExtranjeros(cEgresado)))

# 2 Imprimir relacion de egresados de una especialidad ingresada
print('''1. Inteligencia articial
2. Ciberseguridad
3. Ingeniero de software''')
Especialidad = input('Ingrese la especialidad: ')

lista = []
if Especialidad == '1':
    for i in range(len(cEgresado)):
        if cEgresado[i].aEspecialidad == 'Inteligencia Articicial':
            lista.append(cEgresado[i].aNombres + " " + cEgresado[i].aAP + " " + cEgresado[i].aAM)
    print(lista)
elif Especialidad == '2':
    for i in range(len(cEgresado)):
        if cEgresado[i].aEspecialidad == 'Ciberseguridad':
            lista.append(cEgresado[i].aNombres + " " + cEgresado[i].aAP + " " + cEgresado[i].aAM)
    print('Egresados de Ciberseguridad: {}'.format(lista))
elif Especialidad == '3':
    for i in range(len(cEgresado)):
        if cEgresado[i].aEspecialidad == 'Ingeniero de software':
            lista.append(cEgresado[i].aNombres + " " + cEgresado[i].aAP + " " + cEgresado[i].aAM)
    print('Egresados de Ingeniero de software: {}'.format(lista))
else:
    print('Especialidad no encontrada')


