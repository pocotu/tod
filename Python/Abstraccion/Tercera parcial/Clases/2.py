'''
Desarrolle una clase de Python para poder validar una cadena de paréntesis,
'(', ')', '{', '}', '[' y ']. Estos paréntesis deben cerrarse en el orden correcto, 
por ejemplo: 
"()" y "()[]{}" son válidos, 
pero "[)", "({[)]" y "{{{" no son válidos.
'''

class ValidarParesentesis:
    # Constructor de la clase
    def Validar(self, cadena):
        # atributo de la clase que almacena la cadena
        pila, char = [], {"(": ")", "{": "}", "[": "]"}
        # recorre la cadena
        for parentesis in cadena:
            # si el parentesis es una llave abre la pila y agrega el parentesis a la pila
            if parentesis in char:
                pila.append(parentesis)
            # si el parentesis es una llave cierra la pila y agrega el parentesis a la pila
            elif len(pila) == 0 or char[pila.pop()] != parentesis:
                # si la pila esta vacia o el parentesis de la pila no es igual al parentesis de la cadena imprime que no es valido
                return False
        # si la pila esta vacia imprime que es valido
        return len(pila) == 0

Validar = ValidarParesentesis() # instanciamos
cadena = "()" #cadena a validar
print(Validar.Validar(cadena)) 
cadena = "()[]{}" #cadena a validar
print(Validar.Validar(cadena))
cadena = "[)" #cadena a validar
print(Validar.Validar(cadena)) 
cadena = "({[)]" #cadena a validar
print(Validar.Validar(cadena)) 

#class ValidarCadena:
#    def __init__(self, cadena):
#        self.cadena = cadena
#        self.validar()
#    
#    def validar(self):
#        # arreglo que almacena los paréntesis
#        self.arreglo = ["(", ")", "{", "}", "[", "]"]
#        # arreglo que almacena los paréntesis validos
#        self.arreglo_valido = ["(", ")", "{", "}", "[", "]"]
#        # arreglo que almacena los paréntesis invalidos
#        self.arreglo_invalido = []
#        # recorre la cadena y busca los paréntesis
#        for i in self.cadena:
#            # si el paréntesis no esta en el arreglo valido lo agrega al arreglo invalido
#            if i not in self.arreglo_valido:
#                self.arreglo_invalido.append(i)
#        # si el arreglo invalido tiene valores imprime que no es valido
#        if self.arreglo_invalido:
#            print("No es valido")
#        # si el arreglo invalido no tiene valores imprime que es valido
#        else:
#            print("Es valido")
#
## llamar a la clase
#cadena1 = "()"
#cadena2 = "()[]{}"
#cadena3 = "[)"
#cadena4 = "({[)]"
#cadena5 = "{{{"
#ValidarCadena(cadena1)
#ValidarCadena(cadena2)
#ValidarCadena(cadena3)
#ValidarCadena(cadena4)
#ValidarCadena(cadena5)


