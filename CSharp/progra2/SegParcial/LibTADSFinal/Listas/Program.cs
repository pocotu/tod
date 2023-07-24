using System;

namespace Listas
{
    class Program
    {
        static void Main(string[] args)
        {
            // Crear una nueva lista
            CListaRecursiva lista = new CListaRecursiva();

            // Agregar elementos a la lista
            lista.Agregar("Elemento 1");
            lista.Agregar("Elemento 2");
            lista.Agregar("Elemento 3");

            // Mostrar la lista
            Console.WriteLine("Elementos en la lista:");
            lista.Mostrar();
            Console.WriteLine("");

            // Obtener el elemento en la posición 2
            int posicion = 2;
            Console.WriteLine($"Elemento en la posición {posicion}: {lista.Iesimo(posicion)}");
            Console.WriteLine("");

            // Insertar un nuevo elemento en la posición 2
            string nuevoElemento = "Elemento 5";
            Console.WriteLine($"Nuevo elemento: {nuevoElemento}");
            lista.Insertar(nuevoElemento, posicion);
            Console.WriteLine("");

            // Mostrar la lista actualizada
            Console.WriteLine("Elementos en la lista después de la inserción:");
            lista.Mostrar();
            Console.WriteLine("");

            // Eliminar un elemento de la lista
            lista.Eliminar("Elemento 2");

            // Mostrar la lista actualizada
            Console.WriteLine("Elementos en la lista después de la eliminación:");
            lista.Mostrar();
            Console.WriteLine("");

            // Verificar si la lista está vacía
            Console.WriteLine($"La lista está vacía? {lista.EstaVacia()}");

            // Calcular la longitud de la lista
            Console.WriteLine($"Longitud de la lista: {lista.Longitud()}");
            Console.WriteLine("");

            // Buscar la ubicación de un elemento en la lista
            string elementoBuscado = "Elemento 3";
            int ubicacion = lista.Ubicacion(elementoBuscado);
            if (ubicacion != -1)
            {
                Console.WriteLine($"El elemento '{elementoBuscado}' se encuentra en la posición {ubicacion}");
            }
            else
            {
                Console.WriteLine($"El elemento '{elementoBuscado}' no está en la lista");
            }
            Console.WriteLine("----------------------------------------");

            // Crear una nueva lista circular
            CListaCircular listaCircular = new CListaCircular();

            // Agregar elementos a la lista circular
            listaCircular.Agregar("Elemento A");
            listaCircular.Agregar("Elemento B");
            listaCircular.Agregar("Elemento C");

            // Mostrar la lista circular
            Console.WriteLine("Elementos en la lista circular:");
            listaCircular.Mostrar();
            Console.WriteLine("");

            Console.WriteLine("----------------------------------------");

            // Crear una nueva lista ordenada
            CListaOrdenada listaOrdenada = new CListaOrdenada();

            // Agregar elementos a la lista ordenada
            listaOrdenada.Agregar("Manzana");
            listaOrdenada.Agregar("Naranja");
            listaOrdenada.Agregar("Banana");

            // Mostrar la lista ordenada
            Console.WriteLine("Elementos en la lista ordenada:");
            listaOrdenada.Mostrar();
            Console.WriteLine("");

            Console.WriteLine("----------------------------------------");

            // Crear una nueva lista enlazada
            CListaEnlazada listaEnlazada = new CListaEnlazada();

            // Agregar elementos a la lista enlazada
            listaEnlazada.Agregar("Rojo");
            listaEnlazada.Agregar("Verde");
            listaEnlazada.Agregar("Azul");

            // Mostrar la lista enlazada
            Console.WriteLine("Elementos en la lista enlazada:");
            listaEnlazada.Mostrar();
            Console.WriteLine("");

            Console.WriteLine("----------------------------------------");
            
            // Crear una nueva lista doble enlazada
            CListaDobleEnlazada listaDobleEnlazada = new CListaDobleEnlazada();

            // Agregar elementos a la lista doble enlazada
            listaDobleEnlazada.Agregar("Lunes");
            listaDobleEnlazada.Agregar("Martes");
            listaDobleEnlazada.Agregar("Miércoles");

            // Mostrar la lista doble enlazada
            Console.WriteLine("Elementos en la lista doble enlazada:");
            listaDobleEnlazada.Mostrar();
            Console.WriteLine("");

            Console.ReadKey();
        }
    }
}
