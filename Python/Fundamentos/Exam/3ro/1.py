'''
La Universidad en la intención de activar las clases presenciales en el
próximo semestre, realizó un empadronamiento de los Alumnos, Docentes y
Personal Administrativo. Para este propósito solicitó, tanto a los alumnos,
docentes y personal administrativo su respectivo certificado de vacunación
contra el COVID-19. El área de informática automatizó este proceso;
para lo cual, en tres listas se registró datos del certificado de
vacuna (DNI, AP, AM, Nombres, Edad y NroVacunas) correspondientes a alumnos,
docentes y personal administrativo.

A Ud. Se le pide escribir módulos para:

1.- Determinar cuántos alumnos, docentes y personal administrativo tienen
    una vacuna.
    
2.- Determinar cuántos docentes y personal administrativo mayores de 65 años
    no tienen las tres dosis.
'''
# Modulos

# Modulo contador Alumnos, Docentes y personal administrativo
def Contador():
    contadorA = 0 # contador de alumnos
    for i in  ListaA:
        contadorA += 1

    contadorD = 0 # contador de docentes
    for i in ListaD:
        contadorD += 1
    
    contadorP = 0 # contador de personal administrativo
    for i in ListaP:
        contadorP += 1

    return contadorA, contadorD, contadorP



# ***  PROGRAMA PRINCIPAL   ***

ListaA = [['40567832','PFUÑO','SOLÍS','ZOILA', 21, 2],
          ['62457810','ARCE','ANDÍA','ABEL', 19, 1],
          ['72474588','OLIVERA','CANO','ANA MARIA', 19, 2],
          ['74121014','APAZA','YEPEZ','MARTHA', 20, 1]]

ListaD = [['23567832','CRUZ','MENDOZA','EMILIO', 45, 1],
          ['23457810','PEREZ','CANDIA','ANGEL', 65, 2],
          ['24232122','QUISPE','MAMANI','MARCELO', 35, 2],
          ['22345678','PAREDES','OTAZU','MAMERTO', 66, 1],
          ['24567890','CONDORI','CHAVEZ','FERNANDO', 68, 3]]

ListaP = [['23456732','CARRASCO','MAMANI','DORIS', 55, 2],
          ['23147810','SANDRO','PUMA','ROLANDO', 66, 3]]


# PREGUNTA 1
Alumnos, Docentes, PersonalAdministrativo = Contador()

def UnaVacuna():

    

    Conta = 0
    Contando = []

    for i in range(len(ListaA)):

        if ListaA[i] == '1':
            Contando.append('1')
        
    return Conta
    
print(UnaVacuna())
# PREGUNTA 2

print(type(ListaA))