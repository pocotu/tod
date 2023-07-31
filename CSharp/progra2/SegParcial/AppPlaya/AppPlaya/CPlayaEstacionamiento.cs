using System;

namespace AppPlaya
{
    public class PlayaEstacionamiento
    {
        // Atributos
        private CCola colaEstacionamiento;

        // Constructores
        public PlayaEstacionamiento()
        {
            colaEstacionamiento = new CCola();
        }

        // Metodos
        public void LlegarVehiculo(string nombreVehiculo)
        {
            Vehiculo vehiculo = new Vehiculo(nombreVehiculo);
            colaEstacionamiento.agregar(vehiculo);
            Console.WriteLine($"El vehiculo '{nombreVehiculo}' ha llegado al estacionamiento.");
        }

        public void SalirVehiculo()
        {
            if (!colaEstacionamiento.esVacia())
            {
                Vehiculo vehiculo = (Vehiculo)colaEstacionamiento.primero();
                colaEstacionamiento.avanzar();
                Console.WriteLine($"El vehiculo '{vehiculo.Nombre}' ha salido del estacionamiento.");
            }
            else
            {
                Console.WriteLine("El estacionamiento esta vacio. No hay vehiculos para salir.");
            }
        }
    }
}
