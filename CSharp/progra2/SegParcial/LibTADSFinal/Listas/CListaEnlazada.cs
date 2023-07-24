using System;

namespace Listas
{
    public class CListaEnlazada
    {
        private CNodoLista aNodo;

        public CListaEnlazada()
        {
            aNodo = null;
        }

        public bool EstaVacia()
        {
            return aNodo == null;
        }

        public void Agregar(object elemento)
        {
            CNodoLista nuevoNodo = new CNodoLista(elemento);
            nuevoNodo.Sgte = aNodo;
            aNodo = nuevoNodo;
        }

        public void Mostrar()
        {
            CNodoLista nodoActual = aNodo;
            while (nodoActual != null)
            {
                Console.WriteLine(nodoActual.Elemento.ToString());
                nodoActual = nodoActual.Sgte;
            }
        }
    }
}
