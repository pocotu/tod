''' Escribir un algoritmo que permita determinar el número de dígitos
de un número entero positivo '''

# Leer el número 
Nro = int(input('Ingrese el número: '))
# --- Validar Nro
while (Nro <= 0):
    # --- Volver a Ingresar Nro.
    Nro = int(input(' ERROR.. Ingresa Nro. > 0: '))
NroDigitos = 0

while Nro > 0:
    # Contablizar por lo menos el último dígito
    NroDigitos += 1
    # Quitar del número el último dígito
    Nro = Nro // 10
# Mostrar resultado
print('Nro. de Digitos = ',NroDigitos)

