using System;

namespace B_Secuencial
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] lista = { 4, 7, 2, 1, 5, 9, 8, 3, 6 };
            int valorBuscado = 9;

            int posicion = Comparacion.BusquedaSecuencial(lista, valorBuscado);


            Comparacion.ImprimirResultado(valorBuscado, posicion);
            Comparacion.ImprimirResultado(valorBuscado, posicion);
            
        }
    }
}
