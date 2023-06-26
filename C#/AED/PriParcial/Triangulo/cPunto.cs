using System;
using System.Collections.Generic;
using System.Text;

namespace appPunto1
{
    class cPunto
    {
        //--------------------------------------------------------
        // Atributos
        //--------------------------------------------------------
        private int aX;
        private int aY;

        //--------------------------------------------------------
        // Constructores 
        //--------------------------------------------------------
        public cPunto()
        {
            aX = 0;
            aY = 0;
        }
        //--------------------------------------------------------
        public cPunto(int pX, int pY)
        {
            aX = pX;
            aY = pY;
        }
        //--------------------------------------------------------
        // Propiedades
        //--------------------------------------------------------
        //Setters y Getters
        public int X
        {
            get { return aX; }
            set { aX = value;}
        }
        //---------------------------------------------------------
        public int Y
        {
            get { return aY;  }
            set { aY = value; }
        }

        //--------------------------------------------------------
        // Métodos de instancia
        //--------------------------------------------------------
        public double Distancia(cPunto pPunto)
        { // calcula la distancia entre pPunto y el objeto anfitrion
            return Math.Sqrt(Math.Pow(X - pPunto.X, 2) + Math.Pow(Y - pPunto.Y, 2));
        }
        //--------------------------------------------------------
        // Métodos de clase
        //--------------------------------------------------------
        public static double Distancia(cPunto pPunto1, cPunto pPunto2)
        { // calcula la distancia entre pPunto1 y pPunto2
            return Math.Sqrt(Math.Pow(pPunto1.X - pPunto2.X, 2) + Math.Pow(pPunto1.Y - pPunto2.Y, 2));
        }
        public static double operator - (cPunto pPunto1, cPunto pPunto2)
        { // calcula la distancia entre pPunto1 y pPunto2
            return Math.Sqrt(Math.Pow(pPunto1.X - pPunto2.X, 2) + Math.Pow(pPunto1.Y - pPunto2.Y, 2));
        }
    }
}