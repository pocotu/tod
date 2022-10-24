'''
Implementar un programa para imprimir:
1
1 2
1 2 3
……
1 2 3…. N
Para un n informado por el usuario. Use una 
función que reciba un valor n entero imprima 
hasta la n - ésima línea.
'''

def Imprimir(n):
	for i in range(1, n+1):
		for j in range(1, n+1):
			print(j, end = " ")
		print()

def main():
	n = int(input("Numero: "))
	Imprimir(n)

main()
