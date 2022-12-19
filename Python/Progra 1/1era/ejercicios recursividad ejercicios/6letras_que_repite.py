def letra_mas_comun(cadena):
    # contar las ocurrencias de cada letra en la cadena
    contadores = {}
    for c in cadena:
        if c in contadores:
            contadores[c] += 1
        else:
            contadores[c] = 1
    
    # encontrar la letra con la mayor cantidad de ocurrencias
    max_ocurrencias = 0
    letra_mas_comun = None
    for letra, ocurrencias in contadores.items():
        if ocurrencias > max_ocurrencias:
            max_ocurrencias = ocurrencias
            letra_mas_comun = letra
    
    return letra_mas_comun

print(letra_mas_comun('hola mundo'))  # 'o'
print(letra_mas_comun('abcabcabc'))  # 'a'
print(letra_mas_comun('aaaabbbbcccc'))  # 'a' o 'b' o 'c'
