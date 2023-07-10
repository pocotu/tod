using System;

namespace Listas
{
    class Program
    {
        static void Main(string[] args)
        {
            // Presentacion
            Console.WriteLine("#### Grupo 7 ####");
            Console.WriteLine("Integrantes:");
            Console.WriteLine("- Rossbel Huaylla Huillca");
            Console.WriteLine("- Diego Shaid Ninancuro Huarayo");
            Console.WriteLine("- Andree Achahuanci Valenza");
            Console.WriteLine("");

            // Crear una nueva lista
            CLista lista = new CLista();

            // Agregar elementos a la lista
            lista.Agregar("Elemento 1");
            lista.Agregar("Elemento 2");
            lista.Agregar("Elemento 3");

            // Mostrar la lista
            Console.WriteLine("Elementos en la lista:");
            lista.Mostrar();

            // Obtener el elemento en la posicion 2
            int posicion = 2;
            Console.WriteLine($"Elemento en la posicion {posicion}: {lista.Iesimo(posicion)}");

            // Insertar un nuevo elemento en la posicion 2
            string nuevoElemento = "Nuevo Elemento";
            lista.Insertar(nuevoElemento, posicion);

            // Mostrar la lista actualizada
            Console.WriteLine("Elementos en la lista despues de la insercion:");
            lista.Mostrar();

            // Eliminar un elemento de la lista
            lista.Eliminar("Elemento 1");

            // Mostrar la lista actualizada
            Console.WriteLine("Elementos en la lista despues de la eliminacion:");
            lista.Mostrar();

            // Verificar si la lista esta vacía
            Console.WriteLine($"La lista esta vacia? {lista.EstaVacia()}");

            // Calcular la longitud de la lista
            Console.WriteLine($"Longitud de la lista: {lista.Longitud()}");

            // Buscar la ubicacion de un elemento en la lista
            string elementoBuscado = "Elemento 3";
            int ubicacion = lista.Ubicacion(elementoBuscado);
            if (ubicacion != -1)
            {
                Console.WriteLine($"El elemento '{elementoBuscado}' se encuentra en la posicion {ubicacion}");
            }
            else
            {
                Console.WriteLine($"El elemento '{elementoBuscado}' no esta en la lista");
            }

            Console.ReadKey();
        }
    }
}
