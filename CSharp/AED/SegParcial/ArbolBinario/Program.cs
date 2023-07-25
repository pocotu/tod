using System;

namespace AppArbolBinario
{
    class Program
    {
        static void Main(string[] args)
        {
            CArbolBinario AppArbolBinario = new CArbolBinario();
            AppArbolBinario.Insertar(100);
            AppArbolBinario.Insertar(50);
            AppArbolBinario.Insertar(25);
            AppArbolBinario.Insertar(75);
            AppArbolBinario.Insertar(150);

            Console.WriteLine("Impresion PreOrder:");
            AppArbolBinario.ImprimirPre();

            Console.WriteLine("Impresion InOrder:");
            AppArbolBinario.ImprimirIn();

            Console.WriteLine("Impresion PostOrder:");
            AppArbolBinario.ImprimirPost();

            Console.ReadKey();
        }
    }
}
