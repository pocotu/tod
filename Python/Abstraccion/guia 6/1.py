'''
Dada la siguiente lista, haciendo uso de listas y sublistas ubique los elementos de
la sublista en el lugar que le corresponde (Enumere los pasos a seguir).
lista_original = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_lista = ["h", "i", "j"]
'''
lista_original = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_lista = ["h", "i", "j"]
lista_original[2][1][2] = sub_lista
print(lista_original)
