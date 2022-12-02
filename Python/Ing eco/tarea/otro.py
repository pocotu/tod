# sistema de amortizacion americano

import pandas as pd

def Sistema_americano():
    # ingresando datos
    capital = float(input("ingrese el capital prestado : "))
    tipo = float(input("ingrese la tasa de interes anual : "))
    periodo = int(input("ingrese el numero de periodos : "))
    anio = int(input("ingrese el numero de pagos por año : "))

    cuota = round(capital * (tipo/(anio*100)), 2)
    print(    'Plan de Amortización Americano')

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
        plan.loc[t, 'Interes'] = round(plan.loc[t-1, 'Capital Restante'] * (tipo/(anio*100)),2)
        # amortizacion capital = cuota - tipo
        plan.loc[t, 'Amortizacion'] = cuota - plan.loc[t, 'Interes']
        # capital amortizado = sumatoria(amortizacion capital * periodo)
        plan.loc[t, 'Capital Amortizado'] = plan.loc[t-1, 'Capital Amortizado'] + plan.loc[t, 'Amortizacion']
        # capital restante = capital amortizado - capital amortizado - 1
        plan.loc[t, 'Capital Restante'] = capital - plan.loc[t, 'Capital Amortizado']
    
    print(plan)

    # imprimir el total de intereses mas el capital prestado
    print('\nTotal de intereses: ', round(float(plan['Interes'].sum()),2) + capital)

Sistema_americano()