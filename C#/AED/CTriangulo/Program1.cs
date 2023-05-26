using System;

namespace appPunto1
{
    class cPunto
    {
        // Atributos
        private double x;
        private double y;

        // Propiedades
        public double X
        {
            get { return x; }
            set { x = value; }
        }

        public double Y
        {
            get { return y; }
            set { y = value; }
        }

        // Constructor
        public cPunto(double pX, double pY)
        {
            x = pX;
            y = pY;
        }
    }

    class cTriangulo
    {
        // Atributos
        private cPunto aPunto1;
        private cPunto aPunto2;
        private cPunto aPunto3;

        // Constructores
        public cTriangulo()
        {
            aPunto1 = new cPunto(0, 0);
            aPunto2 = new cPunto(-1, 1);
            aPunto3 = new cPunto(1, -1);
        }

        public cTriangulo(cPunto pPunto1, cPunto pPunto2, cPunto pPunto3)
        {
            aPunto1 = pPunto1;
            aPunto2 = pPunto2;
            aPunto3 = pPunto3;
        }

        // Getters y Setters
        public cPunto Punto1
        {
            get { return aPunto1; }
            set { aPunto1 = value; }
        }

        public cPunto Punto2
        {
            get { return aPunto2; }
            set { aPunto2 = value; }
        }

        public cPunto Punto3
        {
            get { return aPunto3; }
            set { aPunto3 = value; }
        }

        // Método de instancia para calcular el área del triángulo
        public double CalcularArea()
        {
            double ladoA = CalcularDistancia(aPunto1, aPunto2);
            double ladoB = CalcularDistancia(aPunto2, aPunto3);
            double ladoC = CalcularDistancia(aPunto3, aPunto1);

            double semiperimetro = (ladoA + ladoB + ladoC) / 2;
            double area = Math.Sqrt(semiperimetro * (semiperimetro - ladoA) * (semiperimetro - ladoB) * (semiperimetro - ladoC));

            return area;
        }

        // Método de clase para calcular el área del triángulo
        public static double CalcularArea(cPunto punto1, cPunto punto2, cPunto punto3)
        {
            cTriangulo triangulo = new cTriangulo(punto1, punto2, punto3);
            return triangulo.CalcularArea();
        }

        // Método auxiliar para calcular la distancia entre dos puntos
        private static double CalcularDistancia(cPunto punto1, cPunto punto2)
        {
            double distancia = Math.Sqrt(Math.Pow(punto2.X - punto1.X, 2) + Math.Pow(punto2.Y - punto1.Y, 2));
            return distancia;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // Crear un triángulo con puntos personalizados
            cPunto punto1 = new cPunto(0, 0);
            cPunto punto2 = new cPunto(3, 0);
            cPunto punto3 = new cPunto(0, 4);

            cTriangulo triangulo1 = new cTriangulo(punto1, punto2, punto3);

            double areaTriangulo1 = triangulo1.CalcularArea();
            Console.WriteLine("Área del triángulo 1: " + areaTriangulo1);

            // Crear un triángulo con puntos predeterminados
            cTriangulo triangulo2 = new cTriangulo();

            double areaTriangulo2 = cTriangulo.CalcularArea(triangulo2.Punto1, triangulo2.Punto2, triangulo2.Punto3);
            Console.WriteLine("Área del triángulo 2: " + areaTriangulo2);
        }
    }
}

