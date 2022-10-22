'''
Escribir un algoritmo que ordene ascendentemente tres números
'''
# Leer los tres numeros
Nro1 = int(input('Ingrese el primer numero: '))
Nro2 = int(input('Ingrese el segundo numero: '))
Nro3 = int(input('Ingrese el tercer numero: '))

# Ordenando y mostrando los numeros de forma ascendente
if Nro1 > Nro2 and Nro2 > Nro3:
    print('Numeros ordenandos:',Nro3,Nro2,Nro1)
elif Nro2 > Nro1 and Nro1 > Nro3:
    print('Numeros ordenandos:',Nro3,Nro1,Nro2)
elif Nro3 > Nro1 and Nro1 > Nro2:
    print('Numeros ordenandos:',Nro2,Nro1,Nro3)
elif Nro3 > Nro2 and Nro2 > Nro1:
    print('Numeros ordenandos:',Nro1,Nro2,Nro3)
elif Nro2 > Nro3 and Nro3 > Nro1:
    print('Numeros ordenandos:',Nro1,Nro3,Nro2)
else:
    print('Se ingresaron numeros iguales')
