namespace B_Secuencial
{
    class Comparacion
    {
        public static int BusquedaSecuencial(int[] lista, int valorBuscado)
        {
            for (int i = 0; i < lista.Length; i++) {
                if (lista[i] == valorBuscado) {
                    return i; // Si encontro el valor, se retorna la posicion
                }
            }
            return -1; // El valor no se encontro en la lista
        }

        public static void ImprimirResultado(int valorBuscado, int posicion)
        {
            if (posicion != -1) {
                Console.WriteLine("El valor {0} se encontro en la posicion {1}", valorBuscado, posicion);
            }
            else {
                Console.WriteLine("El valor {0} no se encontro en la lista", valorBuscado);
            }
        }
    }
}

