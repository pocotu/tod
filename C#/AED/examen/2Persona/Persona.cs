using System;

namespace Ejercicio_2
{
    public class Persona
    {
        // Atributos
        private string nombre;
        private DateTime fechaNacimiento;
        private string dni;
        private char sexo;
        private double peso;
        private double altura;

        // Constructor por defecto
        public Persona()
        {
            this.nombre = "";
            this.fechaNacimiento = DateTime.MinValue;
            this.dni = "";
            this.sexo = 'H';
            this.peso = 0.0;
            this.altura = 0.0;
        }

        // Constructor con nombre, edad y sexo, el resto por defecto
        public Persona(string nombre, DateTime fechaNacimiento, char sexo)
        {
            this.nombre = nombre;
            this.fechaNacimiento = fechaNacimiento;
            this.dni = "";
            this.sexo = sexo;
            this.peso = 0.0;
            this.altura = 0.0;
        }

        // Constructor con todos los atributos como parametro
        public Persona(string nombre, DateTime fechaNacimiento, string dni, char sexo, double peso, double altura)
        {
            this.nombre = nombre;
            this.fechaNacimiento = fechaNacimiento;
            this.dni = dni;
            this.sexo = sexo;
            this.peso = peso;
            this.altura = altura;
        }

        // Propiedades
        public string Nombre
        {
            get { return nombre; }
            set { nombre = value; }
        }

        public DateTime FechaNacimiento
        {
            get { return fechaNacimiento; }
            set { fechaNacimiento = value; }
        }

        public string DNI
        {
            get { return dni; }
        }

        public char Sexo
        {
            get { return sexo; }
            set { sexo = value; }
        }

        public double Peso
        {
            get { return peso; }
            set { peso = value; }
        }

        public double Altura
        {
            get { return altura; }
            set { altura = value; }
        }

        // Metodos
        public int CalcularIMC()
        {
            double imc = peso / (altura * altura);

            if (imc < 20)
            {
                return -1;
            }
            else if (imc >= 20 && imc <= 25)
            {
                return 0;
            }
            else
            {
                return 1;
            }
        }

        public bool EsMayorDeEdad()
        {
            // Calcular la edad de la persona

            // Devuelve la fecha actual
            DateTime fechaActual = DateTime.Today;
            // Calcula la edad
            int edad = fechaActual.Year - fechaNacimiento.Year;

            // si la fecha de nacimiento es posterior al día de hoy, le resto un año
            if (fechaNacimiento > fechaActual.AddYears(-edad))
            {
                // Resto un año a la edad
                edad--;
            }

            return edad >= 18;
        }

        // Genera un número aleatorio de 8 cifras y lo convierte en string
        public void GenerarDNI()
        {
            Random random = new Random();
            this.dni = random.Next(10000000, 99999999).ToString();
        }
    }
}