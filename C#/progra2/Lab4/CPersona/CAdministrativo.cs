using System;

namespace AppPersonas
{
    class CAdministrativo : CPersona
    {
        // Atributos
        private string codigo;
        private string departamento;
        private string categoria;

        // Constructor
        public CAdministrativo(string nombre, string direccion, string codigo, 
            string departamento, string categoria) : base(nombre, direccion)
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

        public override void Mostrar()
        {
            Console.WriteLine(ToString());
        }
    }
}