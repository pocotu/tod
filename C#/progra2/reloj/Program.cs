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

        int[] ln = { 10, 20, 30, 40, 50,
                    100, 200, 300, 400, 500,
                    1000, 2000, 3000, 5000,
                    10000, 20000, 50000, 100000 };

        foreach (int n in ln)
        {
            stopwatch.Start();
            Console.WriteLine(fac_iterativo(100));
            stopwatch.Stop();
            Console.WriteLine("El tiempo transcurrido es {0} ms",
                stopwatch.ElapsedMilliseconds);
            stopwatch.Reset();
        }

        // Código a medir
        // int resultado = fac_recursivo(10);
        // int resultado = fac_iterativo(3);

        // Mostramos el resultado y el tiempo de ejecución
        // Console.WriteLine("El resultado es: {0}", resultado);
        // Console.WriteLine("El tiempo de ejecución en milisegundos: {0} ms", stopwatch.ElapsedMilliseconds);
    }
}


/*
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
        for (int i=1; 1<n; i++)
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

        
        int [] ln = {10, 20, 30, 40, 50, 
                    100, 200,300, 400, 500, 
                    1000, 2000, 3000, 5000, 
                    10000, 20000, 50000, 100000};
        foreach (int n in ln){
            stopwatch.Start();
            Console.WriteLine(fac_iterativo(n));
            stopwatch.Stop();
            Console.WriteLine("El tiempo transcurrido es {0} ms",
                stopwatch.ElapsedMilliseconds);
            stopwatch.Reset();
        }
        
        //stopwatch.Start();
        // Código a medir
        //int resultado = fac_recursivo(10);
        //int resultado = fac_iterativo(3);
        //stopwatch.Stop();

        // Mostramos el resultado y el tiempo de ejecución
        //Console.WriteLine("El resultado es: {0}", resultado);
        //Console.WriteLine("El tiempo de ejecución en milisegundos: {0} ms", stopwatch.ElapsedMilliseconds);
    }
}
*/
