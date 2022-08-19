'''
Desarrollar una clase de Python para encontrar tres elementos del
arreglo cuya suma sea igual a cero.
ejemplo:
[-25, -10, -7, -3, 2, 4, 8, 10]
Suma uno = [-10, 2, 8]
Suma dos = [-7, -3, 10]
'''
class SumaCero:
    # Constructor de la clase
    def __init__(self, arreglo):
        # atributo de la clase que almacena el arreglo
        self.arreglo = arreglo
        # atributo suma con valor 0
        self.suma = 0
        # atributo resultado con valor vacio     
        self.resultado = []
        # llamado al metodo suma_cero
        self.suma_cero()
        # llamado al metodo imprimir
        self.imprimir()
    
    def suma_cero(self):
        # recorre el arreglo y suma los valores
        for i in self.arreglo:
            # suma el valor de cada elemento del arreglo
            self.suma += i
        self.suma = 0
        # recorre el arreglo nuevamente y busca los valores que suman 0 y los agrega al arreglo resultado
        for i in self.arreglo:
            # suma el valor de cada elemento del arreglo y lo guarda en la variable suma
            self.suma += i
            # si la suma es 0 agrega el valor de la posicion del arreglo al arreglo resultado
            if self.suma == 0:
                self.resultado.append(i)
            # reinicia la suma para que vuelva a buscar los valores que suman 0
            self.suma = 0
    # imprime el arreglo resultado
    def imprimir(self):
        print(self.resultado)

arreglo = [-25, -10, -7, -3, 2, 4, 8, 10]
suma_cero = SumaCero(arreglo)
