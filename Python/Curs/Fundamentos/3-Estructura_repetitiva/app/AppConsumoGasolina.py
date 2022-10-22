'''
En la universidad se tienen N vehículos; opara cada vehículo se
tiene la cantidad de galones de gasolina consumidos por día.
Escribir un algoritmo que determine el total de galones consumidos
en cada día y por el total de vehículos, en los primeros D
días del mes.
'''

# -- Leer el número de vehículos y el número de días
NroVehiculos = int(input('Ingrese el número de vehículos:'))
NroDias = int(input('Ingrese el número de días del mes:'))
# -- Procesar para cada día del mes
TotalConsumo = 0;
for Dia in range(1,NroDias+1):
    print('Ingrese los consumos para el día',Dia)
    # -- Procesar para cada vehículo
    TotalConsumoDia = 0
    for Vehiculo in range(1, NroVehiculos+1):
        # -- Leer el consumo de gasolina por cada carro y día        
        Consumo = int(input('Cosumo del vehículo '+str(Vehiculo)+':'))
        # -- Acumular consumo por día
        TotalConsumoDia += Consumo
    # -- Mostrar el consumo del día
    print('El día ', Dia,' se ha consumido ', TotalConsumoDia, 'galones')
    # -- Acumular consumo total de vehiculo
    TotalConsumo += TotalConsumoDia
# -- Mostrar consumo total
print('En total se han consumido ', TotalConsumo, 'galones')                      
    
