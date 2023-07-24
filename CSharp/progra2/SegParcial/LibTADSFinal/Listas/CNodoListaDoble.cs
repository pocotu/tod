using System;

namespace Listas
{
    public class CNodoListaDoble
    {
        private Object aElemento;
        private CNodoListaDoble aSgte;
        private CNodoListaDoble aAnt;

        public CNodoListaDoble()
        {
            aElemento = null;
            aSgte = null;
            aAnt = null;
        }

        public CNodoListaDoble(Object pElemento)
        {
            aElemento = pElemento;
            aSgte = null;
            aAnt = null;
        }

        public CNodoListaDoble(Object pElemento, CNodoListaDoble pSgte, CNodoListaDoble pAnt)
        {
            aElemento = pElemento;
            aSgte = pSgte;
            aAnt = pAnt;
        }

        public object Elemento
        {
            set { aElemento = value; }
            get { return aElemento; }
        }

        public CNodoListaDoble Sgte
        {
            set { aSgte = value; }
            get { return aSgte; }
        }

        public CNodoListaDoble Ant
        {
            set { aAnt = value; }
            get { return aAnt; }
        }
    }
}
