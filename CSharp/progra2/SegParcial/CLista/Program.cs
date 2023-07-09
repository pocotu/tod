using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        // Crear una lista de textos
        List<string> nombres = new List<string>();

        // Agregar elementos a la lista
        nombres.Add("J");
        nombres.Add("M");
        nombres.Add("P");
        nombres.Add("A");
        nombres.Add("R");

        // Imprimir todos los elementos de la lista
        Console.WriteLine("Elementos de la lista:");
        Console.WriteLine(string.Join(", ", nombres));

        // Ordenar la lista en orden alfabetico
        nombres.Sort();

        // Imprimir los elementos de la lista ordenados
        Console.WriteLine("Elementos de la lista ordenados:");
        Console.WriteLine(string.Join(", ", nombres));

        // Obtener el indice de un elemento en la lista
        string nombreBuscado = "P";
        // IndexOf devuelve el indice del elemento buscado
        int indice = nombres.IndexOf(nombreBuscado);
        if (indice != -1)
        {
            Console.WriteLine("La letra '{0}' se encuentra en el indice {1}", nombreBuscado, indice);
        }
        else
        {
            Console.WriteLine("La letra '{0}' no se encontro en la lista", nombreBuscado);
        }
    }
}
