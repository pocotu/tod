namespace SistemaTienda
{
    public class Pedido
    {   
        // Propiedades
        public int ProductoID { get; set; }
        public int CantidadPedido { get; set; }
        public string NombreCliente { get; set; }
        public string DireccionEntrega { get; set; }
    }
}
