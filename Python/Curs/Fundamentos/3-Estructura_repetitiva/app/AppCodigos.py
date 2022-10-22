'''
En la empresa alfa, se codificó a los N empleados con números de 4 dígitos.
El código es válido si por lo menos hay dos dígitos primos.
Escribir un algoritmo que determine el procentaje de los códigos válidos.
'''
# -- Leer Nro de Empleados
N = int(input('Ingresa Nro. de Empleados: '))
while (N<0):
    N = int(input('ERROR ... N > 0: '))
# --- Buscar en los números de tres dígitos
CodigosValidos = 0
for K in range(1,N+1):
    # --- Ingresa Codigo del Empleado
    Codigo = int(input('Ingresa Codigo del Empleado '+str(K)+': '))
    # --- Descomponer Codigo en digitos
    D1 = Codigo //1000
    D2 = (Codigo % 1000) // 100
    D3 = (Codigo % 100)// 10
    D4 = Codigo % 10
    # --- Determinar Si los digitos son primos o no
    NroDigitosPrimos= 0
    if ((D1 == 2) or (D1 == 3) or(D1 ==5) or (D1 == 7)):
        NroDigitosPrimos +=1
    if ((D2 == 2) or (D2 == 3) or(D2 ==5) or (D2 == 7)):
        NroDigitosPrimos +=1
    if ((D3 == 2) or (D3 == 3) or(D3 ==5) or (D3 == 7)):
        NroDigitosPrimos +=1
    if ((D4 == 2) or (D4 == 3) or(D4 ==5) or (D4 == 7)):
        NroDigitosPrimos +=1
    # --- Determinar si tiene el número de dígitos primos para ser considerado válido
    if  (NroDigitosPrimos >=2):
        CodigosValidos+=1
# --- Determinar Porcentaje de codigos validos
print('Codigo Validos = ',CodigosValidos)
Porcentaje = CodigosValidos/N *100
# --- Mostrar Porcentaje de Codigos Validos
print('Porcentaje Codigos Validos = ',Porcentaje)
    
