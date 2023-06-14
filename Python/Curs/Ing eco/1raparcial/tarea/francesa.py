import pandas as pd

def prestamo_frances():
    capital = int(input('Capital : '))
    tipo = float(input('Tasa interes anual: '))
    periodo = int(input('Num. pagos: '))
    anio = int(input('Pagos por año: '))
    # formula de la cuota del prestamo sistema frances
    cuota= round(capital*((tipo/(anio*100))/(1-(1+(tipo/(anio*100)))**(-1*periodo))),2)
    print(    'Plan de pagos')


    plan = pd.DataFrame(columns=['Anualidad', 'Amortizacion', 'Interes', 'Capital Amortizado', 'Capital Restante'])
    
    plan.loc[0, 'Anualidad'] = 0
    plan.loc[0, 'Amortizacion'] = 0
    plan.loc[0, 'Interes'] = 0
    plan.loc[0, 'Capital Amortizado'] = 0
    plan.loc[0, 'Capital Restante'] = capital


    # calcular los datos de cada cuota
    for t in range(1, periodo+1):
        plan.loc[t, 'Anualidad'] = cuota
        plan.loc[t, 'Interes'] = round(plan.loc[t-1, 'Capital Restante'] * (tipo/(anio*100)),2)
        plan.loc[t, 'Amortizacion'] = cuota - plan.loc[t, 'Interes']
        plan.loc[t, 'Capital Amortizado'] = plan.loc[t-1, 'Capital Amortizado'] + plan.loc[t, 'Amortizacion']
        plan.loc[t, 'Capital Restante'] = capital - plan.loc[t, 'Capital Amortizado']
    print(plan)
    
    print('\nTotal de intereses: ', round(float(plan['Interes'].sum()),2))


prestamo_frances()
