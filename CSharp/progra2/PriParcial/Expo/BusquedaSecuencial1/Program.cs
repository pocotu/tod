using System;

class Program
{
    static int BusquedaSecuencial(int[] lista, int valorBuscado)
    {
        int posicion = 0;

        foreach (int numero in lista)
        {
            if (numero == valorBuscado)
            {
                return posicion; // Se encontró el valor, se retorna la posición
            }

            posicion++;
        }

        return -1; // El valor no se encontró en la lista
    }

    static void Main()
    {
        int[] lista = { 4, 7, 2, 1, 5, 9, 8, 3, 6 };
        int valorBuscado = 9;

        int posicion = BusquedaSecuencial(lista, valorBuscado);

        if (posicion != -1)
        {
            Console.WriteLine("El valor {0} se encontro en la posicion {1}.", valorBuscado, posicion);
        }
        else
        {
            Console.WriteLine("El valor {0} no se encontro en la lista.", valorBuscado);
        }
    }
}
