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






#POTENCIA RECURSIVA 
#================AXB==========
# mudula para AXB
def Potencia(N,M):
    if M==0:
        return 1
    else :
        return N*Potencia(N,M-1)

#-----===========Programa principal=======-------
print('==========leer numero==========')
Nro1=int(input('ingrese el numero 1 : '))
Nro2=int(input('ingrese el numero 2 : '))
#--- importar el moodulo Multiplicar 
factor=Potencia(Nro1,Nro2)
#------mostrar resultado

print(factor)



#MULTIPLICACION RECURSIVA
#  ---- Programa principal
#================AXB==========
# mudula para AXB
def Multiplicacion(N,M):
    if M==0:
        return 0
    else :
        return N + Multiplicacion(N,M-1)
#-----Programa principal 
print('==========leer numero==========')
Nro1=int(input('ingrese el numero 1 : '))
Nro2=int(input('ingrese el numero 2 : '))
#--- importar el moodulo Multiplicar 
factor=Multiplicacion(Nro1,Nro2)
#------mostrar resultado
print(factor)



#----------------------------------------------------------------------
def Factorial(N):
    #Caso base
    if N<10:
        return 1

    else : #cccaso contrario
        return 1+ Factorial(N//10)
print('==========leer numero==========')
Nro1=int(input('ingrese el numero 1 : '))
Nro2=int(input('ingrese el numero 2 : '))
#--- importar el moodulo 
factor=Potencia(Nro1,Nro2)
#------mostrar resultado
print(factor)