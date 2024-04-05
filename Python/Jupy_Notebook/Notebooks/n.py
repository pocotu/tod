def rsa_encrypt(message, public_key):
    # Convert each character in the plaintext to integers based on the Unicode standard using ord()
    # Encrypt each character by raising it to the power of e and then taking the modulus n
    return [pow(ord(char), public_key[1], public_key[0]) for char in message]

# Define the public key
public_key = (2491, 65537)

# Define the message
message = "huaylla"

# Encrypt the message
encrypted_message = rsa_encrypt(message, public_key)

# Print the encrypted message
print(f"The encrypted message is: {encrypted_message}")

# muestra los calculos que se hicieron internamente para cifrar el mensaje
print(f"Calculos internos: {[(ord(char), pow(ord(char), public_key[1]), pow(ord(char), public_key[1], public_key[0])) for char in message]}")

# muestra los calculos que se hicieron internamente para cifrar el mensaje



