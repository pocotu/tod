"""
Una empresa comercial ofrece dos tipos de descuentos:
- 10% si el importe de la venta es mayor o igual a s/ 200.00
- 5% si el importe de la venta es menor a 200.00
Escribir un algoritmo que lea el numero de unidades vendidas
y el precio unitario, luego que calcule el importe de la venta neta
"""
# Leer precio unitario y nro. unidades
PrecioUnitario = float(input('ingresa precio unitario: '))
NroUnidades = float(input('Ingresa nro. unidades: '))

# Calcular venta bruta
VentaBruta = PrecioUnitario*NroUnidades

#Calcular descuento
if VentaBruta >= 200:
    # Aplicar 10% de descuento
    Descuento = VentaBruta*0.10
else:
    # Aplicar 5% de descuento
    Descuento = VentaBruta*0.05

# Calcular venta neta
VentaNeta = VentaBruta - Descuento

# Mostrar resultado
print('Venta Neta =',VentaNeta)