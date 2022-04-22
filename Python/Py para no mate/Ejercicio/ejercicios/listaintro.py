array = ["futbol","pc",18.3,6,[3,34,2.5],True,False]
print(array[4])
print("el ultimo de la lista es:",array[-1])
print("Cantidad de elemetos:",len(array))
array.append(100)
print(array)
print("Cantidas de elementos de la nueva lista:",len(array))
array.insert(2,250)
print(array)
print("Cantidas de elementos de la nueva lista:",len(array))
array.extend([2,3,False,True])
print(array)

#concatenar
array2 = [400,True,2.9]
array3 = array + array2
print("lista concatenada:",array3)
print("cantidad de elementos de la lista concatenada:",len(array))

#busqueda
print("Hola" in array)
print(array.index("futbol"))

#numero de veces que se repite un elemento
print("numero de veces que se repite el elemento",array.count(True))

#quitar datos de una lista
array.remove(True)
print(array)

#borrar elementos de una lista
#array.clear()

#cambiar la posicion de los datos
array.reverse()
print(array)

#ordena una lista de menor a mayor
#array=[1,2,5,-11,8]
#array.sort()
#print(array)

#ordernar una lista de mayor a menor
#array=[1,2,5,-11,8]
#array.sort(reverse=True)
#print(array)