'''
Tres hermanos constituyen una empresa, al primero hermano le corresponde el 50% de las acciones, 
al segundo hermano le corresponde una cantidad equivalente a las 2/3 partes de las acciones 
del primer hermano. El resto de las acciones pertenecen al tercer hermano. 
Al final de cada mes se debe repartir las utilidades generadas por la empresa 
en forma proporcional a las acciones de cada hermano. Escribir un algoritmo que determine
el monto correspondiente a cada hermano.
'''

# Leer utilidad de la empresa
Utilidad = float(input('Ingrese la utilidad del mes de la emprese: '))

# Calcular la utilidad de cada hermano segun la proporsion
Her1 = Utilidad/2
Her2 = 2/3*1/2*Utilidad
Her3 = Utilidad - Her1 - Her2

# Mostrar utilidad de cada hermano
print('Utilidad del 1er hermano:',Her1)
print('Utilidad del 2do hermano:',Her2)
print('Utilidad del 3er hermano:', Her3)