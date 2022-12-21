'''
Tres chicos juegan un juego: cada persona escribe nn palabras distintas de
longitud 3. Luego, suman el numero de puntos de la siguiente manera:
si una palabra fue escrita por una persona, esa persona obtiene 3 puntos,
si una palabra fue escrita por dos personas, cada una de las dos obtiene 1
punto,
si una palabra fue escrita por todos, nadie obtiene puntos.
Al final, ¿cuantos puntos tiene cada jugador?
'''

# cada persona escribe nn palabras distintas de longitud 3.
def Entrada_palabras():
    palabras = []
    # recorre del 1 al 3 y lo agrega a la lista palabras
    for i in range(3):
        palabras.append(input("Ingrese una palabra: "))
    return palabras

# si una palabra fue escrita por una persona, esa persona obtiene 3 puntos
def tres_puntos(palabras):
    puntos = 0
    for i in palabras:
        # si 
        if palabras.count(i) == 1:
            puntos += 3
            print(puntos)
    return puntos

# si una palabra fue escrita por dos personas, cada una de las dos obtiene 1 punto
def un_punto(palabras):
    puntos = 0
    for i in palabras:
        if palabras.count(i) == 2:
            puntos += 1
            print(puntos)
    return puntos

# si una palabra fue escrita por todos, nadie obtiene puntos
def cero_puntos(palabras):
    puntos = 0
    for i in palabras:
        if palabras.count(i) == 3:
            puntos += 0
            print(puntos)
    return puntos

def main():
    # cada persona escribe nn palabras distintas de longitud 3.
    print("##### Judador 1 #####")
    palabras1 = Entrada_palabras()
    print()
    print("##### Jugador 2 #####")
    palabras2 = Entrada_palabras()
    print()
    print("##### Judador 3 #####")
    palabras3 = Entrada_palabras()
    print()
    
    puntos1 = tres_puntos(palabras1) + un_punto(palabras1) +  cero_puntos(palabras1)
    puntos2 = tres_puntos(palabras2) + un_punto(palabras2) +  cero_puntos(palabras2)
    puntos3 = tres_puntos(palabras3) + un_punto(palabras3) +  cero_puntos(palabras3)
    
    print(f"El jugador 1 obtuvo {puntos1} puntos")
    print(f"El jugador 2 obtuvo {puntos2} puntos")
    print(f"El jugador 3 obtuvo {puntos3} puntos")

main()
