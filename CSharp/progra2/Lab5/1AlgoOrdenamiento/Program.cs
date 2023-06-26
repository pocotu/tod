using System;
using System.Diagnostics;

namespace App2
{
    class COrdenamiento
    {
        // Atributos
        private int[] aarreglo;
        private int an;

        public COrdenamiento(int[] parreglo)
        {
            this.aarreglo = parreglo;
            this.an = parreglo.Length;
        }

        public COrdenamiento(int pn)
        {
            int[] aux = new int[pn];
            Random rand = new Random();
            for (int i = 0; i < pn; i++)
            {
                aux[i] = rand.Next(0, 100);
            }
            aarreglo = aux;
            an = pn;
        }

        // Propiedades
        public int[] Arreglo
        {
            get => aarreglo;
            set => aarreglo = value;
        }
        public int N
        {
            get => an;
            set => an = value;
        }

        // Métodos
        public void swap(ref int a, ref int b)
        {
            int temp = a;
            a = b;
            b = temp;
        }

        public int[] OrdenamientoInsersion()
        {
            for (int i = 1; i < N; ++i)
            {
                int x = Arreglo[i];
                int j = i - 1;

                while (j >= 0 && aarreglo[j] > x)
                {
                    Arreglo[j + 1] = Arreglo[j];
                    j = j - 1;
                }
                Arreglo[j + 1] = x;
            }
            return Arreglo;
        }

        public int[] OrdenamientoSeleccion()
        {
            int min_pos;
            for (int i = 0; i < N; i++)
            {
                min_pos = i;
                for (int x = i + 1; x < N; x++)
                {
                    if (Arreglo[x] < Arreglo[min_pos])
                    {
                        min_pos = x;
                    }
                }
                if (min_pos != i)
                {
                    swap(ref Arreglo[min_pos], ref Arreglo[i]);
                }
            }
            return Arreglo;
        }

        public int[] OrdenamientoBurbuja()
        {
            for (int i = 0; i < N - 1; i++)
            {
                for (int x = 0; x < N - i - 1; x++)
                {
                    if (Arreglo[x] > Arreglo[x + 1])
                    {
                        swap(ref Arreglo[x], ref Arreglo[x + 1]);
                    }
                }
            }
            return Arreglo;
        }

        static void Main(string[] args)
        {
            int n = 1000;

            int[] arrB = new int[n];
            int[] arrI = new int[n];
            int[] arrS = new int[n];
            Random rand = new Random();
            for (int i = 0; i < n; i++)
            {
                int num = rand.Next(0, 100);
                arrB[i] = num;
                arrI[i] = num;
                arrS[i] = num;
            }
            COrdenamiento ordB = new COrdenamiento(arrB);
            COrdenamiento ordS = new COrdenamiento(arrS);
            COrdenamiento ordI = new COrdenamiento(arrI);

            Stopwatch stopwatch = new Stopwatch();

            Console.WriteLine("#### Ordenamiento Burbuja ####");
            stopwatch.Start();
            int[] resB = ordB.OrdenamientoBurbuja();
            stopwatch.Stop();
            for (int i = 0; i < n; i++)
            {
                Console.Write(" " + resB[i]);
            }
            Console.WriteLine("\nEl tiempo transcurrido es {0} ms", stopwatch.ElapsedMilliseconds / 1000.0);

            Console.WriteLine("\n#### Ordenamiento Seleccion ####");
            stopwatch.Reset();
            stopwatch.Start();
            int[] resS = ordS.OrdenamientoSeleccion();
            stopwatch.Stop();
            for (int i = 0; i < n; i++)
            {
                Console.Write(" " + resS[i]);
            }
            Console.WriteLine("\nEl tiempo transcurrido es {0} ms", stopwatch.ElapsedMilliseconds / 1000.0);

            Console.WriteLine("\n#### Ordenamiento Insercion ####");
            stopwatch.Reset();
            stopwatch.Start();
            int[] resI = ordI.OrdenamientoInsersion();
            stopwatch.Stop();
            for (int i = 0; i < n; i++)
            {
                Console.Write(" " + resI[i]);
            }
            Console.WriteLine("\nEl tiempo transcurrido es {0} ms", stopwatch.ElapsedMilliseconds / 1000.0);
        }
    }
}