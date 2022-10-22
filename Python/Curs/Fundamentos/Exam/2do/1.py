'''
Una tienda Comercial tiene dos tipos de productos: gravados y exonerados de IGV. Escribir una aplicacion modular que calcule
el importe total de un comprobante de pago, en cuyo detalle se considera la venta de N productos; considerando para cada
paso: el tipo de producto, el valor unitario y la cantidad de articulos vendidos
Ejemplo:
N = 5
Nro Tipo         Cantidad    Precio unitario     Impuesto    Sub total
1   Gravado         10              10              18          118
2   Gravado         1               200             36          236
3   Exonerado       2               40              0           80
4   Exonerado       2               50              0           100
5   Gravado         10              5               9           59
'''
# Leer cantidad de productos
Cant_productos = int(input('Cantidad de productos: '))

# Leer datos 
def Gravados():
    Precio_gravados = float(input('Precio del producto gravado: '))
    Cantidad_gravados = int(input('Cantidad del producto: '))
    Precio_total_gravado = Cantidad_gravados * Precio_gravados
    IGV = Precio_total_gravado * 0.18
    return IGV

def Exonerados():
    Precio_exonerados = float(input('Precio del producto exonerado: '))
    Cantidad_exonerados = int(input('Cantidad del producto: '))
    Precio_total_exonerado = Precio_exonerados * Cantidad_exonerados
    return Precio_total_exonerado

print()
print('Ingrese el tipo de producto: Gravados = G, Exonerados = E')
i = 0
while i < Cant_productos:
    print('Tipo del producto',i+1)
    Tipo_productos = str(input())
    if Tipo_productos == 'G':
        Gravados()
        i = i + 1

    elif Tipo_productos == 'E':
        Exonerados()
        i = i + 1

IGV = Gravados()
print(IGV)