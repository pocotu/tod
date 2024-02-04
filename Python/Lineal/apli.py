import string

def encriptar(plaintext, a, b):
    alphabet = string.ascii_uppercase
    m = len(alphabet)
    ciphertext = ""

    for char in plaintext:
        if char.upper() in alphabet:
            x = alphabet.index(char.upper())
            encrypted_char = (a * x + b) % m
            ciphertext += alphabet[encrypted_char]
        else:
            ciphertext += char

    return ciphertext

def decencriptar(ciphertext, a, b):
    alphabet = string.ascii_uppercase
    m = len(alphabet)
    inv_a = pow(a, -1, m)  # Calcular el inverso modular de 'a'

    plaintext = ""

    for char in ciphertext:
        if char.upper() in alphabet:
            y = alphabet.index(char.upper())
            decrypted_char = (inv_a * (y - b)) % m
            plaintext += alphabet[decrypted_char]
        else:
            plaintext += char

    return plaintext

def main():
    print("\n### Cifrado Afín ###")
    while True:
        print("\nSeleccione una opción:")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Salir")

        choice = input("Ingrese el número de la opción: ")

        if choice == "1":
            mensaje = input("Ingrese el mensaje a cifrar: ")
            a = int(input("Ingrese el valor de a (numero primo mayor a 0 y menor a 26): "))
            b = int(input("Ingrese el valor de b (numero primo mayor a 0 y menor a 26): "))
            textoCifrado = encriptar(mensaje, a, b)
            print("Mensaje cifrado:", textoCifrado)
        elif choice == "2":
            mensaje = input("Ingrese el mensaje a descifrar: ")
            a = int(input("Ingrese el valor de a: "))
            b = int(input("Ingrese el valor de b: "))
            textoPlano = decencriptar(mensaje, a, b)
            print("Mensaje descifrado:", textoPlano)
        elif choice == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")


if __name__ == "__main__":
    main()