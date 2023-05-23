using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace appPOOEjercicio1

{
    Class Program
    {
        static void Main(string[] args)
        {
            // crear 2 objetos de la clase CPunto (instanciar)
            CPunto punto1 = new CPunto();
            CPunto punto2 = new CPunto(5, 10);

            // Imprimir los valores de los atributos de los objetos
            Console.WriteLine("punto1 = ("+punto1.X+","+punto1.Y+")");
            console.ReadLine();
        }
    }
}