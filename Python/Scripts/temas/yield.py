def devolver_cuidades(*ciudades):
    for ciudad in ciudades:
        for elemento in ciudad:
            yield elemento

def devolucion(*frutas):
    for fruta in frutas:
        yield from fruta

devolver = devolver_cuidades("Cusco, Arequipa", "Lima", "Cajamarca")
print(next(devolver))
print(next(devolver))
print(next(devolver))
print(next(devolver))
print(next(devolver))
print(next(devolver))
print(next(devolver))
print(next(devolver))
print(next(devolver))
print(next(devolver))
print(next(devolver))
print(next(devolver))
print(next(devolver))
print(next(devolver))
print(next(devolver))
print(next(devolver))
print(next(devolver))

volver = devolucion("Manzana", "Pera", "Uva")
print(next(volver))
