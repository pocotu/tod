// Implementar la clase Fecha, que contenga los atributos: día, mes y año. Luego implementar 
// la clase FechaCompleta que corresponde a la clase hija de la clase Fecha, que incluirá además los atributos hora, minuto segundo.
// 1.1. Implementar los 2 respectivos constructores para la clase FechaCompleta, el cual puede tener parámetros ingresados por 
//      el usuario o cuando no se ingresan parámetros, deberá capturar la fecha y hora actual del sistema). Implementar 
//      sus correspondientes Getters y Setters para los atributos.
// 1.2. Implementar el método: FechaCorrecta(): Devuelva un valor booleano indicado si la fecha es válida o no. 
// 1.3. Implementar el método: EnTexto(): Muestra una fecha en texto. (Ejemplo: 10/05/2023 = DIEZ DE MAYO DEL DOS MIL VENTITRES).
// 1.4. Implementar el método: DiasTranscurridos(): Muestra cantidad de días transcurridos entre la fecha del objeto y otra pasada como parámetro.
// 1.5. Implementar el método: DiaSiguiente(): Devuelve la fecha correspondiente al día siguiente.

using System;

namespace Fechas
{
    public class Program
    {
        public static void Main(string[] args)
        {
            // Ejemplo de uso de las clases Fecha y FechaCompleta
            Fecha fecha1 = new Fecha(10, 5, 2023);
            FechaCompleta fechaCompleta1 = new FechaCompleta(10, 5, 2023, 12, 30, 0);

            Console.WriteLine("Fecha: " + fecha1.EnTexto());
            Console.WriteLine("Fecha completa: " + fechaCompleta1.EnTexto());

            Console.WriteLine("Fecha válida: " + fecha1.FechaCorrecta());
            Console.WriteLine("Fecha completa válida: " + fechaCompleta1.FechaCorrecta());

            Fecha fecha2 = new Fecha(20, 5, 2023);
            Console.WriteLine("Días transcurridos: " + fecha1.DiasTranscurridos(fecha2));

            Fecha fechaSiguiente = fecha1.DiaSiguiente();
            Console.WriteLine("Día siguiente: " + fechaSiguiente.EnTexto());
        }
    }
}