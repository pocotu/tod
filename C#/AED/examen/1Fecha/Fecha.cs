using System;

namespace Fechas
{
    public class Fecha
    {
        protected int dia;
        protected int mes;
        protected int año;

        public Fecha()
        {
            dia = DateTime.Now.Day;
            mes = DateTime.Now.Month;
            año = DateTime.Now.Year;
        }

        public Fecha(int dia, int mes, int año)
        {
            this.dia = dia;
            this.mes = mes;
            this.año = año;
        }

        public int Dia
        {
            get { return dia; }
            set { dia = value; }
        }

        public int Mes
        {
            get { return mes; }
            set { mes = value; }
        }

        public int Año
        {
            get { return año; }
            set { año = value; }
        }

        public bool FechaCorrecta()
        {
            return ValidarFecha(dia, mes, año);
        }

        public virtual string EnTexto()
        {
            string textoFecha = $"{dia}/{mes}/{año}";
            return textoFecha;
        }

        public int DiasTranscurridos(Fecha otraFecha)
        {
            DateTime fecha1 = new DateTime(año, mes, dia);
            DateTime fecha2 = new DateTime(otraFecha.Año, otraFecha.Mes, otraFecha.Dia);

            TimeSpan diferencia = fecha2 - fecha1;
            int diasTranscurridos = diferencia.Days;

            return Math.Abs(diasTranscurridos);
        }

        public Fecha DiaSiguiente()
        {
            DateTime fecha = new DateTime(año, mes, dia);
            fecha = fecha.AddDays(1);

            Fecha siguienteFecha = new Fecha(fecha.Day, fecha.Month, fecha.Year);
            return siguienteFecha;
        }

        protected bool ValidarFecha(int dia, int mes, int año)
        {
            try
            {
                DateTime fecha = new DateTime(año, mes, dia);
                return true;
            }
            catch (Exception)
            {
                return false;
            }
        }
    }
}