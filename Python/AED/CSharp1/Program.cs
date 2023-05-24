
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


using Algoritmos;

namespace Punto
{
    class Program
    {
        static void Main(string[] args)
        {
            //Crear 2 objetos de la clase CPunto(Instanciar)
            CPunto Punto1 = new CPunto();
            CPunto Punto2 = new CPunto(-15, 8);
            Punto1.X = 50;
            Punto1.Y = 25;
            Console.WriteLine("Punto1 = ("+Punto1.X + ","+Punto1.Y+")");
            Console.WriteLine("Punto1 = (" + Punto2.X + "," + Punto2.Y + ")");
            //Calcular distancia (Méteodo de instancia)
            double Distancia = Punto1.CalcularDistancia(Punto2);
            //Calcular la distancia 2
            double Distancia2 = CPunto.CalcularDistancia(Punto1, Punto2);
            //Calcular la distancia 3
            double Distancia3 = Punto1 - Punto2;
            //Mostrar la distancia
            Console.WriteLine("Distancia = " + Distancia);
            Console.WriteLine("Distancia2 = " + Distancia2);
            Console.WriteLine("Distancia3 = " + Distancia3);
            Console.ReadLine();
        }
        
    }
}