using System;
using System.Collections.Generic;

namespace Lista
{
    class Program
    {
        static void Main(string[] args)
        {
            // Crear una lista de enteros
            List <int> numeros = new List<int>();

            // Agregar elementos a la lista
            numeros.Add(10);
            numeros.Add(20);
            numeros.Add(30);
            numeros.Add(40);

            // Acceder a los elementos de la lista
            Console.WriteLine("Elementos de la lista:");
            foreach (int n in numeros)
            {
                Console.WriteLine(n);
            }

            // Obtener la cantidad de elementos en la lista
            int cantidadElementos = numeros.Count;
            Console.WriteLine("Cantidad de elementos en la lista: " + cantidadElementos);

            // Verificar Si la lista contiene un elemento especifico
            int numeroBuscado = 30;
            if (numeros.Contains(numeroBuscado))
            {
                Console.WriteLine("La lista contiene el numero: " + numeroBuscado);
            }
            else
            {
                Console.WriteLine("La lista no contiene el numero: " + numeroBuscado);
            }

            // Eliminar un elemento
            int numeroEliminar = 20;
            numeros.Remove(numeroEliminar);
            Console.WriteLine("Elementos en la lista despues de eliminar al numero " + numeroEliminar);
            foreach(int n in numeros)
            {
                Console.WriteLine(n);
            }

            // Limpiar todos los elementos de la lista
            numeros.Clear();
        }
    }
}