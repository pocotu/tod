'''Se tiene las ventas del mes de octubre de una determinada empresa.
Escribir un algoritmo que determine:
- La venta total del mes
- El día que se tuvo la venta más baja
- El día que se tuvo la venta más alta
- El promedio de ventas por día.
'''
# --- Inicializar contadores y acumuladores
TotalVentasMes = 0
VentaMayor = 0
DiaVentaMayor = 0
VentaMenor = 1000000
DiaVentaMenor=0
for Dia in range(1,32):
    # Leer el importe de la venta total del K-ésimo día
    ImporteDia = int(input('Ingrese el importe de la venta del día '+str(Dia)+': '))
    # Acumular la venta diaria
    TotalVentasMes += ImporteDia
    
    # Verificar si venta del día es la mayor
    if ImporteDia > VentaMayor:
        VentaMayor = ImporteDia
        DiaVentaMayor = Dia
    # Verificar si venta del día es menor
    if ImporteDia < VentaMenor:
        VentaMenor = ImporteDia
        DiaVentaMenor = Dia
# Mostrar los resultados
print('Total de ventas del mes: ', TotalVentasMes)
print('Se vendió más el día ', DiaVentaMayor,'Venta = ',VentaMayor)
print('Se vendió menos el día ', DiaVentaMenor,'Venta = ',VentaMenor)
print('Promedio Venta = ', TotalVentasMes/31)

