/*
Implementar la clase CComplejo que permita representar a los Números Complejos (Que están
formados por una parte real y una parte imaginaria). Implementar sus respectivos constructores, sus
respectivos Getters y Setters. E implementar los Métodos para Sumar, Resta, Multiplicar y Dividir
números complejos. (Implementarlos como Método de Instancia, Métodos de Clase y Sobrecarga de
Operadores).
*/

using System;

namespace CComplejo
{
    class NComplejo
    {   
        // Atributos
        private double real;
        private double imaginario;

        // Constructores
        public NComplejo(double real, double imaginario)
        {
            this.real = real;
            this.imaginario = imaginario;
        }

        // Propiedades
        public double Real
        {
            get { return real; }
            set { real = value; }
        }

        public double Imaginario
        {
            get { return imaginario; }
            set { imaginario = value; }
        }

        // Metodo de instancia
        
        public NComplejo Sumar(NComplejo c)
        {
            return new NComplejo(real + c.real, imaginario + c.imaginario);
        }

        public NComplejo Restar(NComplejo c)
        {
            return new NComplejo(real - c.real, imaginario - c.imaginario);
        }

        public NComplejo Multiplicar(NComplejo c)
        {
            return new NComplejo(real * c.real - imaginario * c.imaginario, real * c.imaginario + imaginario * c.real);
        }

        public NComplejo Dividir(NComplejo c)
        {
            return new NComplejo((real * c.real + imaginario * c.imaginario) / (c.real * c.real + c.imaginario * c.imaginario), (imaginario * c.real - real * c.imaginario) / (c.real * c.real + c.imaginario * c.imaginario));
        }

        
        // Metodo de clase
        public static NComplejo Sumar(NComplejo c1, NComplejo c2)
        {
            return new NComplejo(c1.real + c2.real, c1.imaginario + c2.imaginario);
        }

        public static NComplejo Restar(NComplejo c1, NComplejo c2)
        {
            return new NComplejo(c1.real - c2.real, c1.imaginario - c2.imaginario);
        }

        public static NComplejo Multiplicar(NComplejo c1, NComplejo c2)
        {
            return new NComplejo(c1.real * c2.real - c1.imaginario * c2.imaginario, c1.real * c2.imaginario + c1.imaginario * c2.real);
        }

        public static NComplejo Dividir(NComplejo c1, NComplejo c2)
        {
            return new NComplejo((c1.real * c2.real + c1.imaginario * c2.imaginario) / (c2.real * c2.real + c2.imaginario * c2.imaginario), (c1.imaginario * c2.real - c1.real * c2.imaginario) / (c2.real * c2.real + c2.imaginario * c2.imaginario));
        }

        // Sobrecarga de operadores
        public static NComplejo operator +(NComplejo c1, NComplejo c2)
        {
            return new NComplejo(c1.real + c2.real, c1.imaginario + c2.imaginario);
        }

        public static NComplejo operator -(NComplejo c1, NComplejo c2)
        {
            return new NComplejo(c1.real - c2.real, c1.imaginario - c2.imaginario);
        }

        public static NComplejo operator *(NComplejo c1, NComplejo c2)
        {
            return new NComplejo(c1.real * c2.real - c1.imaginario * c2.imaginario, c1.real * c2.imaginario + c1.imaginario * c2.real);
        }

        public static NComplejo operator /(NComplejo c1, NComplejo c2)
        {
            return new NComplejo((c1.real * c2.real + c1.imaginario * c2.imaginario) / (c2.real * c2.real + c2.imaginario * c2.imaginario), (c1.imaginario * c2.real - c1.real * c2.imaginario) / (c2.real * c2.real + c2.imaginario * c2.imaginario));
        }

        // Metodo ToString
        public override string ToString()
        {
            return real + " + " + imaginario + "i";
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            NComplejo c1 = new NComplejo(2, 3);
            NComplejo c2 = new NComplejo(4, 5);
            NComplejo c3 = new NComplejo(0, 0);
            NComplejo c4 = new NComplejo(0, 0);

            // Metodo de instancia
            c3 = c1.Sumar(c2);
            Console.WriteLine("Suma de c1 y c2: " + c3.ToString());
            c3 = c1.Restar(c2);
            Console.WriteLine("Resta de c1 y c2: " + c3.ToString());
            c3 = c1.Multiplicar(c2);
            Console.WriteLine("Multiplicacion de c1 y c2: " + c3.ToString());
            c3 = c1.Dividir(c2);
            Console.WriteLine("Division de c1 y c2: " + c3.ToString());

            // Metodo de clase
            c3 = NComplejo.Sumar(c1, c2);
            Console.WriteLine("Suma de c1 y c2: " + c3.ToString());
            c3 = NComplejo.Restar(c1, c2);
            Console.WriteLine("Resta de c1 y c2: " + c3.ToString());
            c3 = NComplejo.Multiplicar(c1, c2);
            Console.WriteLine("Multiplicacion de c1 y c2: " + c3.ToString());
            c3 = NComplejo.Dividir(c1, c2);
            Console.WriteLine("Division de c1 y c2: " + c3.ToString());

            // Sobrecarga de operadores
            c3 = c1 + c2;
            Console.WriteLine("Suma de c1 y c2: " + c3.ToString());
            c3 = c1 - c2;
            Console.WriteLine("Resta de c1 y c2: " + c3.ToString());
            c3 = c1 * c2;
            Console.WriteLine("Multiplicacion de c1 y c2: " + c3.ToString());
            c3 = c1 / c2;
            Console.WriteLine("Division de c1 y c2: " + c3.ToString());

            // Metodo ToString
            Console.WriteLine("c1: " + c1.ToString());
            Console.WriteLine("c2: " + c2.ToString());
            Console.WriteLine("c3: " + c3.ToString());
            Console.WriteLine("c4: " + c4.ToString());

            // Metodo Equals

            if (c1.Equals(c2))
            {
                Console.WriteLine("c1 y c2 son iguales");
            }
            else
            {
                Console.WriteLine("c1 y c2 no son iguales");
            }
        }
    }
}   