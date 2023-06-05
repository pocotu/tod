using System;

namespace appPunto1
{
    class Program
    {
        static void Main(string[] args)
        {  
            /*
            cPunto Punto1 = new cPunto();
            cPunto Punto2 = new cPunto(-15, 8);
            
            Punto1.X = 50; // 50 es el value
            Punto1.Y = 25;
            
            Console.WriteLine("Punto1 = (" + Punto1.X + "," + Punto1.Y + ")");
            Console.WriteLine("Ingrese coordenadas del Punto 2:");
            Console.Write("X= ");
            
            Punto2.X = int.Parse(Console.ReadLine());
            Console.Write("Y= ");
            Punto2.Y = int.Parse(Console.ReadLine());

            Console.WriteLine("Punto2 = (" + Punto2.X + "," + Punto2.Y + ")");
            
            //Metodo de instancia
            double Distancia1 = Punto1.Distancia(Punto2);
            
            //Metodo de clase
            double Distancia2 = cPunto.Distancia(Punto1, Punto2);
            
            //Sobrecarga de operadores
            double Distancia3 = Punto1 - Punto2;
            
            // Mostrar resultados
            Console.WriteLine("Distancia1 = " + Distancia1);
            Console.WriteLine("Distancia2 = " + Distancia2);
            Console.WriteLine("Distancia3 = " + Distancia3);
            */

            // Crear el Objeto TrianguloRectangulo
            cTrianguloRectangulo trianguloRectangulo1 = new cTrianguloRectangulo();
            Console.WriteLine(trianguloRectangulo1.Punto1.X);
            Console.WriteLine(trianguloRectangulo1.Punto1.Y);
            Console.WriteLine(trianguloRectangulo1.Punto2.X);
            Console.WriteLine(trianguloRectangulo1.Punto2.Y);
            Console.WriteLine(trianguloRectangulo1.Punto3.X);
            Console.WriteLine(trianguloRectangulo1.Punto3.Y);
            Console.WriteLine(trianguloRectangulo1.Angulo1);
            Console.WriteLine(trianguloRectangulo1.Angulo2);
        }
    }
}

