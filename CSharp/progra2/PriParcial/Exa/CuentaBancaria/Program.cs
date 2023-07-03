using System;

class CuentaBancaria
{
    // Atributos
    private string numeroCuenta;
    private string titular;
    private decimal saldo;
    
    // Constructor 
    public CuentaBancaria(string numeroCuenta, string titular)
    {
        this.numeroCuenta = numeroCuenta;
        this.titular = titular;
        this.saldo = 0;
    }

    // Metodo para depositar
    public void Depositar(decimal monto)
    {
        saldo += monto;
    }

    // Metodo para retirar
    public void Retirar(decimal monto)
    {
        saldo -= monto;
    }
    // Metodo para mostrar saldo
    public decimal MostrarSaldo()
    {
        return saldo;
    }
}

// Clase principal
class Program
{
    static void Main(string[] args)
    {
        CuentaBancaria cuenta = new CuentaBancaria("123456789", "Juan Perez");
        Console.WriteLine("Saldo inicial: " + cuenta.MostrarSaldo());
        cuenta.Depositar(1000);
        Console.WriteLine("Despues de depositar: " + cuenta.MostrarSaldo());
        cuenta.Retirar(500);
        Console.WriteLine("Despues de retirar: " + cuenta.MostrarSaldo());
    }
}
