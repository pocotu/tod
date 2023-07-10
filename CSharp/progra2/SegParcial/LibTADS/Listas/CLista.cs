using LibTADS;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Listas
{
    public class CLista : ILista
    {
        // Nodo inicial de la lista
        private CNodoLista aNodo; 

        public CLista()
        {
            // Inicializa la lista vacia
            aNodo = null; 
        }

        public bool EstaVacia()
        {
            // Verifica si la lista está vacia
            return aNodo == null;
        }

        public int Longitud()
        {
            // Calcula la longitud de la lista de forma recursiva
            return LongitudRecursiva(aNodo); 
        }

        private int LongitudRecursiva(CNodoLista nodo)
        {
            if (nodo == null)
                return 0; // Caso base: el nodo es nulo, devuelve 0

            // Llamada recursiva para contar los nodos restantes
            return 1 + LongitudRecursiva(nodo.Sgte);
        }

        public void Agregar(object elemento)
        {
            // Agrega un elemento a la lista de forma recursiva
            aNodo = AgregarRecursivo(aNodo, elemento); 
        }

        private CNodoLista AgregarRecursivo(CNodoLista nodo, object elemento)
        {
            if (nodo == null)
                // Caso base: el nodo es nulo, crea un nuevo nodo y lo devuelve
                return new CNodoLista(elemento); 

            // Llamada recursiva para avanzar al siguiente nodo y agregar el elemento
            nodo.Sgte = AgregarRecursivo(nodo.Sgte, elemento);
            return nodo;
        }

        public object Iesimo(int posicion)
        {
            if (posicion < 1 || posicion > Longitud())
            {
                Console.WriteLine("ERROR: Posición incorrecta");
                // Si la posición es incorrecta, muestra un mensaje de error y devuelve null
                return null; 
            }

            // Obtiene el elemento en la posición especificada de forma recursiva
            return IesimoRecursivo(aNodo, posicion, 1);
        }

        private object IesimoRecursivo(CNodoLista nodo, int posicion, int contador)
        {
            if (contador == posicion)
                // Caso base: se encontro la posicion, devuelve el elemento del nodo actual
                return nodo.Elemento; 

            // Llamada recursiva para avanzar al siguiente nodo y buscar la posicion
            return IesimoRecursivo(nodo.Sgte, posicion, contador + 1);
        }

        public void Mostrar()
        {
            if (EstaVacia())
            {
                // Si la lista está vacía, muestra un mensaje
                Console.WriteLine("Lista vacía"); 
                return;
            }

            // Muestra los elementos de la lista de forma recursiva
            MostrarRecursivo(aNodo); 
        }

        private void MostrarRecursivo(CNodoLista nodo)
        {
            // Muestra el elemento del nodo actual
            Console.WriteLine(nodo.Elemento.ToString()); 

            if (nodo.Sgte != null)
                // Llamada recursiva para mostrar el siguiente nodo si no es nulo
                MostrarRecursivo(nodo.Sgte); 
        }

        public void Insertar(object elemento, int posicion)
        {
            if (posicion < 1 || posicion > Longitud() + 1)
            {
                Console.WriteLine("ERROR: Posición incorrecta");
                // Si la posición es incorrecta, muestra un mensaje de error y retorna
                return; 
            }

            // Inserta un elemento en la posición especificada de forma recursiva
            aNodo = InsertarRecursivo(aNodo, elemento, posicion, 1); 
        }

        private CNodoLista InsertarRecursivo(CNodoLista nodo, object elemento, int posicion, int contador)
        {
            if (contador == posicion)
                // Caso base: se encontro la posicion, crea un nuevo nodo y lo enlaza con el nodo actual
                return new CNodoLista(elemento, nodo); 

            // Llamada recursiva para avanzar al siguiente nodo y buscar la posición
            nodo.Sgte = InsertarRecursivo(nodo.Sgte, elemento, posicion, contador + 1);
            return nodo;
        }

        public int Ubicacion(object elemento)
        {
            // Busca la ubicacion de un elemento en la lista de forma recursiva
            return UbicacionRecursiva(aNodo, elemento, 1); 
        }

        private int UbicacionRecursiva(CNodoLista nodo, object elemento, int posicion)
        {
            if (nodo == null)
                return -1; // Caso base: el nodo es nulo, el elemento no está en la lista

            if (nodo.Elemento.Equals(elemento))
                // Caso base: se encontro el elemento, devuelve la posicion actual
                return posicion; 

            // Llamada recursiva para avanzar al siguiente nodo y buscar el elemento
            return UbicacionRecursiva(nodo.Sgte, elemento, posicion + 1);
        }

        public void Eliminar(int posicion)
        {
            if (posicion < 1 || posicion > Longitud())
            {
                Console.WriteLine("ERROR: Posición fuera de rango");
                // Si la posicion es incorrecta, muestra un mensaje de error y retorna
                return; 
            }

            // Elimina un elemento en la posicion especificada de forma recursiva
            aNodo = EliminarRecursivo(aNodo, posicion, 1); 
        }

        private CNodoLista EliminarRecursivo(CNodoLista nodo, int posicion, int contador)
        {
            if (contador == posicion - 1)
            {
                if (nodo.Sgte != null)
                    // Caso base: se encontro el nodo anterior al que se va a eliminar, actualiza el enlace para saltar el nodo a eliminar
                    nodo.Sgte = nodo.Sgte.Sgte; 
                return nodo;
            }

            if (nodo != null)
                // Llamada recursiva para avanzar al siguiente nodo y eliminar el nodo deseado
                nodo.Sgte = EliminarRecursivo(nodo.Sgte, posicion, contador + 1); 

            return nodo;
        }

        public void Eliminar(object elemento)
        {
            // Busca la posicion del elemento en la lista
            int posicion = Ubicacion(elemento); 
            if (posicion != -1)
                // Si se encontro el elemento, llama al metodo Eliminar para eliminarlo
                Eliminar(posicion); 
        }
    }
}
