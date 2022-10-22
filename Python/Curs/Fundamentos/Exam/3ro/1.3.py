# PREGUNTA 1
#Modulo para contar cuantos tienen 1 vacuna
def UnaVacuna(L):
    #incializar contador
    Cont=0
    for k in L:
        #Si cantidad de vcunas es un
        if k[5]==1:
            #empezar a contabilizar
            Cont+=1
    return Cont
# PREGUNTA 2
#Modulo para determinar mayos de 65 sin 3 vacunas
def Sin3Mayor65(L):
    #inicializar contador
    C=0
    for e in L:
        #Verificar si edad es mayor o igual a 65 y vacuna meor a 3
        if e[4]>=65 and e[5]<3:
            #contabilizar
            C+=1
    return C
        
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

# -- Solución pregunta 1
#Cantidad de personas con 1 vacuna
Al=UnaVacuna(ListaA)
Doc=UnaVacuna(ListaD)
Adm=UnaVacuna(ListaP)
Total=Al+Doc+Adm
print('Respuesta 1: Personas con 1 vacuna: ',Total)

# -- Solución pregunta 2
Docen =Sin3Mayor65(ListaD)
Admi =Sin3Mayor65(ListaP)
Total2 =Docen+Admi
print('Respuesta 2: Personas mayorres o iguales a 65 sin las 3 vacunas: ',Total2)