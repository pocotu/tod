# Imprimir numeros primos en un rango
def NrosPrimos(menor, mayor):
    # recorriendo
    for num in range(menor, mayor + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i == 0):
                    #print("resto: ", num)
                    break
            else:
                print("numero primo: ", num) # Primo
    return num

def main():
    menor = int(input("Ingrese el numero menor: "))
    mayor = int(input("Ingrese el numero mayor: "))
    NrosPrimos(menor, mayor)

main()