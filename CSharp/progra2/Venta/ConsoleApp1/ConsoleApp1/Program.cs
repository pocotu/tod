using System;

namespace SistemaTienda
{
    class Program
    {
        static void Main(string[] args)
        {
            cLista<Producto> inventario = new cLista<Producto>();
            inventario.Agregar(new Producto { ID = 1, Nombre = "Radio", Precio = 100, CantidadDisponible = 10 });
            inventario.Agregar(new Producto { ID = 2, Nombre = "DVD", Precio = 200, CantidadDisponible = 20 });
            inventario.Agregar(new Producto { ID = 3, Nombre = "Televisor", Precio = 550, CantidadDisponible = 15 });
            inventario.Agregar(new Producto { ID = 4, Nombre = "Licuadora", Precio = 220, CantidadDisponible = 5 });
            inventario.Agregar(new Producto { ID = 5, Nombre = "Lavadora", Precio = 2050, CantidadDisponible = 8 });

            cPila<Devolucion> devoluciones = new cPila<Devolucion>();

            cCola<Pedido> pedidosEnLinea = new cCola<Pedido>();

            Devolucion devolucion = new Devolucion { ProductoID = 3, CantidadDevuelta = 2, Motivo = "Producto defectuoso" };
            devoluciones.Push(devolucion);

            Pedido pedido = new Pedido { ProductoID = 1, CantidadPedido = 3, NombreCliente = "Cliente1", DireccionEntrega = "Direccion1" };
            pedidosEnLinea.Encolar(pedido);

            Console.WriteLine("Inventario");
            foreach (Producto producto in inventario)
            {
                Console.WriteLine($"ID: {producto.ID}, Nombre: {producto.Nombre}, Cantidad disponible: {producto.CantidadDisponible}");
            }
        }
    }
}
