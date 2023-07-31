using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AppArbolBinario
{
    internal class CNodo
    {
        // Atributos
        public int info;
        public CNodo izq, der;

        // Constructor
        public CNodo(int data)
        {
            info = data;
            izq = null;
            der = null;
        }
    }
}
