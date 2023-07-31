using System;
using System.Collections.Generic;

namespace CalculadoraApp
{
    public class Calculadora
    {
        public static double EvaluarExpresion(string expresion)
        {
            Stack<double> valores = new Stack<double>();
            Stack<char> operadores = new Stack<char>();

            for (int i = 0; i < expresion.Length; i++)
            {
                char c = expresion[i];

                if (c == ' ')
                    continue;

                if (char.IsDigit(c))
                {
                    string numStr = c.ToString();
                    while (i + 1 < expresion.Length && (char.IsDigit(expresion[i + 1]) || expresion[i + 1] == '.'))
                    {
                        numStr += expresion[i + 1];
                        i++;
                    }

                    double num = double.Parse(numStr);
                    valores.Push(num);
                }
                else if (EsOperador(c))
                {
                    while (operadores.Count > 0 && Precedencia(c, operadores.Peek()))
                    {
                        RealizarOperacion(valores, operadores);
                    }

                    operadores.Push(c);
                }
                else if (c == '(')
                {
                    operadores.Push(c);
                }
                else if (c == ')')
                {
                    while (operadores.Count > 0 && operadores.Peek() != '(')
                    {
                        RealizarOperacion(valores, operadores);
                    }

                    operadores.Pop(); // Quita el paréntesis de apertura de la pila
                }
            }

            while (operadores.Count > 0)
            {
                RealizarOperacion(valores, operadores);
            }

            return valores.Pop();
        }

        private static void RealizarOperacion(Stack<double> valores, Stack<char> operadores)
        {
            double valor2 = valores.Pop();
            double valor1 = valores.Pop();
            char op = operadores.Pop();
            double resultado = Operacion(valor1, valor2, op);
            valores.Push(resultado);
        }

        private static bool EsOperador(char c)
        {
            return c == '+' || c == '-' || c == '*' || c == '/' || c == '^';
        }

        private static bool Precedencia(char op1, char op2)
        {
            if (op2 == '(' || op2 == ')')
                return false;
            return (op1 == '*' || op1 == '/' || op1 == '^') && (op2 == '+' || op2 == '-');
        }

        private static double Operacion(double a, double b, char op)
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
                case '^':
                    return Potencia(a, b);
                default:
                    throw new ArgumentException("Operador invalido: " + op);
            }
        }

        private static double Potencia(double baseValue, double exponente)
        {
            return Math.Pow(baseValue, exponente);
        }
    }
}
