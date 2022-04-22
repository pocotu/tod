# ---- Modulos ----

# PREGUNTA 1
# Modulo para contar cuantos tienen 1 vacuna
def UnaVacuna(Lista):
    Contador1 = 0 # incializar contador
    for i in Lista:
        # Si la posicion 5 es igual a 1 
        if i[5] == 1:
            Contador1 += 1
    return Contador1

# PREGUNTA 2
# Modulo para determinar el mayor o igual a 65 sin 3 vacunas
def MayorIgual65(Lista):
    Contador2 = 0 # Inicializar contador
    for i in Lista:
        # Si la posicion 4 es mayor igual a 65 y la posicion 5 es menor que 3 
        if i[4]>=65 and i[5]<3:
            Contador2 += 1
    return Contador2
        
# ********  PROGRAMA PRINCIPAL   ********
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

# -- Solucion pregunta 1
# Cantidad de personas con 1 vacuna
Alumnos = UnaVacuna(ListaA)
Docentes = UnaVacuna(ListaD)
PersonalAdministrativo = UnaVacuna(ListaP)
TotalUnaVacuna = Alumnos + Docentes + PersonalAdministrativo
print("Personas con 1 vacuna:", TotalUnaVacuna)

# -- Solucion pregunta 2
Docentes = MayorIgual65(ListaD)
PersonalAdministrativo = MayorIgual65(ListaP)
TotalMAyorIgual65 = Docentes + PersonalAdministrativo
print("Personas >= 65 sin las 3 vacunas:", TotalMAyorIgual65)