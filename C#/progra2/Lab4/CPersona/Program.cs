using System;

namespace AppPersonas
{
    class Program
    {
        static void Main(string[] args)
        {
            CAlumno alumno = new CAlumno("Juan", "Av. principal 123", "A001", "Ingeniería informatica");
            alumno.Mostrar();

            CDocente docente = new CDocente("Pedro", "Av. principal 123", "D001", "Matematicas", "Titular");
            docente.Mostrar();

            CAdministrativo administrativo = new CAdministrativo("Maria", "Av. principal 123", "A004", "Secretaria", "Administrativo");
            administrativo.Mostrar();
            
        }
    }
}