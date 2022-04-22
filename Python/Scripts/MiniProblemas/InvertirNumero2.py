n = float(input("Ingrese un número: "))

if n>9:
    c4 = int(n%10)
    c3 = int((n%100)/10)
    c2 = int((n%1000)/100)
    c1 = int((n-(n%1000))/1000)
    inv = (c4*1000)+(c3*100)+(c2*10)+c1
    
else:
    print("Ingrese un numero entero")
print("El numero invetido es: ",inv)

