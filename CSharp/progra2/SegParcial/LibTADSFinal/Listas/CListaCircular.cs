using System;

namespace Listas
{
    public class CListaCircular
    {
        private CNodoListaCircular aNodo;

        public CListaCircular()
        {
            aNodo = null;
        }

        public bool EstaVacia()
        {
            return aNodo == null;
        }

        public void Agregar(object elemento)
        {
            if (EstaVacia())
            {
                aNodo = new CNodoListaCircular(elemento);
                aNodo.Sgte = aNodo;
            }
            else
            {
                CNodoListaCircular nuevoNodo = new CNodoListaCircular(elemento);
                nuevoNodo.Sgte = aNodo.Sgte;
                aNodo.Sgte = nuevoNodo;
                aNodo = nuevoNodo;
            }
        }

        public void Mostrar()
        {
            if (EstaVacia())
            {
                Console.WriteLine("Lista vacía");
                return;
            }

            CNodoListaCircular nodoActual = aNodo.Sgte;
            do
            {
                Console.WriteLine(nodoActual.Elemento.ToString());
                nodoActual = nodoActual.Sgte;
            } while (nodoActual != aNodo.Sgte);
        }
    }
}
