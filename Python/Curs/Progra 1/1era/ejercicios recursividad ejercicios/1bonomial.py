# modulo para calcular el binomio de dos numeros
def binomial(n, k):
    # si k es 0 o n, el binomio es 1
    if k == 0 or k == n:
        return 1
    # si k es 1, el binomio es n 
    return binomial(n - 1, k - 1) + binomial(n - 1, k)

def main():
    # leemos los datos
    n = int(input('Introduce n: '))
    k = int(input('Introduce k: '))
    # calculamos el binomio
    print(binomial(n, k))

main()
