M= int(input("Imgrese su monto inicial-->"))
I= float(input("Ingrese el interes--> "))
P= int(input("Ingrese el periodo--> "))


def InteresSimpleAnual(M,I,P):
    MF=M*(I/100)*P
    RF=M+MF
    print("Su monto final ANUAL en soles es : " ,RF )
    
def InteresSimpleMensual(M,I):
    T= int(input("Ingrese el periodo en meses--> "))
    IF=M*(I/1200)*T
    RF=M+IF
    print("Su monto final MENSUAL en soles es : " ,RF )

def Menu():
    print("1. I.S.A")
    print("2. I.S.M")
    print("3. Salir ")

print(Menu())
OPCION=int(input("INGRESE LA OPCION: "))
while(OPCION!=3):
    
    if(OPCION==1):
        InteresSimpleAnual(M,I,P)
        
    else:
        InteresSimpleMensual(M,I)
            
    print(Menu())
    OPCION=int(input("INGRESE LA OPCION: "))



MF=M*I*P
print(MF)
