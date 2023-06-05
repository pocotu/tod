namespace AppPersonas
{
    class CPersona
    {   
        // Atributos
        protected string nombre;
        protected string direccion;

        // Constructor
        public CPersona(string nombre, string direccion)
        {
            this.nombre = nombre;
            this.direccion = direccion;
        }
        
        // Propiedades
        public string Nombre
        {
            get { return nombre; }
            set { nombre = value; }
        }

        public string Direccion
        {
            get { return direccion; }
            set { direccion = value; }
        }

        // Metodos
        public override string ToString()
        {
            return $"Nombre: {nombre}\nDireccion: {direccion}";
        }

        public override bool Equals(object obj)
        {
            if (obj == null || obj.GetType() != GetType())
                return false;
            CPersona otraPersona = (CPersona)obj;
            return nombre == otraPersona.nombre && direccion == otraPersona.direccion;
        }

        public virtual void Mostrar()
        {
            Console.WriteLine(ToString());
        }
    }
}