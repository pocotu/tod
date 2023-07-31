using System;

namespace CalculadoraApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("#### Calculadora de Expresiones #####");
            Console.WriteLine("Ingrese una expresión matemática para evaluar:");
            Console.WriteLine("Ejemplo: 2 + 3 * 4 - 5 ^ 2");
            Console.Write("> ");

            // Obtiene la expresion a evaluar desde la consola
            // Si no se ingresa nada, asigna un string vacio a la variable expresion
            // y continúa con la ejecucion del programa
            string expresion = Console.ReadLine() ?? string.Empty;

            try
            {
                double resultado = Calculadora.EvaluarExpresion(expresion);
                Console.WriteLine("El resultado de la expresion es: " + resultado);
            }
            // Si ocurre un error, muestra el mensaje de error
            catch (Exception ex)
            {
                Console.WriteLine("Error: " + ex.Message);
            }
        }
    }
}