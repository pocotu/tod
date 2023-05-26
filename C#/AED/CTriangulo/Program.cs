using System;

namespace appPunto1
{
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
}

