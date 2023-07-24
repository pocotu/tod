using System;

namespace Listas
{
    public class CNodoListaCircular
    {
        private Object aElemento;
        private CNodoListaCircular aSgte;

        public CNodoListaCircular()
        {
            aElemento = null;
            aSgte = null;
        }

        public CNodoListaCircular(Object pElemento)
        {
            aElemento = pElemento;
            aSgte = null;
        }

        public CNodoListaCircular(Object pElemento, CNodoListaCircular pNodo)
        {
            aElemento = pElemento;
            aSgte = pNodo;
        }

        public object Elemento
        {
            set { aElemento = value; }
            get { return aElemento; }
        }

        public CNodoListaCircular Sgte
        {
            set { aSgte = value; }
            get { return aSgte; }
        }
    }
}
