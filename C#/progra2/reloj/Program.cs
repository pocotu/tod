using System;
using System.Diagnostics;

public class Ejemplo
{
    // Factorial recursivo
    public static int fac_recursivo(int n)
    {
        if (n == 1 || n == 2)
        {
            return 1;
        }
        else
        {
            return fac_recursivo(n - 1) + fac_recursivo(n - 2);
        }
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

    public static void Main()
    {
        // Inicializamos el reloj
        Stopwatch stopwatch = new Stopwatch();
        /////////////////////////////////////////////////
        
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
        
        /////////////////////////////////////////////////
        
        // Código a medir para el factorial recursivo
        stopwatch.Start();
        int resultado1 = fac_recursivo(50);
        stopwatch.Stop();
        Console.WriteLine("El resultado del factorial recursivo es: {0}", resultado1);
        Console.WriteLine("El tiempo de ejecución para el factorial recursivo es: {0} ms", stopwatch.ElapsedMilliseconds);
        Console.WriteLine();

        // Reinicializamos el reloj
        stopwatch.Reset();

        // Código a medir para el factorial iterativo
        stopwatch.Start();
        int resultado2 = fac_iterativo(50);
        stopwatch.Stop();
        Console.WriteLine("El resultado del factorial iterativo es: {0}", resultado2);
        Console.WriteLine("El tiempo de ejecución para el factorial iterativo es: {0} ms", stopwatch.ElapsedMilliseconds);
        /////////////////////////////////////////////////
        
    }
}
