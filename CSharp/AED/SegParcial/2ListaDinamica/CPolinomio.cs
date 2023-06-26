using System;

namespace ListaDinamica
{
internal class CPolinomio // Px = 3x^4 + 5x^2 + 6x + 2
    {
        private double[] coeficientes;

        // constructor
        public CPolinomio(params double[] coeficientes)
        {
            this.coeficientes = coeficientes;
        }

        // metodos
        public void Mostrar()
        {
            Console.Write("Polinomio: ");
            // se asume que el primer coeficiente es el de mayor grado
            int grado = coeficientes.Length - 1;
            // se recorre el arreglo de coeficientes de mayor a menor grado
            for (int i = coeficientes.Length - 1; i >= 0; i--)
            {
                if (coeficientes[i] != 0)
                {
                    Console.Write($"{coeficientes[i]}x^{i} ");
                    if (i != 0)
                    {
                        Console.Write("+ ");
                    }
                }
            }
            Console.WriteLine();
        }

        // evaluar el polinomio en X
        public double Evaluar(double x)
        {
            double resultado = 0;
            int grado = coeficientes.Length - 1;
            // inicia un ciclo desde el coeficiente de mayor grado
            for (int i = coeficientes.Length - 1; i >= 0; i--)
            {
                resultado += coeficientes[i] * Math.Pow(x, i);
            }

            return resultado;
        }
    }
}