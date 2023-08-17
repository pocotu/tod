using System;
using System.Collections.Generic;

namespace SistemaTienda
{
    public class cCola<T>
    {
        private Queue<T> items = new Queue<T>();

        public void Encolar(T item)
        {
            items.Enqueue(item);
        }

        public T Desencolar()
        {
            if (items.Count == 0)
                throw new InvalidOperationException("La cola esta vacia");

            return items.Dequeue();
        }

        public int Conteo
        {
            get { return items.Count; }
        }
    }
}
