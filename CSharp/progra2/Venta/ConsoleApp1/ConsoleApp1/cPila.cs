using System;
using System.Collections.Generic;

namespace SistemaTienda
{
    public class cPila<T>
    {
        private List<T> items = new List<T>();

        // Agregar un elemento a la pila
        public void Push(T item)
        {
            items.Add(item);
        }

        // Eliminar un elemento de la pila
        public T Pop()
        {
            if (items.Count == 0)
                throw new InvalidOperationException("La pila esta vacia");

            T item = items[items.Count - 1];
            items.RemoveAt(items.Count - 1);
            return item;
        }

        // Contar los elementos de la pila
        public int Count
        {
            get { return items.Count; }
        }
    }
}
