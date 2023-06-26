using System;

namespace Busqueda
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] lista = { 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 };
            int valorBuscado = 14;

            Comparacion comparacion = new Comparacion(lista, valorBuscado);
            comparacion.RealizarComparacion();
        }
    }
}

