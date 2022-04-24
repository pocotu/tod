A = str(input('Ingrese un arreglo'))
B = str(input('Ingrese otro arreglo'))
def UNION(A,B): 
    todo=A+B    
    union=[]    
    for i in todo:
        if i not in union:
            union.append(i)  
    return print("La union es: ",union)
n=4
UNION(A,B)