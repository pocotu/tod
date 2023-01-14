using System;
using System.Linq;
using System.Collections.Generic;

class Persona
{
    public string DNI { get; set; }
    public string Nombre { get; set; }
    public string Ciudad { get; set; }
}

class Program
{
    static List<Persona> personas = new List<Persona>()
    {
        new Persona() { DNI = "123", Nombre = "Juan", Ciudad = "Cusco" },
        new Persona() { DNI = "456", Nombre = "Maria", Ciudad = "Lima" },
        new Persona() { DNI = "789", Nombre = "Pedro", Ciudad = "Cusco" }
    };

    static Stack<Persona> accesitarios = new Stack<Persona>(new List<Persona>()
    {
        new Persona() { DNI = "12345678", Nombre = "Juan", Ciudad = "Cusco" },
        new Persona() { DNI = "45678901", Nombre = "Maria", Ciudad = "Lima" },
        new Persona() { DNI = "78901234", Nombre = "Pedro", Ciudad = "Cusco" }
    });

    static void ReemplazarPersonaPorAccesitario(string dni)
    {
        // Buscar la persona habilitada en la lista
        var persona = personas.FirstOrDefault(p => p.DNI == dni);
        if (persona != null)
        {
            // Reemplazar la persona habilitada con el accesitario de la cima de la pila
            int index = personas.IndexOf(persona);
            personas[index] = accesitarios.Pop();
        }
    }

    static List<Persona> ObtenerPersonasDeCiudad(string ciudad)
    {
        return personas.Where(p => p.Ciudad == ciudad).ToList();
    }

    static void Main(string[] args)
    {
        // para obtener las personas de Cusco
        var personasDeCusco = ObtenerPersonasDeC
