using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace appTDACola
{
    internal class CCola
    {
        // -------------------------------------------------------
        // Atributos
        // -------------------------------------------------------
        private CNodo aCabeza; // Cabeza de la cola                       
        
        // -------------------------------------------------------
        // Constructores
        // -------------------------------------------------------
        public CCola()
        {
            aCabeza = null;
        }

        //--------------------------------------------------------
        // Propiedades
        //--------------------------------------------------------
        //Setters y Getters
        public CNodo Cabeza
        {
            get { return aCabeza; }
            set { aCabeza = value; }
        }
        // -------------------------------------------------------
        // Insertar un elemento al INICIO de la cola
        // -------------------------------------------------------
        public void Insertar(int Elemento)
        {
            // Crear un nodo Auxiliar
            CNodo Auxiliar = new CNodo();
            Auxiliar.Dato = Elemento;
            Auxiliar.Siguiente = null;
            if (Cabeza == null)
            { // La lista ES vacia
                Cabeza = Auxiliar; // Hacemos que el Nodo sea parte de la lista
            }
            else
            { // La lista NO ES vacia
                CNodo Puntero; // Nodo para recorrer la lista
                Puntero = Cabeza; // Nodo apunta donde apunta Cabeza
                Cabeza = Auxiliar; // Cabeza apunta donde apunta Auxiliar
                // El puntero de Auxiliar que ahora es Cabeza, se enlaza con el nodo
                // que era antes la cabeza y que tiene apuntador puntero
                Auxiliar.Siguiente = Puntero;
            }
        }

        // -------------------------------------------------------
        // Implementar el método Atender, que permita extraer el 
        // primer elemento de la cola
        // -------------------------------------------------------
        public void Atender()
        {
            if (Cabeza == null)
            { // Si la cola esta vacia
                Console.WriteLine("La Cola esta vacia");
            }
            else
            { // La cola NO ES vacia
                CNodo Puntero; // Nodo para recorrer la cola
                Puntero = Cabeza; // Nodo apunta donde apunto Cabeza
                Cabeza = Puntero.Siguiente; // Cabeza apunta donde apunta el siguiente de Puntero
                Puntero = null; // Eliminamos el nodo Puntero
            }
        }

        // -------------------------------------------------------
        // Implementar el método PrimerElemento, que permita MOSTRAR 
        // el PRIMER elemento de la cola
        // -------------------------------------------------------
        public void PrimerElemento()
        {
            if (Cabeza == null)
            { // Si la cola esta vacia
                Console.WriteLine("La Cola está vacía");
            }
            else
            { // si la cola no esta vacia
                CNodo Puntero; // Nodo para recorrer la cola
                Puntero = Cabeza; // Nodo apunta donde apunto Cabeza
                Console.WriteLine("El primer elemento de la cola es: {0}", Puntero.Dato);
            }
        }

        // -------------------------------------------------------
        // Implementar el método ÚltimoElemento, que permita MOSTRAR 
        // el ULTIMO elemento de la cola.
        // -------------------------------------------------------
        public void UltimoElemento()
        {
            if (Cabeza == null)
            { // Si la cola esta vacia
                Console.WriteLine("La Cola está vacía...");
            }
            else
            { // Si la cola no esta vacia
                CNodo Puntero; // Nodo para recorrer la cola
                Puntero = Cabeza; // Nodo apunta donde apunto Cabeza
                while (Puntero.Siguiente != null)
                {
                    Puntero = Puntero.Siguiente;
                }
                Console.WriteLine("El último elemento de la cola es: {0}", Puntero.Dato);
            }
        }

        // -------------------------------------------------------
        // Implementar el método LongitudCola, que permita MOSTRAR 
        // la cantidad de elementos de la cola.
        // -------------------------------------------------------
        public void LongitudCola()
        {
            if (Cabeza == null)
            { // Si la cola esta vacia
                Console.WriteLine("La Cola esta vacia");
            }
            else
            { // Si la cola no esta vacia
                CNodo Puntero; // Nodo para recorrer la cola
                Puntero = Cabeza; // Nodo apunta donde apunto Cabeza
                int Contador = 0;
                while (Puntero != null)
                {
                    Puntero = Puntero.Siguiente;
                    Contador++;
                }
                Console.WriteLine("La longitud de la cola es: {0}", Contador);
            }
        }

        // -------------------------------------------------------
        // Mostrar los elementos de la cola
        // -------------------------------------------------------
        public void Mostrar()
        {
            if (Cabeza == null)
            { // Si la cola esta vacia
                Console.WriteLine("La Cola está vacía...");
            }
            else
            { // Si la cola no esta vacia
                CNodo Puntero; // Nodo para recorrer la cola
                Puntero = Cabeza; // Nodo apunta donde apunto Cabeza
                Console.Write("{0} -> \t", Puntero.Dato); // Mostrar el atributo Dato del Nodo
                while (Puntero.Siguiente != null)
                {
                    Puntero = Puntero.Siguiente;
                    Console.Write("{0} -> \t", Puntero.Dato);
                }
            }
            Console.WriteLine();
        }
    }
}