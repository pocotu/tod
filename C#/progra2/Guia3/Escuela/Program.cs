using System;

public class Estudiante
{
    public string Nombre { get; set; }
    public int Identificacion { get; set; }
    public string GradoAcademico { get; set; }
    public DateTime FechaNacimiento { get; set; }

    public void MostrarInformacion()
    {
        Console.WriteLine("Nombre: " + Nombre);
        Console.WriteLine("Identificacion: " + Identificacion);
        Console.WriteLine("Grado academico: " + GradoAcademico);
        Console.WriteLine("Edad: " + CalcularEdad());
    }

    public int CalcularEdad()
    {
        DateTime fechaActual = DateTime.Now;
        // Se calcula la edad restando el año actual menos el año de nacimiento
        int edad = fechaActual.Year - FechaNacimiento.Year;
        if (fechaActual.Month < FechaNacimiento.Month || (fechaActual.Month == FechaNacimiento.Month && fechaActual.Day < FechaNacimiento.Day))
        {   
            // Se resta 1 a la edad
            edad--;
        }
        return edad;
    }
}

public class Escuela
{
    private Estudiante[] estudiantes;
    private int indice;

    public Escuela(int capacidad)
    {
        estudiantes = new Estudiante[capacidad];
        indice = 0;
    }

    public void AgregarEstudiante(Estudiante estudiante)
    {
        if (indice < estudiantes.Length)
        {
            estudiantes[indice] = estudiante;
            indice++;
            Console.WriteLine("Estudiante registrado exitosamente.");
        }
        else
        {
            Console.WriteLine("No se puede agregar mas estudiantes. Capacidad maxima alcanzada.");
        }
    }

    public void MostrarInformacionEstudiante(int identificacion)
    {
        Estudiante estudiante = BuscarEstudiante(identificacion);
        if (estudiante != null)
        {
            estudiante.MostrarInformacion();
        }
        else
        {
            Console.WriteLine("No se encontro un estudiante con la identificacion especificada.");
        }
    }

    private Estudiante BuscarEstudiante(int identificacion)
    {
        foreach (Estudiante estudiante in estudiantes)
        {
            if (estudiante != null && estudiante.Identificacion == identificacion)
            {
                return estudiante;
            }
        }
        return null;
    }
}

//// Programa principal ////
public class Program
{
    public static void Main(string[] args)
    {
        Escuela escuela = new Escuela(3);

        Estudiante estudiante1 = new Estudiante
        {
            Nombre = "Juan Perez",
            Identificacion = 123,
            GradoAcademico = "1 grado",
            FechaNacimiento = new DateTime(2008, 5, 15)
        };

        Estudiante estudiante2 = new Estudiante
        {
            Nombre = "Maria Lopez",
            Identificacion = 456,
            GradoAcademico = "2 Grado",
            FechaNacimiento = new DateTime(2009, 9, 10)
        };

        escuela.AgregarEstudiante(estudiante1);
        escuela.AgregarEstudiante(estudiante2);

        escuela.MostrarInformacionEstudiante(123);
    }
}
