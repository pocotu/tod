'''
int Misterio(int n1, int n2)
{
int aux;
if (n2==0)
aux=0;
else
aux=Misterio(n1*10,n2-1)+n1;
return aux;
}
- Realizar una traza con n1=5 y n2=4.
- ¿Qué hace el algoritmo?
- Hacer otra traza con n1=518 y n2=4.
- Realizare el diagrama de llaves
'''
# definimos la funcion
def Misterio(n1, n2):
    # si n2 es 0, retornamos 0
    if n2==0:
        # retornamos 0
        return 0
    # si no, retornamos la suma de la funcion con el numero de la funcion
    else:
        # retornamos la suma de la funcion con el numero de la funcion
        return Misterio(n1*10,n2-1)+n1
# imprimimos el resultado
print('Imprimiendo',Misterio(5,4))
print(Misterio(518,4))