using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace appTDACola
{
    // -------------------------------------------------------
    // Clase Menu
    // -------------------------------------------------------
    class Menu
    {
        private CCola cola;

        public Menu()
        {
            cola = new CCola();
        }

        // -------------------------------------------------------
        // Metodo MostrarMenu
        // -------------------------------------------------------
        public void MostrarMenu()
        {
            int opcion = 0;
            do
            {
                Console.WriteLine("1. Insertar");
                Console.WriteLine("2. Atender");
                Console.WriteLine("3. Primer Elemento");
                Console.WriteLine("4. Ultimo Elemento");
                Console.WriteLine("5. Longitud de la Cola");
                Console.WriteLine("6. Mostrar");
                Console.WriteLine("7. Salir");
                Console.Write("Opcion: ");
                // Pide una opcion al usuario en formato string
                // y lo convierte a int
                opcion = int.Parse(Console.ReadLine());

                switch (opcion)
                {
                    case 1:
                        Console.Write("Elemento: ");
                        int elemento = int.Parse(Console.ReadLine());
                        cola.Insertar(elemento);
                        break;
                    case 2:
                        cola.Atender();
                        break;
                    case 3:
                        cola.PrimerElemento();
                        break;
                    case 4:
                        cola.UltimoElemento();
                        break;
                    case 5:
                        cola.LongitudCola();
                        break;
                    case 6:
                        cola.Mostrar();
                        break;
                    case 7:
                        Console.WriteLine("Fin del programa.");
                        break;
                    default:
                        Console.WriteLine("Opcion no valida.");
                        break;
                }
            } while (opcion != 7);
        }
    }

    // -------------------------------------------------------
    // Programa Principal
    // -------------------------------------------------------
    class Program
    {
        static void Main(string[] args)
        {
            Menu menu = new Menu();
            menu.MostrarMenu();
        }
    }
}
