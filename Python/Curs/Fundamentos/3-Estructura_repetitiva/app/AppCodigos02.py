'''
En la empresa alfa, se codificó a los N empleados con números de 6 dígitos.
El código es válido si por lo menos hay dos dígitos primos.
Escribir un algoritmo que determine el procentaje de los códigos válidos.
'''
# -- Leer Nro de Empleados
N = int(input('Ingresa Nro. de Empleados: '))
while (N<0):
    N = int(input('ERROR ... N > 0: '))
# --- Buscar en los números los Nros. los dígitos primos
CodigosValidos = 0
for K in range(1,N+1):
    NroDigitosPrimos= 0
    # --- Ingresa Codigo del Empleado
    Codigo = int(input('Ingresa Codigo del Empleado '+str(K)+': '))
    # --- Procesar los dígitos del código
    for I in range(1,7):
        # --- Obtener el último dígito
        UD = Codigo % 10
        Codigo = Codigo // 10
        # -- Verificar si último dígito es primo
        if ((UD == 2) or (UD == 3) or(UD ==5) or (UD == 7)):
            NroDigitosPrimos +=1
    # --- Determinar si tiene el número de dígitos primos para ser considerado válido
    if  (NroDigitosPrimos >=2):
        CodigosValidos+=1
# --- Determinar Porcentaje de codigos validos
print('Codigo Validos = ',CodigosValidos)
Porcentaje = CodigosValidos/N *100
# --- Mostrar Porcentaje de Codigos Validos
print('Porcentaje Codigos Validos = ',Porcentaje)
    
