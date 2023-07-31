using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AppPlaya
{
    public class CCola
    {
        // Atributos
        private Object elemento;
        private CCola subCola;
        
        // Constructores
        public CCola()
        {
            this.elemento = null;
            this.subCola = null;
        }

        private CCola(Object elemento, CCola subCola)
        {
            this.elemento = elemento;
            this.subCola = subCola;
        }

        // Metodos
        public bool esVacia()
        {
            return elemento == null;
        }
        public void agregar(Object elemento)
        {
            if (esVacia())
            {
                this.elemento = elemento;
                this.subCola = new CCola();
            }
            else
                this.subCola.agregar(elemento);
        }
        public void avanzar()
        {
            if (!esVacia())
            {
                elemento = subCola.elemento;
                subCola = subCola.subCola;
            }
        }
        public Object primero()
        {
            return elemento;
        }
    }
}
