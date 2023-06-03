// Crea una clase Fracción, que contenga que represente un número racional que tenga como parámetros un numerador y denominador:
// 2.1. Implementar los 2 respectivos constructores, el cual puede contender parámetros ingresados por el usuario o 
//      cuando no se ingresen parámetros, tanto el numerador como denominador será igual a 1. Implementar 
//      sus correspondientes Getters y Setters para los atributos.
// 2.2. Implementar los métodos: Sumar(), Restar(), Multiplicar() y Dividir() que permita realizar las 4 operaciones 
//      básicas con 2 números racionales (Implementarlo como método de instancia, método de clase y sobrecarga de 
//      operaciones). Al mostrar los resultados se deberán mostrar como fracciones simplificadas.
// 2.3. Implementar los métodos correspondientes a los operadores de comparación (Implementarlo como método de 
//      instancia, método de clase y sobrecarga de operaciones).

using System;

namespace Francciones
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Fraccion fraccion1 = new Fraccion(1, 2);
            Fraccion fraccion2 = new Fraccion(3, 4);

            Fraccion resultado = fraccion1.Sumar(fraccion2);
            Console.WriteLine($"Suma: {fraccion1} + {fraccion2} = {resultado}");

            resultado = fraccion1.Restar(fraccion2);
            Console.WriteLine($"Resta: {fraccion1} - {fraccion2} = {resultado}");

            resultado = fraccion1.Multiplicar(fraccion2);
            Console.WriteLine($"Multiplicación: {fraccion1} * {fraccion2} = {resultado}");

            resultado = fraccion1.Dividir(fraccion2);
            Console.WriteLine($"División: {fraccion1} / {fraccion2} = {resultado}");

            resultado = fraccion1 + fraccion2;
            Console.WriteLine($"Suma (sobrecarga de operador): {fraccion1} + {fraccion2} = {resultado}");

            resultado = fraccion1 - fraccion2;
            Console.WriteLine($"Resta (sobrecarga de operador): {fraccion1} - {fraccion2} = {resultado}");

            resultado = fraccion1 * fraccion2;
            Console.WriteLine($"Multiplicación (sobrecarga de operador): {fraccion1} * {fraccion2} = {resultado}");

            resultado = fraccion1 / fraccion2;
            Console.WriteLine($"División (sobrecarga de operador): {fraccion1} / {fraccion2} = {resultado}");

            bool esMayor = fraccion1.EsMayorQue(fraccion2);
            Console.WriteLine($"{fraccion1} es mayor que {fraccion2}? {esMayor}");

            bool esMenor = fraccion1.EsMenorQue(fraccion2);
            Console.WriteLine($"{fraccion1} es menor que {fraccion2}? {esMenor}");

            bool esIgual = fraccion1.EsIgualA(fraccion2);
            Console.WriteLine($"{fraccion1} es igual a {fraccion2}? {esIgual}");
        }
    }
}
