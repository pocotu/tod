'''
validar la entrada de un numero que no sea caracter o letra
'''

def Validacion(n):
    if n.isdigit():
        return True
    else:
        return False