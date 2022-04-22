'''
En el  ultimo concurso de programacion, el equipo ganador resolvio 
5 preguntas, para cada pregunta se tiene el tiempo empleado en resolver 
en HH:MM:SS. Escribir un programa modular que termine el tiempo total 
empleado por el equipo ganador.
'''

from Libreria import *
# --- Modulo Leer Tiempo
def LeerTiempo(Texto):
    print(Texto)
    H = LeerNroEntero('Ingresa Hora: ',0,23)
    M = LeerNroEntero('Ingresa Minuto: ',0,59)
    S = LeerNroEntero('Ingresa Segundo: ',0,59)
    return H,M,S
# --- Modulo Tiempo a Segundos
def TiempoASegundos(H,M,S):
    return H*3600+M*60+S

# --- Modulo para convertir segundos a HH:MM:SS
def SegundosATiempo(TotalSegundos):
    HH = TotalSegundos //3600
    MM = (TotalSegundos %3600)//60
    SS = TotalSegundos % 60
    return HH,MM,SS

# ---- Programa Principal
# --- Leer Los Tiempos
HH1,MM1,SS1 = LeerTiempo('Ingresa Tiempo de Primera Pregunta:') 
HH2,MM2,SS2 = LeerTiempo('Ingresa Tiempo de Segunda Pregunta: ')
HH3,MM3,SS3 = LeerTiempo('Ingresa Tiempo de Tercer Pregunta:')
HH4,MM4,SS4 = LeerTiempo('Ingresa Tiempo de Cuarta Pregunta: ')
HH5,MM5,SS5 = LeerTiempo('Ingresa Tiempo de Quinta Pregunta:')

# --- Convertir las HH:MM:SS a Segundos
Segundos1 = TiempoASegundos(HH1,MM1,SS1)
Segundos2 = TiempoASegundos(HH2,MM2,SS2)
Segundos3 = TiempoASegundos(HH3,MM3,SS3)
Segundos4 = TiempoASegundos(HH4,MM4,SS4)
Segundos5 = TiempoASegundos(HH5,MM5,SS5)

TotalSegundos = Segundos1+Segundos2+Segundos3+Segundos4+Segundos5

# --- Convertir los Segundos Totales a HH:MM:SS
HH,MM,SS = SegundosATiempo(TotalSegundos)
# --- Mostrar Tiempo Total
print(f'Tiempo Total = {HH}:{MM}:{SS}')
