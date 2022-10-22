# RECURSIVA DE UN NUMER DECIMAL A NUMERO BINARIO
# IMPLEMENTAR EL MODULO

def DecBin(N):
    # caso Base
    if N<=1:
        return N
    # Caso recurrente
    else :
        return N%2+DecBin(N//2)*10
#=====PROGRAMA PRINCIPAL=====
#----LEER NUMERO
    

Nro=int(input('ingresar el numero decimal: '))
#---CALCULAR EL NUMERO DECIMAL A NUMEOR BINARIO

Binario=DecBin(Nro)
#--MOSTRAR RESULTADO 
print(Binario)