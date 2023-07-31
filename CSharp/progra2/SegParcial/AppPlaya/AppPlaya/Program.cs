using System;

namespace AppPlaya
{
    class Program
    {
        static void Main(string[] args)
        {
            PlayaEstacionamiento playa = new PlayaEstacionamiento();

            playa.LlegarVehiculo("Auto1");
            playa.LlegarVehiculo("Camioneta1");
            playa.LlegarVehiculo("Moto1");

            playa.SalirVehiculo();
            playa.SalirVehiculo();
            playa.SalirVehiculo();
            // Intentar salir cuando el estacionamiento esta vacio
            playa.SalirVehiculo(); 

            Console.ReadKey();
        }
    }
}
