using System;
using System.Collections.Generic;
using System.Text;

namespace appPunto1
{
    class cTriangulo
    {
        //--------------------------------------------------------
        // Atributos
        //--------------------------------------------------------
        private cPunto aPunto1;
        private cPunto aPunto2;
        private cPunto aPunto3;

        //--------------------------------------------------------
        // Constructores 
        //--------------------------------------------------------
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
        //--------------------------------------------------------
        // Propiedades
        //--------------------------------------------------------
        //Setters y Getters
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
    }
}
