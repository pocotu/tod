'''
Sistema de prestamo frances
Anualidad

cuota = Ci/(1-(1+i)^n)

Donde:
cuota: cuota periódica constante
Ci: capital inicial
i: tasa de interés anual
n: número de periodos


Ik = C(k-1) - i
Ck = a - Ik 

Donde:
Ik: Interés del periodo k
Ck: Capital del anio, anio que se hace el calculo
C(k-1): Capital del periodo anterior (k-1)
'''

import numpy as np


#def Sistema_Frances(Co, i, n):
#
#    def anualidad_francesa(Co, i, n):
#        a = Co*((i)/(1-((1+i)**-n)))
#        return a
#    
#    def interes_total_de_un_periodo(Ck, i):
#        Ik = Ck*i
#        return Ik
#    
#    def capital_de_un_periodo(Ck, Ik):
#        Ck = Ck - Ik
#        return Ck
#    
#    a = anualidad_francesa(Co, i, n)
#    print("La anualidad es de: ", a)
#
#
#
#    # ingresando datos
#    Co = float(input("ingrese el capital prestado : "))
#    i = float(input("ingrese la tasa de interes anual : "))
#    n = int(input("ingrese el numero de periodos : "))
#
#    # cuadro de amortizacion con, anio(k), anualidad(a(Co*((i)/(1-((1+i)^-n))))), amortizacion capital(A(a-Ik)), 
#    # interes(Ik(Ck-1*I)), capital amortizado(Ck(suma(Ak))), capital restante(mk(ck-ck-1))
#
#    # impresion de cuadro de amortizacion con anio, anualidad, amortizacion capital, interes, capital amortizado, capital restante
#    # usando


def main():
    print("ingrese los datos del prestamo")
    prestamo = float(input("prestamo : "))
    interes = float(input("interes : "))
    interes = interes/100
    anios = int(input("anios : "))
    cuotas = int(input("cuotas : "))
    periodo = anios*cuotas
    anualidad = prestamo*((interes)/(1-((1+interes)**(-periodo))))
    print("la anualidad es de : " + str(anualidad))
    print("el cuadro de amortizacion es el siguiente : ")
    print("periodo\tcapital\tinteres\tcuota\tcapital restante")
    capital = prestamo
    for i in range(periodo):
        interes = capital*interes
        cuota = anualidad - interes
        capital = capital - cuota
        print(str(i+1) + "\t" + str(round(cuota,2)) + "\t" + str(round(interes,2)) + "\t" + str(round(anualidad,2)) + "\t" + str(round(capital,2)))

main()




#    # crear un dataframe para guardar los datos
#    plan = pd.DataFrame(columns=['Cuota','Interes','Amort.','Capital'])
#    # guardar el capital inicial
#    plan.loc[0,'Capital']= capital
#    plan.loc[0,'Cuota']= 0
#    plan.loc[0,'Interes']= 0
#    plan.loc[0,'Amort.']= 0
#
#    # calcular los datos de cada cuota
#    for t in range(1,periodo+1):
#        # guardar la cuota
#        plan.loc[t,'Cuota']= cuota
#        plan.loc[t,'Interes']= round(float(plan.loc[t-1,'Capital']*(tipo/(100*anio))),2)
#        plan.loc[t,'Amort.']= (plan.loc[t,'Cuota']-plan.loc[t,'Interes'])
#        plan.loc[t,'Capital']= plan.loc[t-1,'Capital']-plan.loc[t,'Amort.']
#
#    print(plan)
#    # imprimir el total de intereses
#    print('\nTotal intereses :',round(float(plan['Interes'].sum()),2))