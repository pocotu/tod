using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace appTDAPila
{
    internal class CNodo
    {
        // -------------------------------------------------------
        // Atributos
        // -------------------------------------------------------
        private int aDato; // Dato del nodo
        private CNodo aSiguiente; // Apuntador del nodo
        
        //--------------------------------------------------------
        // Propiedades
        //--------------------------------------------------------
        //Setters y Getters
        public int Dato
        {
            get { return aDato; }
            set { aDato = value; }
        }
        public CNodo Siguiente
        {
            get { return aSiguiente; }
            set { aSiguiente = value; }
        }
    }
}