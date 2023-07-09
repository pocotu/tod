using System;

namespace appTDAPila
{
    class Program
    {
        static void Main(string[] args)
        {
            CPila pila = new CPila();

            // Verificar si la pila esta vacia
            Console.WriteLine("La pila esta vacia: " + pila.EstaVacia());

            // Apilar elementos
            pila.Apilar(10);
            pila.Apilar(20);
            pila.Apilar(30);

            // Mostrar elementos
            Console.WriteLine("Elementos en la pila:");
            pila.MostrarElementos();

            // Numero de elementos
            Console.WriteLine("Numero de elementos en la pila: " + pila.NumeroElementos());

            // Desapilar elementos
            int elementoDesapilado = pila.Desapilar();
            Console.WriteLine("Elemento desapilado: " + elementoDesapilado);

            // Mostrar elementos después de desapilar
            Console.WriteLine("Elementos en la pila despues de desapilar:");
            pila.MostrarElementos();

            // Numero de elementos despues de desapilar
            Console.WriteLine("Numero de elementos en la pila despues de desapilar: " + pila.NumeroElementos());

            // Verificar si la pila está vacia despues de desapilar
            Console.WriteLine("La pila esta vacia despues de desapilar: " + pila.EstaVacia());

            Console.ReadLine();
        }
    }
}
