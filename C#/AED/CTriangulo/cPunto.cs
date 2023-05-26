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
}

