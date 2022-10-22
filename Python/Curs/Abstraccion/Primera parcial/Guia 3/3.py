'''
Dado el algoritmo recursivo
int Recursivo(int n)
{
int aux;
if (n==0)
aux=0;
else
aux=Recursivo(n-1)+(n*n);
return aux;
}
- Realizar una traza con n=5.
- Explicar brevemente qué hace el algoritmo.
- Realizare el diagrama de llaves
'''
# definimos la funcion
def Recursivo(n):
    # si n es 0, retornamos 0
    if n==0:
        # retornamos 0
        return 0
    # si no, retornamos la suma de la funcion con el numero de la funcion
    else:
        # retornamos la suma de la funcion
        return Recursivo(n-1)+(n*n)

print(Recursivo(5))
