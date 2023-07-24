using System;

namespace Listas
{
    public class CListaDobleEnlazada
    {
        private CNodoListaDoble aNodo;

        public CListaDobleEnlazada()
        {
            aNodo = null;
        }

        public bool EstaVacia()
        {
            return aNodo == null;
        }

        public void Agregar(object elemento)
        {
            CNodoListaDoble nuevoNodo = new CNodoListaDoble(elemento);
            nuevoNodo.Sgte = aNodo;
            if (aNodo != null)
            {
                aNodo.Ant = nuevoNodo;
            }
            aNodo = nuevoNodo;
        }

        public void Mostrar()
        {
            CNodoListaDoble nodoActual = aNodo;
            while (nodoActual != null)
            {
                Console.WriteLine(nodoActual.Elemento.ToString());
                nodoActual = nodoActual.Sgte;
            }
        }
    }
}
