# Te dan una matriz b de longitud n, definamos otro arreglo a, tambien
# de longitud n, para el cual ai = (2^(bi))(1<=i<=n)
#
# Valeri dice qie cada dos subarreglos de a que no se intersecan tienen
# diferentes suma de elementos. quiere determinar si esta equivocado, mas
# formalmente. necesita determinar si existe cuatro enteros l1, r1, l2, r2,
# eso satisface la siguiente condicion:
#
# 1 <= l1 <= r1 <= l2 <= r2 <= ni
# al1 + ali + 1 + ... + ar1 - 1 + ar1 = al2 + al2 + 1 + ... + ar2 - 1 + ar2
#
# si tales cuatro elementos existen, demostrara que valeri esta equivocado
# existen?
#
# Input
# cada prueba contiene multiples casos de prueba. la primera linea el numero
# de casos de prueba t (1 <= t <= 100). a continuacion, cada caso de prueba
#
# la primera linea de cada caso de prueba contiene un solo numero n (1 <= n 1000)
#
# la segunda linea contiene n enteros b1, b2, ..., bn (0 <= bi <= 10^9)
#
# Output
# para cada caso de prueba, si existen dos subarreglos que no se intersecan en a que
# tienen la misma suma, genere SI en una linea separada. de lo contrario, genere NO
# en una linea separada
# ademas, que tenga en cuenta que cada letra puede ser cualquier caso.
#
# Ejemplo
# Input
# 2
# 6
# 4 3 0 1 2 0
# 2
# 2 5
#
# Output
# SI
# NO
#
# Nota: en el primer caso a=[16, 8, 1, 2, 4, 1]. elegir l1 = 1, r1 = 1, l2 = 2, r2 = 6
# porque trabaja 16 = 8 + 1 + 2 + 4 + 1
# en el segundo caso, se puede verificar que no hay forma de seleccionar tas subarreglos
