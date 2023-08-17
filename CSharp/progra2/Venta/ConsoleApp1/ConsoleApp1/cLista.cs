using System;
using System.Collections;
using System.Collections.Generic;

namespace SistemaTienda
{
    public class cLista<T> : IEnumerable<T>
    {
        private List<T> items = new List<T>();

        // Agregar un elemento a la lista
        public void Agregar(T item)
        {
            items.Add(item);
        }

        public void Eliminar(T item)
        {
            items.Remove(item);
        }

        public int Conteo
        {
            get { return items.Count; }
        }

        public T this[int index]
        {
            get { return items[index]; }
        }

        // Implementación de IEnumerable para poder usar foreach
        public IEnumerator<T> GetEnumerator()
        {
            return items.GetEnumerator();
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return (IEnumerator)GetEnumerator();
        }
    }
}
