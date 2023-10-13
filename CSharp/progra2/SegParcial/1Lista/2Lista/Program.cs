using System;
// System.Collections.Generic es el namespace que contiene la clase List
using System.Collections.Generic;

class Program
{
    static void Main (string[] args)
    {
        // crear un lista de enteros
		// La sintaxis para crear una lista es:
		// List <tipo> nombreLista = new List<tipo>();
		List <int> numeros = new List <int>();		 

        // Agregar elementos a la lista
        numeros.Add(10);
        numeros.Add(20);
        numeros.Add(30);
        numeros.Add(40);
        
		// Imprimir todos los elementos de la lista
		// en una sola linea
		Console.WriteLine("Elementos de la lista en una sola linea:");
		Console.WriteLine(string.Join(", ", numeros));


        // Optener la cantidad de elementos de la lista
        int cantidadElementos = numeros.Count;
        Console.WriteLine("Cantidad de elementos en la lista: " + cantidadElementos);

        // Verificar si la lista contiene un elemento especifico
        int numeroBuscado = 30;
        if (numeros.Contains(numeroBuscado))
        {
            Console.WriteLine("La lista contiene el numero " + numeroBuscado);
        }
        else
        {
            Console.WriteLine("La lista no contiene el numero " + numeroBuscado);
        }

        // Eliminar un elemento de la lista
        numeros.Remove(20);
        Console.WriteLine("Elementos de la lista despues de eliminar el numero 20:");
        foreach (int num in numeros)
        {
            Console.WriteLine(num);
        }

        // Limpiar todos los elementos de la lista
        numeros.Clear();
    }
}

