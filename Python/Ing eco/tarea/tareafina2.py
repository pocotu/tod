import pandas as pd
# ESTUDIANTES:
# LLASA YUCRA , RUTH MARGOT
# HUAYLLA HUILLCA, ROSSBEL
# SISTEMA DE AMORTIZACION FRANCES

def Sistema_frances():
    print("_________________________________________________")
    print("__________Sistema de Amortización Frances _______\n")
    capital = float(input("Capital prestado : "))
    interes = float(input("La tasa de interes : "))
    periodo = int(input("El numero de periodos : "))
    anio = int(input("El numero de pagos por año : "))
    # formula de la cuota del prestamo sistema frances
    cuota= round(capital*((interes/(anio*100))/(1-(1+(interes/(anio*100)))**(-1*periodo))),2)
    print()
    print('>>>Plan de Amortización Frances<<<')
    print()

    # crear un dataframe para almacenar los datos
    plan = pd.DataFrame(columns=['Cuota', 'Interes', 'Amortizacion', 'Capital Amortizado', 'Capital Restante'])
    
    # calcular los datos de cada cuota
    plan.loc[0, 'Cuota'] = 0
    plan.loc[0, 'Interes'] = 0
    plan.loc[0, 'Amortizacion'] = 0
    plan.loc[0, 'Capital Amortizado'] = 0
    plan.loc[0, 'Capital Restante'] = capital

    # calcular los datos de cada cuota
    for t in range(1, periodo+1):
        # anualidad = cuota
        plan.loc[t, 'Cuota'] = cuota
        # interes = capital * 
        plan.loc[t, 'Interes'] = round(plan.loc[t-1, 'Capital Restante'] * (interes/(anio*100)),2)
        plan.loc[t, 'Amortizacion'] = cuota - plan.loc[t, 'Interes']
        plan.loc[t, 'Capital Amortizado'] = plan.loc[t-1, 'Capital Amortizado'] + plan.loc[t, 'Amortizacion']
        plan.loc[t, 'Capital Restante'] = capital - plan.loc[t, 'Capital Amortizado']
    print(plan)
    print('\nTotal de Cuotas: ', round(float(plan['Cuota'].sum()),2))
    print('\nTotal de intereses: ', round(float(plan['Interes'].sum()),2))

# SISTEMA DE AMORTIZACION AMERICANO
def Sistema_americano():
    print("_________________________________________________")
    print("________Sistema de Amortización Americano _______\n")
    # ingresando datos
    capital = float(input("Capital prestado : "))
    interes = float(input("La tasa de interes : "))
    periodo = int(input("El numero de periodos : "))
    anio = int(input("El numero de pagos por año : "))

    cuota = round(capital * (interes/(anio*100)), 2)
    print()
    print('>>>Plan de Amortización Americano<<<')
    print()

    plan = pd.DataFrame(columns=['Cuotas', 'Interes', 'Amortizacion', 'Capital Amortizado', 'Capital Restante'])

    plan.loc[0, 'Cuotas'] = 0
    plan.loc[0, 'Interes'] = 0
    plan.loc[0, 'Amortizacion'] = 0
    plan.loc[0, 'Capital Amortizado'] = 0
    plan.loc[0, 'Capital Restante'] = capital

    # calcular los datos de cada cuota
    for t in range(1, periodo+1):
        # anualidad = capital * tipo, si es la ultima cuota se suma el capital restante
        plan.loc[t, 'Cuotas'] = cuota if t < periodo else cuota + plan.loc[t-1, 'Capital Restante']
        # interes = capital * tipo
        plan.loc[t, 'Interes'] = round(plan.loc[t-1, 'Capital Restante'] * (interes/(anio*100)),2)
        # amortizacion capital = cuota - tipo
        plan.loc[t, 'Amortizacion'] = cuota - plan.loc[t, 'Interes']
        # capital amortizado = sumatoria(amortizacion capital * periodo)
        plan.loc[t, 'Capital Amortizado'] = plan.loc[t-1, 'Capital Amortizado'] + plan.loc[t, 'Amortizacion']
        # capital restante = capital amortizado - capital amortizado - 1
        plan.loc[t, 'Capital Restante'] = capital - plan.loc[t, 'Capital Amortizado']
    
    print(plan)

    # imprimir el total de intereses mas el capital prestado
    print('\nTotal de Cuotas: ', round(float(plan['Cuotas'].sum()),2))
    print('\nTotal de intereses: ', round(float(plan['Interes'].sum()),2))



# SISTEMA DE AMORTIZACION ALEMAN
def Sistema_aleman():
    print("_________________________________________________")
    print("__________Sistema de Amortización Aleman ________\n")
    # ingresando datos
    capital = float(input("Capital prestado : "))
    interes = float(input("La tasa de interes : "))
    periodo = int(input("El numero de periodos : "))
    anio = int(input("El numero de pagos por año : "))
    # formula de la cuota del prestamo sistema aleman
    amortizacion = round(capital/periodo, 2)

    print()
    print('>>>Plan de Amortización Aleman<<<')
    print()
    plan = pd.DataFrame(columns=['Cuotas', 'Interes','Amortizacion', 'Capital Amortizado', 'Capital Restante'])

    plan.loc[0, 'Cuotas'] = 0
    plan.loc[0, 'Interes'] = 0
    plan.loc[0, 'Amortizacion'] = 0
    plan.loc[0, 'Capital Amortizado'] = 0
    plan.loc[0, 'Capital Restante'] = capital

    # calcular los datos de cada cuota
    for t in range(1, periodo+1):
        # amortizacion = capital / periodo
        plan.loc[t, 'Amortizacion'] = amortizacion
        # interes = (capital * tipo) / periodo
        plan.loc[t, 'Interes'] = round(plan.loc[t-1, 'Capital Restante'] * (interes/(anio*100)),2)
        # anualidad = amortizacion + interes
        plan.loc[t, 'Cuotas'] = plan.loc[t, 'Amortizacion'] + plan.loc[t, 'Interes']
        # capital amortizado = sumatoria(amortizacion * periodo)
        plan.loc[t, 'Capital Amortizado'] = plan.loc[t-1, 'Capital Amortizado'] + plan.loc[t, 'Amortizacion']
        # capital restante = capital amortizado - capital amortizado - 1
        plan.loc[t, 'Capital Restante'] = capital - plan.loc[t, 'Capital Amortizado']

    print(plan)

    # imprimir el total de intereses mas el capital prestado
    print('\nTotal de Cuotas: ', round(float(plan['Cuotas'].sum()),2))
    print('\nTotal de intereses: ', round(float(plan['Interes'].sum()),2))

    
def Menu():
    print()
    print("                INICIO                   ")
    print("*****************************************")
    print("1. >>> Sistema de Amortización Frances")
    print("2. >>> Sistema de Amortización Americano")
    print("3. >>> Sistema de Amortización Aleman")
    print("4. >>> Salir ")
    print("*****************************************")

print(Menu)
Menu()
opcion = int(input("Ingrese una opcion: "))
while opcion != 4:
    if opcion == 1:
        Sistema_frances()
    elif opcion == 2:
        Sistema_americano()
    elif opcion == 3:
        Sistema_aleman()
    else:
        print("OPCION NO VALIDA")
    Menu()
    opcion = int(input("Ingrese una opcion: "))
print("Fin del programa")


