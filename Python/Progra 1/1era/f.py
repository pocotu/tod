"""SUMAR RESTAR MULTIPLICAR DIVIDIR Y SIMPLIFICAR"""
print("    Las operaciones de suma, resta, multiplicacion, division de fracciones    ")
print(" -----------------------------------------------------------------------------")
# ---Leer Datos
"""NUMERADORES Y DENOMINADORES"""
N1=float(input("Ingresar el numerador_uno: "))
D1=float(input("Ingresar el Denominador_uno: "))
N2=float(input("Ingresar el numerador_dos : "))
D2=float(input("Ingresar el Denominador_dos : "))
# ---ERROR AL PONER 0 EN EL DENOMINADOR
while(D1 and D2 == 0):
    print("ERROR.El denominador no puede ser CERO")
print("")
# ---SUMA DE FRACCIONES
N11=((D2*N1)+(D1*N2))
D11=(D1*D2)
suma=((D2*N1)+(D1*N2))/(D1*D2)
# ---MODULO SIMPLIFICAR
def Simplificar(N11,D11):
    mcd=MCD(N11,D11)
    return N11/ mcd, D11/mcd
# ---MODULO MCD
def MCD(N11,D11):
    Resto= N11%D11
    while Resto !=0:
        N11=D11
        D11=Resto
        Resto= N11 % D11
    return D11
print("El numerador de la suma es", str(N11))
print("El denominador de la suma es",str(D11))
print("**********************************")
print("La suma es",str(suma))
print("Simplificado: ",N11,D11)
print("")
# ---RESTA DE FRACCIONES
N22=((D2*N1)-(D1*N2))
D22=(D1*D2)
resta=((D2*N1)-(D1*N2))/(D1*D2)
# ---MODULO SIMPLIFICAR
def Simplificar(N22,D22):
    mcd=MCD(N22,D22)
    return N22/ mcd, D22/mcd
# ---MODULO MCD
def MCD(N22,D22):
    Resto= N22%D22
    while Resto !=0:
        N22=D22
        D22=Resto
        Resto=N22%D22
    return D22
print("El numerador de la resta es", str(N22))
print("El denominador de la resta es",str(D22))
print("**********************************")
print("La resta es",str(resta))
print("Simplificar", N22,D22)
print("")
# ---MULTIPLICACION DE FRACCIONES
N33=(N1*N2)
D33=(D1*D2)
producto=(N1*N2)/(D1*D2)
# ---MODULO SIMPLIFICAR
def Simplificar(N33,D33):
    mcd=MCD(N33,D33)
    return N33/ mcd, D33/ mcd
# ---MODULO MCD
def MCD(N33,D33):
    Resto= N33%D33
    while Resto !=0:
        N33=D33
        D33=Resto
        Resto=N33%D33
    return D33
print("El numerador del producto es", str(N33))
print("El denominador del producto es",str(D33))
print("**********************************")
print("El producto es",str(producto))
print("Simplificar", N33,D33)
print("")
# ---DIVISION DE FRACCIONES
N44=(N1*D2)
D44=(N2*D1)
division=(N1*D2)/(N2*D1)
# ---MODULO SIMPLIFICAR
def Simplificar(N44,D44):
    mcd=MCD(N44,D44)
    return N44/ mcd, D44/mcd
# ---MODULO MCD
def MCD(N44,D44):
    Resto= N44%D44
    while Resto !=0:
        N44=D44
        D44=Resto
        Resto=N44%D44
    return D44
print('El numerador de la division es', str(N44))
print('El denominador de la division es',str(D44))
print('**********************************')
print('La division es',str(division))
print('Simplificar', N44,D44)
print('')



