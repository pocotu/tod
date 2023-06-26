namespace AppPersonas
{
    class CDocente : CPersona
    {   
        // Atributos
        private string codigo;
        private string departamento;
        private string categoria;

        // Constructor
        public CDocente(string nombre, string direccion, string codigo, string departamento, string categoria) : base(nombre, direccion)
        {
            this.codigo = codigo;
            this.departamento = departamento;
            this.categoria = categoria;
        }

        // Propiedades
        public string Codigo
        {
            get { return codigo; }
            set { codigo = value; }
        }

        public string Departamento
        {
            get { return departamento; }
            set { departamento = value; }
        }

        public string Categoria
        {
            get { return categoria; }
            set { categoria = value; }
        }

        // Metodos
        public override string ToString()
        {
            return base.ToString() + $"\nCodigo: {codigo}\nDepartamento: {departamento}\nCategoria: {categoria}";
        }

        public override bool Equals(object obj)
        {
            if (obj == null || obj.GetType() != GetType())
                return false;
            CDocente otroDocente = (CDocente)obj;
            return base.Equals(obj) && codigo == otroDocente.codigo && departamento == otroDocente.departamento && categoria == otroDocente.categoria;
        }

        public override void Mostrar()
        {
            Console.WriteLine(ToString());
        }
    }
}