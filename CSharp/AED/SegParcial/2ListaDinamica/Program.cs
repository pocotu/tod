using System;

namespace ListaDinamica
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // coeficientes del polinomio
            CPolinomio polinomio = new CPolinomio(2, 6, 5, 0, 3);

            polinomio.Mostrar();

            // evaluar el polinomio en X
            double x = 4;
            double resultado = polinomio.Evaluar(x);
            Console.WriteLine($"Polinomio evaluado en x = {x} es: {resultado}");

            Console.ReadKey();
        }
    }
}
