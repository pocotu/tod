A = srt(input('Ingrese un arreglo'))
B = srt(input('Ingrese otro arreglo'))
def UNION(A,B): 
    todo=A+B    
    union=[]    
    for i in todo:
        if i not in union:
            union.append(i)  
    return print("La union es: ",union)
n=4
UNION(A,B)