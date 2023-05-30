/*
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular y cantidad.
El titular será obligatorio y la cantidad es opcional (En este caso la cantidad se inicializa con 0). Crea
dos constructores que cumpla lo anterior.
Tendrá dos métodos especiales:
Ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se
hará nada.
Retirar(cantidad): se retira una cantidad a la cuenta, si restando la cantidad actual a la que nos pasan
es negativa, la cantidad de la cuenta pasa a ser 0.
mostrar(): muestra todos los datos actuales de la cuenta.
*/

using System;

namespace Ejercicio_1
{
    class Program
    {
        static void Main(string[] args)
        {
            // Crear objetos
            Cuenta cuenta1 = new Cuenta("Juan"); // sin saldo inicial
            Cuenta cuenta2 = new Cuenta("Pedro", 300); // con saldo inicial

            cuenta1.Ingresar(300);
            cuenta2.Retirar(100);

            cuenta1.Mostrar();
            cuenta2.Mostrar();
        }
    }
}



