using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace appTDAPila
{
    internal class CPila
    {
        // -------------------------------------------------------
        // Atributos
        // -------------------------------------------------------
        private CNodo aCabeza; // Cabeza de la pila

        // -------------------------------------------------------
        // Constructores
        // -------------------------------------------------------
        public CPila()
        {
            aCabeza = null;
        }

        //--------------------------------------------------------
        // Propiedades
        //--------------------------------------------------------
        // Setters y Getters
        public CNodo Cabeza
        {
            get { return aCabeza; }
            set { aCabeza = value; }
        }

        // -------------------------------------------------------
        // Metodos
        // -------------------------------------------------------
        // Vacia: Indica si la pila esta vacia
        // -------------------------------------------------------
        public bool EstaVacia()
        {
            return aCabeza == null;
        }

        // -------------------------------------------------------
        // Apilar: Agrega un elemento a la pila
        // -------------------------------------------------------
        public void Apilar(int dato)
        {
            CNodo nuevoNodo = new CNodo();
            nuevoNodo.Dato = dato;
            nuevoNodo.Siguiente = aCabeza;
            aCabeza = nuevoNodo;
        }

        // -------------------------------------------------------
        // Desapilar: Elimina un elemento de la pila
        // -------------------------------------------------------
        public int Desapilar()
        {
            if (EstaVacia())
            {
                throw new InvalidOperationException("La pila esta vacia");
            }

            int datoDesapilado = aCabeza.Dato;
            aCabeza = aCabeza.Siguiente;
            return datoDesapilado;
        }

        // -------------------------------------------------------
        // MostrarElementos: Muestra los elementos de la pila
        // -------------------------------------------------------
        public void MostrarElementos()
        {
            CNodo actual = aCabeza;
            while (actual != null)
            {
                Console.WriteLine(actual.Dato);
                actual = actual.Siguiente;
            }
        }

        // -------------------------------------------------------
        // NumeroElementos: Devuelve el numero de elementos de la pila
        // -------------------------------------------------------
        public int NumeroElementos()
        {
            int count = 0;
            CNodo actual = aCabeza;
            while (actual != null)
            {
                count++;
                actual = actual.Siguiente;
            }
            return count;
        }
    }
}
