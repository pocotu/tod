using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace appTDACola
{
    internal class CNodo
    {
        //-------------------------------------------------
        // Atributos
        //-------------------------------------------------
        private int aDato;          // Dato del Nodo
        private CNodo aSiguiente;   // Puntero del Nodo

        //-------------------------------------------------
        // Propiedades
        //-------------------------------------------------
        // Getters y Setters
        //-------------------------------------------------
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