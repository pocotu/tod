# imprimir numeros en un rango
menor = 100
mayor = 200
for num in range(menor, mayor +1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

