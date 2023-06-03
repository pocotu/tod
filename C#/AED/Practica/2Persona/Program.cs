/*
Implementar la clase llamada Persona que siga las siguientes condiciones:
Sus atributos son: nombre, fechaNacimiento, DNI, sexo (H hombre, M mujer), peso y altura. Si
quieres añadir algún atributo puedes hacerlo. Por defecto, todos los atributos menos el DNI serán
valores por defecto según su tipo (0 números, cadena vacía para String, etc.). Sexo será hombre por
defecto.
Se implantarán varios constructores:
Un constructor por defecto.
Un constructor con el nombre, edad y sexo, el resto por defecto.
Un constructor con todos los atributos como parámetro.
Los métodos que se implementaran son:
calcularIMC(): calculara si la persona está en su peso ideal (peso/(altura^2)), si esta fórmula devuelve
un valor menor que 20, la función devuelve un -1, si devuelve un número entre 20 y 25 (incluidos),
significa que está por debajo de su peso ideal la función devuelve un 0 y si devuelve un valor mayor
que 25 significa que tiene sobrepeso, la función devuelve un 1.
esMayorDeEdad(): indica si es mayor de edad, devuelve un booleano.
comprobarSexo(sexo): comprueba que el sexo introducido es correcto.
generaDNI(): genera un número aleatorio de 8 cifras y asigna ese valor al DNI.
*/

using System;


namespace Ejercicio_2
{
    public class Program
    {
        public static void Main(string[] args)
        {
            // Crear una persona utilizando el constructor por defecto
            Persona persona1 = new Persona();
            persona1.Nombre = "Juan";
            persona1.FechaNacimiento = new DateTime(1990, 5, 15);
            persona1.Sexo = 'H';
            persona1.Peso = 70.5;
            persona1.Altura = 1.75;

            // Crear una persona utilizando el constructor con nombre, edad y sexo
            Persona persona2 = new Persona("Maria", new DateTime(1985, 10, 20), 'M');

            // Crear una persona utilizando el constructor con todos los atributos
            Persona persona3 = new Persona("Luis", new DateTime(2000, 3, 8), "12345678", 'H', 65.2, 1.80);

            // Calcular el IMC de una persona
            int imc = persona1.CalcularIMC();
            Console.WriteLine("IMC: " + imc);

            // Comprobar si una persona es mayor de edad
            bool esMayorDeEdad = persona2.EsMayorDeEdad();
            Console.WriteLine("Es mayor de edad? " + esMayorDeEdad);

            // Generar el DNI de una persona
            persona1.GenerarDNI();
            Console.WriteLine("DNI: " + persona1.DNI);
        }
    }
}