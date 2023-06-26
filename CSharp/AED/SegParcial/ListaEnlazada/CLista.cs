using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace appListaEnlazada
{
    internal class CLista
    {
        //--------------------------------------------------
        // Atributos:
        //--------------------------------------------------
        // Se crea un objeto de tipo CNodo que será la cabeza
        // de la lista enlazada simple
        //--------------------------------------------------
        private CNodo aCabeza; // Cabeza de la lista

        //--------------------------------------------------
        // Propiedades
        //--------------------------------------------------
        public CNodo Cabeza
        {
            get { return aCabeza; }
            set { aCabeza = value; }
        }

        //--------------------------------------------------
        // Constructores:
        //--------------------------------------------------
        // Se inicializa la cabeza de la lista enlazada simple
        // como nula
        //--------------------------------------------------
        public CLista()
        {
            aCabeza = null;
        }

        //--------------------------------------------------
        // Métodos
        //--------------------------------------------------

        //--------------------------------------------------
        // Insertar un nodo al INICIO de la Lista:
        //--------------------------------------------------
        public void InsertarAlInicio(int Elemento)
        {
            // Crear un nodo auxiliar
            CNodo Auxiliar = new CNodo();
            // Asignarle el dato al nodo auxiliar
            Auxiliar.Dato = Elemento;
            // Asignarle el siguiente al nodo auxiliar
            Auxiliar.Siguiente = null;
            if (Cabeza == null)
            { // La lista ES vacía
                Cabeza = Auxiliar; // Hacemos que el nodo sea parte de la lista
            }
            else
            { // La lista NO ES vacía
                CNodo Puntero; // Puntero que nos permite insertar el nodo en la lista
                Puntero = Cabeza; // Puntero apunta donde apunta la cabeza de la lista
                Cabeza = Auxiliar; // Cabeza apunta a Auxilizar
                // El puntero auxiliar ahora es la cabeza, y tenemos que enlazar con el 
                // nodo que era antes cabeza
                Auxiliar.Siguiente = Puntero;
            }
        }

        //--------------------------------------------------
        // Insertar un nodo en una POSICIÓN de la Lista
        //--------------------------------------------------
        public void InsertarEnPosicion(int Elemento, int Posicion)
        {
            // Crear un nodo auxiliar
            CNodo Auxiliar = new CNodo();
            Auxiliar.Dato = Elemento;
            Auxiliar.Siguiente = null;
            if (Cabeza == null)
            { // La lista ES vacia
                Cabeza = Auxiliar; // Hacemos que el nodo sea parte de la lista
            }
            else
            { // La lista NO ES vacia
                CNodo Puntero; // Puntero que nos permite insertar el nodo en la lista
                Puntero = Cabeza; // Puntero apunta donde apunta la cabeza de la lista
                int Contador = 0;
                while (Puntero.Siguiente != null && Contador < Posicion)
                {
                    Puntero = Puntero.Siguiente;
                    Contador++;
                }
                // El puntero auxiliar ahora es la cabeza, y tenemos que enlazar con el 
                // nodo que era antes cabeza
                Auxiliar.Siguiente = Puntero.Siguiente;
                Puntero.Siguiente = Auxiliar;
            }
        }

        //--------------------------------------------------
        // Insertar un nodo al FINAL de la Lista
        //--------------------------------------------------
        public void InsertarAlFinal(int Elemento)
        {
            // Crear un nodo auxiliar
            CNodo Auxiliar = new CNodo();
            Auxiliar.Dato = Elemento;
            Auxiliar.Siguiente = null;
            if (Cabeza == null)
            { // La lista ES vacía
                Cabeza = Auxiliar; // Hacemos que el nodo sea parte de la lista
            }
            else
            { // La lista NO ES vacía
                CNodo Puntero; // Puntero que nos permite insertar el nodo en la lista
                Puntero = Cabeza; // Puntero apunta donde apunta la cabeza de la lista
                while (Puntero.Siguiente != null)
                {
                    Puntero = Puntero.Siguiente;
                }
                // El puntero auxiliar ahora es la cabeza, y tenemos que enlazar con el 
                // nodo que era antes cabeza
                Puntero.Siguiente = Auxiliar;
            }
        }

        //--------------------------------------------------
        // Eliminar el PRIMER nodo de la Lista
        //--------------------------------------------------
        public void EliminarCabeza()
        {
            if (Cabeza == null)
            { // Lista ES vacía
                Console.WriteLine("ERROR: La lista está vacía, no existe cabeza...");
            }
            else
            { // Lista NO ES vacía
                // Cabeza apunta hacia donde estaba apuntando Cabeza.Siguiente
                // (hacia el segundo nodo)
                Cabeza = Cabeza.Siguiente;
            }
        }

        //--------------------------------------------------
        // Eliminar el ULTIMO nodo de la Lista
        //-------------------------------------------------
        public void EliminarCola()
        {
            if (Cabeza == null)
            { // Lista ES vacía
                Console.WriteLine("ERROR: La lista está vacia, no existe cabeza...");
            }
            else
            { // Lista NO ES vacía
                CNodo Puntero; // Puntero que nos permite insertar el nodo en la lista
                Puntero = Cabeza; // Puntero apunta donde apunta la cabeza de la lista
                while (Puntero.Siguiente.Siguiente != null)
                {
                    Puntero = Puntero.Siguiente;
                }
                // El puntero auxiliar ahora es la cabeza, y tenemos que enlazar con el 
                // nodo que era antes cabeza
                Puntero.Siguiente = null;
            }
        }

        //--------------------------------------------------
        // Eliminar un nodo por ELEMENTO de la Lista
        //--------------------------------------------------
        public void EliminarElemento(int Elemento)
        {
            if (Cabeza == null)
            { // Lista ES vacía
                Console.WriteLine("ERROR: La lista está vacía, no existe cabeza...");
            }
            else
            { // Lista NO ES vacía
                CNodo Puntero; // Puntero que nos permite insertar el nodo en la lista
                Puntero = Cabeza; // Puntero apunta donde apunta la cabeza de la lista
                while (Puntero.Siguiente.Dato != Elemento)
                {
                    Puntero = Puntero.Siguiente;
                }
                // El puntero auxiliar ahora es la cabeza, y tenemos que enlazar con el 
                // nodo que era antes cabeza
                Puntero.Siguiente = Puntero.Siguiente.Siguiente;
            }
        }

        //--------------------------------------------------
        // Mostrar los nodos de una lista
        //--------------------------------------------------
        public void Mostrar()
        {
            if (Cabeza == null)
            { // La lista ES vacía
                Console.WriteLine("La lista está vacía...");
            }
            else
            { // La lista NO ES vacía
                CNodo Puntero; // Nodo para recorrer la lista
                Puntero = Cabeza; // Nodo Puntero apunta donde apunta cabeza
                Console.Write("{0} ->", Puntero.Dato);
                while (Puntero.Siguiente != null)
                {
                    Puntero = Puntero.Siguiente;
                    Console.Write("{0} ->", Puntero.Dato);
                }

                Console.WriteLine();
            }
        }
    }
}
