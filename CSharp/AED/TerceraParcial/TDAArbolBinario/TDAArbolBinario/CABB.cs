using System;
using System.Collections.Generic;

namespace appABB
{
    internal class CABB
    {
        //------------------------------------------------------------------------------
        // Atributos
        //------------------------------------------------------------------------------
        public CNodo raiz;
        //------------------------------------------------------------------------------
        // Constructor
        //------------------------------------------------------------------------------
        public CABB()
        {
            raiz = null;
        }
        //------------------------------------------------------------------------------
        // Métodos Principales
        //------------------------------------------------------------------------------
        public void insertarNodo(int valor)
        {
            CNodo nodoAnterior = null, nodoRecorrer = null;
            if (raiz == null)
            {
                raiz = new CNodo();
                raiz.valor = valor;
            }
            else
            {
                // Creamos un nodo
                CNodo nodoNuevo = new CNodo();
                nodoNuevo.valor = valor;
                nodoNuevo.hijoDerecho = null;
                nodoNuevo.hijoIzquierdo = null;
                // Inicializamos el recorrido
                nodoRecorrer = raiz;
                // Recorremos hasta ubicar la posición correcta
                while (nodoRecorrer != null)
                {
                    nodoAnterior = nodoRecorrer; // Guardar el nodo anterior
                    if (valor < nodoRecorrer.valor)
                    {
                        nodoRecorrer = nodoRecorrer.hijoIzquierdo;
                    }
                    else
                    {
                        nodoRecorrer = nodoRecorrer.hijoDerecho;
                    }
                }
                // Agregar el nodo nuevo
                if (valor < nodoAnterior.valor)
                {
                    nodoAnterior.hijoIzquierdo = nodoNuevo;
                }
                else
                {
                    nodoAnterior.hijoDerecho = nodoNuevo;
                }
            }
        }
        //------------------------------------------------------------------------------
        public void recorridoEnOrden(CNodo raiz)
        {
            // Recorrer el sub-árbol izquierdo
            if (raiz.hijoIzquierdo != null)
                recorridoEnOrden(raiz.hijoIzquierdo);
            // Mostrar la raiz
            Console.WriteLine(raiz.valor);
            // Recorrer el sub-árbol derecho
            if (raiz.hijoDerecho != null)
                recorridoEnOrden(raiz.hijoDerecho);
        }
        //------------------------------------------------------------------------------

        public void EliminarNodo(int valor)
        {
            raiz = EliminarNodoRecursivo(raiz, valor);
        }

        private CNodo EliminarNodoRecursivo(CNodo nodo, int valor)
        {
            if (nodo == null)
            {
                return nodo;
            }

            if (valor < nodo.valor)
            {
                nodo.hijoIzquierdo = EliminarNodoRecursivo(nodo.hijoIzquierdo, valor);
            }
            else if (valor > nodo.valor)
            {
                nodo.hijoDerecho = EliminarNodoRecursivo(nodo.hijoDerecho, valor);
            }
            else
            {
                // Caso 1: Nodo con un solo hijo o sin hijos
                if (nodo.hijoIzquierdo == null)
                {
                    return nodo.hijoDerecho;
                }
                else if (nodo.hijoDerecho == null)
                {
                    return nodo.hijoIzquierdo;
                }

                // Caso 2: Nodo con dos hijos
                nodo.valor = ValorMinimo(nodo.hijoDerecho);
                nodo.hijoDerecho = EliminarNodoRecursivo(nodo.hijoDerecho, nodo.valor);
            }
            return nodo;
        }

        private int ValorMinimo(CNodo nodo)
        {
            int minValor = nodo.valor;
            while (nodo.hijoIzquierdo != null)
            {
                minValor = nodo.hijoIzquierdo.valor;
                nodo = nodo.hijoIzquierdo;
            }
            return minValor;
        }
    }
}