# Imprimir numeros primos en un rango
menor = 10
mayor = 20

# recorriendo
for num in range(menor, mayor + 1):
    print("num: ", num)
    if num > 1:
        print("si: ", num)
        for i in range(2, num):
            print("i: ", i)
            if (num % i == 0):
                #print("resto: ", num)
                break
        else:
            print("numero primo: ", num) # Primo


