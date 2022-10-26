def IGV(precio, cantidad):
    precio_t = precio * cantidad
    igv = precio_t * 0.18
    precio_v = precio_t + igv
    print("subototal", precio_t)
    print("IGV", igv)
    return precio_v

def main():
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad de productos: "))
    #print("subototal", precio_t)
    
    print("Total", IGV(precio, cantidad))
          
main()
