print('cantidad de productos:')
productos=int(input())
i=0
sub=0
while i<productos:
    print('Producto',i+1,'valor:')
    val=int(input())
    print('Cantidad')
    cant=int(input())
    subpro=val*cant
    sub=sub+subpro
    i+=1
IGV=sub*0.18
valorVenta=sub+IGV
print('se vendieron:',productos,'productos')
print('subtotal:',sub)
print('IGV:',IGV)
print('total:',valorVenta)