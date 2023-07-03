using System;
using System.Diagnostics;

namespace Busqueda
{
    class Comparacion
    {
        private int[] lista;
        private int valorBuscado;

        public Comparacion(int[] lista, int valorBuscado)
        {
            this.lista = lista;
            this.valorBuscado = valorBuscado;
        }

        public void RealizarComparacion()
        {
            // Busqueda secuencial
            Stopwatch stopwatchSecuencial = new Stopwatch();
            stopwatchSecuencial.Start();
            int posicionSecuencial = BusquedaSecuencial(lista, valorBuscado);
            stopwatchSecuencial.Stop();
            TimeSpan tiempoSecuencial = stopwatchSecuencial.Elapsed;

            Console.WriteLine("Busqueda secuencial:");
            ImprimirResultado(valorBuscado, posicionSecuencial);
            Console.WriteLine("Tiempo de ejecucion: " + tiempoSecuencial.TotalMilliseconds + " ms");

            Console.WriteLine();

            // Busqueda binaria
            Stopwatch stopwatchBinaria = new Stopwatch();
            stopwatchBinaria.Start();
            int posicionBinaria = BusquedaBinaria(lista, valorBuscado);
            stopwatchBinaria.Stop();
            TimeSpan tiempoBinaria = stopwatchBinaria.Elapsed;

            Console.WriteLine("Busqueda binaria:");
            ImprimirResultado(valorBuscado, posicionBinaria);
            Console.WriteLine("Tiempo de ejecucion: " + tiempoBinaria.TotalMilliseconds + " ms");
        }

        public int BusquedaSecuencial(int[] lista, int valorBuscado)
        {
            for (int i = 0; i < lista.Length; i++)
            {
                if (lista[i] == valorBuscado)
                {
                    return i; // Se encontro el valor, se retorna la posicion
                }
            }
            return -1; // El valor no se encontro en la lista
        }

        public static void ImprimirResultado(int valorBuscado, int posicion)
        {
            if (posicion != -1)
            {
                Console.WriteLine("El valor {0} se encontro en la posicion {1}", valorBuscado, posicion);
            }
            else
            {
                Console.WriteLine("El valor {0} no se encontro en la lista", valorBuscado);
            }
        }

        public int BusquedaBinaria(int[] lista, int valorBuscado)
        {
            int inicio = 0;
            int fin = lista.Length - 1;

            while (inicio <= fin)
            {
                int medio = (inicio + fin) / 2;

                if (lista[medio] == valorBuscado)
                {
                    return medio; // Se encontro el valor, se retorna la posicion
                }
                else if (lista[medio] < valorBuscado)
                {
                    inicio = medio + 1; // El valor buscado esta en la mitad derecha
                }
                else
                {
                    fin = medio - 1; // El valor buscado está en la mitad izquierda
                }
            }
            return -1; // El valor no se encontro en la lista
        }
    }
}
