using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace Algoritmos
{
    class CPunto
    {
        //-------------------------------------------------
        // Atributos
        //-------------------------------------------------
        private int aX;
        private int aY;

        public CPunto()
        {
            
        }

        //-------------------------------------------------
        //Constructores
        //-------------------------------------------------

        public CPunto(int pX, int pY)
        {
            aX = pX;
            aY = pY;
        }
        //-------------------------------------------------
        //Propiedades (set and get)
        //-------------------------------------------------
        public int X
        {
            get { return aX; }
            set { aX = value; }
        }
        public int Y
        {
            get { return aY; }
            set { aY = value; }
        }
        //-------------------------------------------------
        //Métodos
        //-------------------------------------------------
        //Métodos de instancia 
        public double CalcularDistancia(CPunto pPunto)
        {
            return (Math.Sqrt(Math.Pow(X - pPunto.X, 2)
                            + Math.Pow(Y - pPunto.Y, 2)));

        }
        // Métoto de class
        public static double CalcularDistancia(CPunto pPunto1, CPunto pPunto2)
        {
            return (Math.Sqrt(Math.Pow(pPunto1.X - pPunto2.X, 2)
                            + Math.Pow(pPunto1.Y - pPunto2.Y, 2)));
        }
        // Sobreescribir el operador 
        public static double operator -(CPunto pPunto1, CPunto pPunto2)
        {
            return (Math.Sqrt(Math.Pow(pPunto1.X - pPunto2.X, 2)
                            + Math.Pow(pPunto1.Y - pPunto2.Y, 2)));
        }
    }
}