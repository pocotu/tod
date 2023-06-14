import pandas as pd

# SISTEMA DE AMORTIZACION FRANCES
def Sistema_frances():
    print("###### Sistema de Amortización Frances ######\n")
    capital = float(input("Capital prestado : "))
    interes = float(input("La tasa de interes anual : "))
    periodo = int(input("El numero de periodos : "))
    anio = int(input("El numero de pagos por año : "))
    # formula de la cuota del prestamo sistema frances
    cuota= round(capital*((interes/(anio*100))/(1-(1+(interes/(anio*100)))**(-1*periodo))),2)
    print('Plan de Amortización Frances')

    # crear un dataframe para almacenar los datos
    plan = pd.DataFrame(columns=['Anualidad', 'Amortizacion', 'Interes', 'Capital Amortizado', 'Capital Restante'])
    
    # calcular los datos de cada cuota
    plan.loc[0, 'Anualidad'] = 0
    plan.loc[0, 'Amortizacion'] = 0
    plan.loc[0, 'Interes'] = 0
    plan.loc[0, 'Capital Amortizado'] = 0
    plan.loc[0, 'Capital Restante'] = capital

    # calcular los datos de cada cuota
    for t in range(1, periodo+1):
        # anualidad = cuota
        plan.loc[t, 'Anualidad'] = cuota
        # interes = capital * interes
        plan.loc[t, 'Interes'] = round(plan.loc[t-1, 'Capital Restante'] * (interes/(anio*100)),2)
        # amortizacion capital = cuota - interes
        plan.loc[t, 'Amortizacion'] = cuota - plan.loc[t, 'Interes']
        # capital amortizado = sumatoria(amortizacion capital * periodo)
        plan.loc[t, 'Capital Amortizado'] = plan.loc[t-1, 'Capital Amortizado'] + plan.loc[t, 'Amortizacion']
        # capital restante = capital amortizado - capital amortizado-1
        plan.loc[t, 'Capital Restante'] = capital - plan.loc[t, 'Capital Amortizado']
    print(plan)
    
    print('\nTotal de intereses: ', round(float(plan['Interes'].sum()),2))

# SISTEMA DE AMORTIZACION AMERICANO
def Sistema_americano():
    print("###### Sistema de Amortización Americano ######\n")
    # ingresando datos
    capital = float(input("Capital prestado : "))
    interes = float(input("La tasa de interes anual : "))
    periodo = int(input("El numero de periodos : "))
    anio = int(input("El numero de pagos por año : "))

    # formula de la cuota del prestamo sistema americano
    cuota = round(capital * (interes/(anio*100)), 2)
    print('Plan de Amortización Americano')

    plan = pd.DataFrame(columns=['Anualidad', 'Interes', 'Amortizacion', 'Capital Amortizado', 'Capital Restante'])

    plan.loc[0, 'Anualidad'] = 0
    plan.loc[0, 'Interes'] = 0
    plan.loc[0, 'Amortizacion'] = 0
    plan.loc[0, 'Capital Amortizado'] = 0
    plan.loc[0, 'Capital Restante'] = capital

    # calcular los datos de cada cuota
    for t in range(1, periodo+1):
        # anualidad = capital * tipo, si es la ultima cuota se suma el capital restante
        plan.loc[t, 'Anualidad'] = cuota if t < periodo else cuota + plan.loc[t-1, 'Capital Restante']
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
    print('\nTotal de intereses: ', round(float(plan['Interes'].sum()),2) + capital)


# SISTEMA DE AMORTIZACION ALEMAN
def Sistema_aleman():
    print("###### Sistema de Amortización Aleman ######\n")
    # ingresando datos
    capital = float(input("Capital prestado : "))
    interes = float(input("La tasa de interes anual : "))
    periodo = int(input("El numero de periodos : "))
    anio = int(input("El numero de pagos por año : "))

    # formula de la amortizacion alemana
    amortizacion = round(capital/periodo, 2)

    print('Plan de Amortización Aleman')
    plan = pd.DataFrame(columns=['Amortizacion', 'Interes', 'Anualidad', 'Capital Amortizado', 'Capital Restante'])

    plan.loc[0, 'Amortizacion'] = 0
    plan.loc[0, 'Interes'] = 0
    plan.loc[0, 'Anualidad'] = 0
    plan.loc[0, 'Capital Amortizado'] = 0
    plan.loc[0, 'Capital Restante'] = capital

    # calcular los datos de cada cuota
    for t in range(1, periodo+1):
        # amortizacion = capital / periodo
        plan.loc[t, 'Amortizacion'] = amortizacion
        # interes = (capital * tipo) / periodo
        plan.loc[t, 'Interes'] = round(plan.loc[t-1, 'Capital Restante'] * (interes/(anio*100)),2)
        # anualidad = amortizacion + interes
        plan.loc[t, 'Anualidad'] = plan.loc[t, 'Amortizacion'] + plan.loc[t, 'Interes']
        # capital amortizado = sumatoria(amortizacion * periodo)
        plan.loc[t, 'Capital Amortizado'] = plan.loc[t-1, 'Capital Amortizado'] + plan.loc[t, 'Amortizacion']
        # capital restante = capital amortizado - capital amortizado - 1
        plan.loc[t, 'Capital Restante'] = capital - plan.loc[t, 'Capital Amortizado']
    print(plan)

    # imprimir el total de intereses mas el capital prestado
    print('\nTotal de intereses: ', round(float(plan['Interes'].sum()),2))


# MENU PRINCIPAL
def menu():
    print("1. Sistema de Amortización Frances")
    print("2. Sistema de Amortización Americano")
    print("3. Sistema de Amortización Aleman")
    print("4. Salir")
    opcion = int(input("Seleccione una opcion: "))
    print()
    if opcion == 1:
        Sistema_frances()
    elif opcion == 2:
        Sistema_americano()
    elif opcion == 3:
        Sistema_aleman()
    elif opcion == 4:
        print("Gracias por utilizar el programa")
        exit()
    else:
        print("Opcion invalida")
        menu()

menu()
