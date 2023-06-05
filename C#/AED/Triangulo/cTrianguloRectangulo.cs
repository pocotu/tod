using System;
using System.Collections.Generic;
using System.Text;

namespace appPunto1
{
    class cTrianguloRectangulo : cTriangulo // Herencia
    {
        private int aAngulo1;
        private int aAngulo2;
        

        public cTrianguloRectangulo():base()
        {
            aAngulo1 = 45;
            aAngulo2 = 45;

        }
        public cTrianguloRectangulo(cPunto pPunto1, cPunto pPunto2, cPunto pPunto3, 
                int pAngulo1, int pAngulo2) : base(pPunto1, pPunto2, pPunto3)
        {
            if (pAngulo1 + pAngulo2 == 90)
            {
                aAngulo1 = pAngulo1;
                aAngulo2 = pAngulo2;
            }
            else 
            {
                aAngulo1 = 45;
                aAngulo2 = 45;
            }
        }
        public int Angulo1
        {
            get { return aAngulo1; }
            set {
                if (value + aAngulo2 == 90)
                    aAngulo1 = value;
                    }
        }
        public int Angulo2
        {
            get { return aAngulo2; }
            set
            {
                if (aAngulo1 + value == 90)
                    aAngulo2 = value;
            }
        }
    }
}
