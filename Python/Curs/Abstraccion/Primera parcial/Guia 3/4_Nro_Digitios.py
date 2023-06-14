# Numero de digitos de un numero
def NumeroDigitos(n):
    if n<10:
        return 1
    else:
        # retornamos 1 mas la funcion dividida entre 10
        return 1+NumeroDigitos(n//10)