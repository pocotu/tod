// Escribir un programa que calcule el factorial de
// un numero dado de manera iterativa (no recursiva)

using System;

// se define el namespace Factorial
// namespace es un contenedor de clases
namespace Factorial
{
    class Program
    {
        static void Main(string[] args)
        {
            // se definen las variables a utilizar
            int numero;
            int factorial; 
            factorial = 1;

            // se pide el numero al usuario
            Console.Write("Ingrese un numero: ");
            // se lee el numero ingresado por el usuario y se convierte a entero
            numero = Convert.ToInt32(Console.ReadLine());

            for (int i = 1; i <= numero; i++)
            {
                factorial *= i;
            }

            Console.WriteLine("El factorial es: {1}", numero, factorial);
        }
    }
}
