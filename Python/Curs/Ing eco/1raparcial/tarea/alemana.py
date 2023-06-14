'''
crear una funcion para el sistema de amortizacion alemana
'''

def amortizacion_alemana(capital, interes, plazo):
    # se calcula el interes
    interes = interes / 100
    # se calcula el interes mensual
    interes_mensual = interes / 12
    # se calcula el interes acumulado
    interes_acumulado = interes_mensual * capital
    # se calcula el capital acumulado
    capital_acumulado = capital - interes_acumulado
    # se calcula el interes acumulado
    interes_acumulado = interes_acumulado * plazo
    # se calcula el capital acumulado
    capital_acumulado = capital_acumulado * plazo
    # se calcula el pago mensual
    pago_mensual = interes_acumulado + capital_acumulado
    # se imprime el pago mensual
    print("Pago mensual: ", pago_mensual)

def main():
    # se pide el capital
    capital = float(input("Capital: "))
    # se pide el interes
    interes = float(input("Interes: "))
    # se pide el plazo
    plazo = int(input("Plazo: "))
    # se llama a la funcion
    amortizacion_alemana(capital, interes, plazo)

main()
