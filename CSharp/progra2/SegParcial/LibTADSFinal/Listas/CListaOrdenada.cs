using System;

namespace Listas
{
    public class CListaOrdenada
    {
        private CNodoLista? aNodo;

        public CListaOrdenada()
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

            if (EstaVacia() || Comparar(elemento, aNodo.Elemento) < 0)
            {
                nuevoNodo.Sgte = aNodo;
                aNodo = nuevoNodo;
            }
            else
            {
                CNodoLista nodoActual = aNodo;
                while (nodoActual.Sgte != null && Comparar(elemento, nodoActual.Sgte.Elemento) >= 0)
                {
                    nodoActual = nodoActual.Sgte;
                }

                nuevoNodo.Sgte = nodoActual.Sgte;
                nodoActual.Sgte = nuevoNodo;
            }
        }

        private int Comparar(object elemento1, object elemento2)
        {
            // Implementa tu lógica de comparación personalizada aquí.
            // Por ejemplo, si los elementos son enteros, podrías usar:
            // return ((int)elemento1).CompareTo((int)elemento2);
            // Para mantener el ejemplo simple, asumimos que los elementos son comparables.
            return ((IComparable)elemento1).CompareTo(elemento2);
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
