"""
Un ciclista parte de la plaza de armas a las HH horas, MM minutos y SS segundos. 
El tiempo que dura el viaje hasta llegar a la UNSAAC es de T segundos. 
Escribir un algoritmo que determine la hora de llegada a la UNSAAC
"""

# Leer hora de partida en HH:MM:SS
HoraPartida =int(input("Ingrese hora de partida: "))
MinPartida = int(input("Ingrese minuto partida: "))
SegPartida = int(input("Ingrese segundos de partida: "))

# Leer tiempo de viaje en SS
TiempoViaje = int(input("Ingrese tiempo de viaje: "))

# Convertir la Hora de partida en segundo
TotalSegPartida = HoraPartida*3600+MinPartida*60+SegPartida
TotalSeg = TotalSegPartida + TiempoViaje

# Determinar la hora de llegada
HoraLlegada = (TotalSeg // 3600) % 24
MinLlegada = (TotalSeg % 3600) // 60
SegLlegada = TotalSeg % 60

# Mostrar hora de llegada
print(f"Hora llegada = {HoraLlegada}:{MinLlegada}:{SegLlegada}")
