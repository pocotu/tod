using System;

namespace Ejercicio_1
{
    class Cuenta
    {
        private string titular;
        private double cantidad;

        // Constructor
        public Cuenta(string titular)
        {
            this.titular = titular;
        }

        // Constructor sobrecargado
        public Cuenta(string titular, double cantidad)
        {
            this.titular = titular;
            this.cantidad = cantidad;
        }

        // Métodos
        // Este método ingresa dinero en la cuenta,
        public void Ingresar(double cantidad)
        {
            if (cantidad > 0)
            {
                this.cantidad += cantidad;
            }
        }
        
        // Este método retira una cantidad de dinero de la cuenta
        public void Retirar(double cantidad)
        {
            // si la cantidad a retirar es mayor que el saldo de la cuenta, se pondrá el saldo a 0.
            if (this.cantidad - cantidad < 0)
            {
                this.cantidad = 0;
            }
            else
            {
                this.cantidad -= cantidad;
            }
        }

        // Este metodo muestra los datos de la cuenta
        public void Mostrar()
        {
            Console.WriteLine($"{titular} tiene {cantidad} pesos en la cuenta.");
        }
    }
}