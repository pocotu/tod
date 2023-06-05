namespace AppPersonas
{
    class CAlumno : CPersona
    {
        // Atributos
        private string codigo;
        private string carrera;

        // Constructor
        public CAlumno(string nombre, string direccion, string codigo, string carrera) : base(nombre, direccion)
        {
            this.codigo = codigo;
            this.carrera = carrera;
        }

        // Propiedades
        public string Codigo
        {
            get { return codigo; }
            set { codigo = value; }
        }

        public string Carrera
        {
            get { return carrera; }
            set { carrera = value; }
        }

        // Metodos
        public override string ToString()
        {
            return base.ToString() + $"\nCodigo: {codigo}\nCarrera: {carrera}";
        }

        public override bool Equals(object obj)
        {
            if (obj == null || obj.GetType() != GetType())
                return false;
            CAlumno otroAlumno = (CAlumno)obj;
            return base.Equals(obj) && codigo == otroAlumno.codigo && carrera == otroAlumno.carrera;
        }

        public override void Mostrar()
        {
            Console.WriteLine(ToString());
        }
    }
}