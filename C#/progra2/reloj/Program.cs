using System;
using System.Diagnostics;

// se crea la clase Ejemplo
public class Ejemplo
{
    // Factorial recursivo
    public static int fac_recursivo(int n)
    {
	// Si n es 1 o 2, entonces retorna 1
        if (n == 1 || n == 2)
        {
            return 1;
        }
	// Si n es mayor que 2, entonces retorna
	// la suma de los dos anteriores
        else
        {
            return fac_recursivo(n - 1) + fac_recursivo(n - 2);
        }
	// ejemplos: 
	// fac_recursivo(5) = fac_recursivo(4) + fac_recursivo(3)
	// fac_recursivo(4) = fac_recursivo(3) + fac_recursivo(2)
	// fac_recursivo(3) = fac_recursivo(2) + fac_recursivo(1)
	// fac_recursivo(2) = fac_recursivo(1) = 1
    }

    // Factorial iterativo
    public static int fac_iterativo(int n)
    {
        int f_ant = 0;
        int f_sig = 1;
        for (int i = 1; i < n; i++)
        {
            int aux = f_ant;
            f_ant = f_sig;
            f_sig = f_sig + aux;
        }
        return f_sig;
    }

    // Suma de numeros
    public static int suma_numeros(int n)
    {
        int suma = 0;
        for (int i = 1; i <= n; i++)
        {
            suma = suma + i;
        }
        return suma;
    }
    public static void Main()
    {
        // Inicializamos el reloj
        Stopwatch stopwatch = new Stopwatch();

        int [] ln = {10, 20, 30, 40, 50, 
                    100, 200,300, 400, 500, 
                    1000, 2000, 3000, 5000, 
                    10000, 20000, 50000, 100000};

        Console.WriteLine("#### Factorial iterativo ####");
        foreach (int i in ln){
            stopwatch.Start();
            Console.WriteLine(fac_iterativo(i));
            stopwatch.Stop();
            Console.WriteLine("El tiempo transcurrido es {0} ms", 
                stopwatch.ElapsedMilliseconds/1000.0);
        }

        Console.WriteLine("#### Factorial recursivo ####");
        foreach (int j in ln){
            stopwatch.Start();
            Console.WriteLine(fac_recursivo(j));
            stopwatch.Stop();
            Console.WriteLine("El tiempo transcurrido es {0} ms", 
                stopwatch.ElapsedMilliseconds/1000.0);
        }
    }
}


