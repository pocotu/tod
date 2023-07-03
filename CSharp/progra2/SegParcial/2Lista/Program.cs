using System;

class Program
{
    static void Main (string[] args)
    {
        // crear un lista de enteros
        List <int> numeros = new List<int>();

        // Agregar elementos a la lista
        numeros.Add(10);
        numeros.Add(20);
        numeros.Add(30);
        numeros.Add(40);

        // Acceder a los elementos de la lista
        Console.WriteLine("Elementos de la lista:");
        foreach (int numero in numeros)
        {
            Console.WriteLine(num);
        }
        
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
        foreach (int numero in numeros)
        {
            Console.WriteLine(num);
        }

        // Limpiar todos los elementos de la lista
        numeros.Clear();
    }
}
