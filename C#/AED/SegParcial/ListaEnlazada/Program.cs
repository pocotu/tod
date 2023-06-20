using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace appListaEnlazada
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Instanciar una lista
            CLista Lista = new CLista();

            // Agregar nodos a nuestra lista
            Lista.InsertarAlInicio(10);
            Lista.InsertarAlInicio(20);
            Lista.InsertarAlInicio(30);
            Lista.InsertarAlInicio(40);
            Lista.InsertarAlInicio(50);

            // Mostrar los nodos de la lista
            Console.WriteLine("Lista de Nodos");
            Lista.Mostrar();
            Console.WriteLine();

            // Insertar un nodo en una posicion específica
            Lista.InsertarEnPosicion(25, 2); //

            // Mostrar los nodos de la lista despues de insertar en posicion
            Console.WriteLine("Lista de Nodos despues de insertar en posicion");
            Lista.Mostrar();
            Console.WriteLine();

            // Insertar un nodo al final de la lista
            Lista.InsertarAlFinal(60);

            // Mostrar los nodos de la lista despues de insertar al final
            Console.WriteLine("Lista de Nodos despues de insertar al final");
            Lista.Mostrar();
            Console.WriteLine();

            // Eliminar la Cabeza
            Lista.EliminarCabeza();

            // Mostrar los nodos de la lista despues de eliminar la cabeza
            Console.WriteLine("Lista de Nodos despues de eliminar la cabeza");
            Lista.Mostrar();
            Console.WriteLine();

            // Eliminar el último nodo
            Lista.EliminarCola();

            // Mostrar los nodos de la lista despues de eliminar el ultimo nodo
            Console.WriteLine("Lista de Nodos despues de eliminar el ultimo nodo");
            Lista.Mostrar();
            Console.WriteLine();

            // Eliminar un nodo por elemento
            Lista.EliminarElemento(25);

            // Mostrar los nodos de la lista despues de eliminar un nodo por elemento
            Console.WriteLine("Lista de Nodos despues de eliminar un nodo por elemento");
            Lista.Mostrar();
            Console.WriteLine();
    
            Console.ReadKey();
        }
    }
}
