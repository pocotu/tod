using System;
using System.Collections.Generic;

namespace CalculadoraApp
{
    public class Calculadora
    {
        // Metodo para evaluar una expresion matematica.
        public static double EvaluarExpresion(string expresion)
        {
            // Creamos dos pilas: 
            // una para los valores y otra para los operadores
            
            Stack<double> valores = new Stack<double>(); // Pila de valores
            Stack<char> operadores = new Stack<char>(); // Pila de operadores

            // Recorre la expresion de izquierda a derecha
            for (int i = 0; i < expresion.Length; i++)
            {
                // Obtenemos el caracter actual
                char c = expresion[i];

                // Ignora los espacios en blanco
                if (c == ' ')
                    continue;

                // Si es un digito, obtiene el numero completo y lo almacenamos en la pila de valores
                if (char.IsDigit(c))
                {
                    string numStr = c.ToString();
                    // Si el siguiente caracter es un digito o un punto decimal, lo agrega al numero
                    // y continua con el siguiente caracter de la expresion
                    while (i + 1 < expresion.Length && (char.IsDigit(expresion[i + 1]) || expresion[i + 1] == '.'))
                    {
                        // Agrega el siguiente caracter al numero
                        numStr += expresion[i + 1];
                        i++;
                    }

                    // Agrega el numero a la pila de valores
                    double num = double.Parse(numStr);
                    valores.Push(num);
                }
                // Si es un operador, lo almacenamos en la pila de operadores
                else if (EsOperador(c))
                {
                    while (operadores.Count > 0 && HasPrecedence(c, operadores.Peek()))
                    {
                        double valor2 = valores.Pop();
                        double valor1 = valores.Pop();
                        char operador = operadores.Pop();

                        double resultado = ApplyOperation(valor1, valor2, operador);
                        valores.Push(resultado);
                    }

                    operadores.Push(c);
                }
            }

            // Realizamos las operaciones restantes que quedaron en las pilas
            while (operadores.Count > 0)
            {
                double valor2 = valores.Pop();
                double valor1 = valores.Pop();
                char op = operadores.Pop();

                double resultado = ApplyOperation(valor1, valor2, op);
                valores.Push(resultado);
            }

            // El resultado final estara en la cima de la pila de valores
            return valores.Pop();
        }

        // Metodo para verificar si un caracter es un operador valido
        private static bool EsOperador(char c)
        {
            return c == '+' || c == '-' || c == '*' || c == '/';
        }

        // Metodo para verificar si el operador op2 tiene mayor precedencia que el operador op1
        private static bool HasPrecedence(char op1, char op2)
        {
            if (op2 == '(' || op2 == ')')
                return false;
            return (op1 == '*' || op1 == '/') && (op2 == '+' || op2 == '-');
        }

        // Metodo para aplicar una operacion matematica basica
        private static double ApplyOperation(double a, double b, char op)
        {
            switch (op)
            {
                case '+':
                    return a + b;
                case '-':
                    return a - b;
                case '*':
                    return a * b;
                case '/':
                    if (b == 0)
                        throw new DivideByZeroException("No se puede dividir entre cero.");
                    return a / b;
                default:
                    throw new ArgumentException("Operador invalido: " + op);
            }
        }
    }
}
