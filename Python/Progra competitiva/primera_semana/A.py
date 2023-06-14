'''
Takahashi está jugando un juego.
En este juego, cada vez que el número de monedas que has recogido 
hasta el momento se convierte en un múltiplo de 100, obtienes un premio.

Takahashi ha recolectado XX monedas hasta ahora. ¿Cuántas monedas 
más necesita recolectar antes de obtener el próximo premio? 
(Si XX es un múltiplo de 100, asumimos que ya 
obtuvo el premio por recolectar XX monedas en total).

limites: 0 ≤ X ≤ 100000
'''

def premio(X):
    while 0 <X < 100000:
        # si el modulo de X entre 100 es igual a 0 entonces es multiplo de 100
        if X % 100 == 0:
            print("Ya obtuvo el premio")
            return 100
        else:
            # si no es multiplo de 100 entonces se le resta el modulo de X entre 100
            print("Faltan", 100 - X % 100, "monedas para el premio")
            return 100 - X % 100

def main():
    x = int(input("Ingrese el numero de monedas: "))
    premio(x)

main()