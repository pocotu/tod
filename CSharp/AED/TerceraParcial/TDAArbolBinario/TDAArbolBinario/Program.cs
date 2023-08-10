using System;

namespace appABB
{
    internal class Program
    {
        static void Main(string[] args)
        {
            CABB arbolBB = new CABB();
            int opcion;

            do
            {
                Console.WriteLine("###### Menu ######");
                Console.WriteLine("1. Agregar Nodo");
                Console.WriteLine("2. Eliminar Nodo");
                Console.WriteLine("3. Visualizar arbol");
                Console.WriteLine(" ");
                Console.Write("Ingrese el número de opcion: ");
                opcion = int.Parse(Console.ReadLine());

                switch (opcion)
                {
                    case 1:
                        Console.Write("Ingrese el valor del nodo a agregar: ");
                        int valorAgregar = int.Parse(Console.ReadLine());
                        arbolBB.insertarNodo(valorAgregar);
                        break;
                    case 2:
                        Console.Write("Ingrese el valor del nodo a eliminar: ");
                        int valorEliminar = int.Parse(Console.ReadLine());
                        arbolBB.EliminarNodo(valorEliminar);
                        break;
                    case 3:
                        if (arbolBB.raiz != null)
                        {
                            Console.WriteLine("Recorrido en Orden:");
                            arbolBB.recorridoEnOrden(arbolBB.raiz);
                        }
                        else
                        {
                            Console.WriteLine("El arbol esta vacio.");
                        }
                        break;
                    default:
                        Console.WriteLine("Opcion invalida.");
                        break;
                }

                Console.WriteLine();
            } while (opcion != 4);
        }
    }
}
