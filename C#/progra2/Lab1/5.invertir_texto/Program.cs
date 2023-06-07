// Escribir un programa que invierta un texto de
// manera recursiva.

using System;

namespace InvertirTexto
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Introduce un texto: ");
            string texto = Console.ReadLine();
            Console.WriteLine("Texto invertido: {0}", InvertirTexto(texto));
        }

        static string InvertirTexto(string texto)
        {
            if (texto.Length == 1)
                return texto;
            else
                return texto.Substring(texto.Length - 1, 1)+InvertirTexto(texto.Substring(0, texto.Length - 1));
        }
    }
}
