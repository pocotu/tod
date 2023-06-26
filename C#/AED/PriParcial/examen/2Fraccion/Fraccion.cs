using System;

namespace Francciones
{
    public class Fraccion
    {
        // Atributos
        private int numerador;
        private int denominador;

        // Metodos
        public Fraccion()
        {
            numerador = 1;
            denominador = 1;
        }

        // Sobrecarga de constructores
        public Fraccion(int numerador, int denominador)
        {
            this.numerador = numerador;
            this.denominador = denominador;
        }

        // Sobrecarga de operadores
        public int Numerador
        {
            get { return numerador; }
            set { numerador = value; }
        }

        public int Denominador
        {
            get { return denominador; }
            set { denominador = value; }
        }

        public Fraccion Sumar(Fraccion otraFraccion)
        {
            int nuevoDenominador = denominador * otraFraccion.Denominador;
            int nuevoNumerador = (numerador * otraFraccion.Denominador) + (otraFraccion.Numerador * denominador);
            return SimplificarFraccion(new Fraccion(nuevoNumerador, nuevoDenominador));
        }

        public Fraccion Restar(Fraccion otraFraccion)
        {
            int nuevoDenominador = denominador * otraFraccion.Denominador;
            int nuevoNumerador = (numerador * otraFraccion.Denominador) - (otraFraccion.Numerador * denominador);
            return SimplificarFraccion(new Fraccion(nuevoNumerador, nuevoDenominador));
        }

        public Fraccion Multiplicar(Fraccion otraFraccion)
        {
            int nuevoNumerador = numerador * otraFraccion.Numerador;
            int nuevoDenominador = denominador * otraFraccion.Denominador;
            return SimplificarFraccion(new Fraccion(nuevoNumerador, nuevoDenominador));
        }

        public Fraccion Dividir(Fraccion otraFraccion)
        {
            int nuevoNumerador = numerador * otraFraccion.Denominador;
            int nuevoDenominador = denominador * otraFraccion.Numerador;
            return SimplificarFraccion(new Fraccion(nuevoNumerador, nuevoDenominador));
        }

        public static Fraccion operator +(Fraccion fraccion1, Fraccion fraccion2)
        {
            return fraccion1.Sumar(fraccion2);
        }

        public static Fraccion operator -(Fraccion fraccion1, Fraccion fraccion2)
        {
            return fraccion1.Restar(fraccion2);
        }

        public static Fraccion operator *(Fraccion fraccion1, Fraccion fraccion2)
        {
            return fraccion1.Multiplicar(fraccion2);
        }

        public static Fraccion operator /(Fraccion fraccion1, Fraccion fraccion2)
        {
            return fraccion1.Dividir(fraccion2);
        }

        public bool EsMayorQue(Fraccion otraFraccion)
        {
            return (double)numerador / denominador > (double)otraFraccion.Numerador / otraFraccion.Denominador;
        }

        public bool EsMenorQue(Fraccion otraFraccion)
        {
            return (double)numerador / denominador < (double)otraFraccion.Numerador / otraFraccion.Denominador;
        }

        public bool EsIgualA(Fraccion otraFraccion)
        {
            return (double)numerador / denominador == (double)otraFraccion.Numerador / otraFraccion.Denominador;
        }

        public override string ToString()
        {
            return $"{numerador}/{denominador}";
        }

        // Metodos privados
        private Fraccion SimplificarFraccion(Fraccion fraccion)
        {
            int gcd = CalcularGCD(fraccion.Numerador, fraccion.Denominador);
            fraccion.Numerador /= gcd;
            fraccion.Denominador /= gcd;
            return fraccion;
        }

        private int CalcularGCD(int a, int b)
        {
            if (b == 0)
                return a;
            return CalcularGCD(b, a % b);
        }
    }
}
