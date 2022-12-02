# sistema de amortizacion aleman

import pandas as pd

def Sistema_aleman():
    # ingresando datos
    capital = float(input("ingrese el capital prestado : "))
    tipo = float(input("ingrese la tasa de interes anual : "))
    periodo = int(input("ingrese el numero de periodos : "))
    anio = int(input("ingrese el numero de pagos por año : "))
    # formula de la cuota del prestamo sistema aleman
    amortizacion = round(capital/periodo, 2)

    print(    'Plan de Amortización Aleman')
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
        plan.loc[t, 'Interes'] = round(plan.loc[t-1, 'Capital Restante'] * (tipo/(anio*100)),2)
        # anualidad = amortizacion + interes
        plan.loc[t, 'Anualidad'] = plan.loc[t, 'Amortizacion'] + plan.loc[t, 'Interes']
        # capital amortizado = sumatoria(amortizacion * periodo)
        plan.loc[t, 'Capital Amortizado'] = plan.loc[t-1, 'Capital Amortizado'] + plan.loc[t, 'Amortizacion']
        # capital restante = capital amortizado - capital amortizado - 1
        plan.loc[t, 'Capital Restante'] = capital - plan.loc[t, 'Capital Amortizado']

    print(plan)

    # imprimir el total de intereses mas el capital prestado
    print('\nTotal de intereses: ', round(float(plan['Interes'].sum()),2))

Sistema_aleman()



