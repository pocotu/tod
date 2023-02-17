def binario1(n):
    # si el número es 0, regresa una cadena vacía
    if n == 0:
        return ""
    
    else:
        # devuelve una cadena de caracteres que representa 
        # el número entero dado como parámetro en base 2.
        return binario1(n // 2) + str(n % 2)

def binario2(n, res):
    if n == 0:
        return res
    else:
        # Se obtiene el primer dígito del número en base 2 como el módulo de la división del número entero por 2, y se almacena en la lista.
        res.append(str(n % 2))
        # Se hace una llamada recursiva a la función con el cociente de la división del número entero por 2 como parámetro, y la lista de dígitos del número en base 2 como parámetro. Esto se repite hasta que el cociente sea 0.
        return binario2(n // 2, res)

def main():
    n = int(input("Ingresa un número entero: "))
    print("El número en base 2 es: ", binario1(n))
    print("El número en base 2 es: ", "".join(binario2(n, [])))

main()