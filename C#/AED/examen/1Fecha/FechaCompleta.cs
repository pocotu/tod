using System;

namespace Fechas
{
    // clase hija de Fecha
    public class FechaCompleta : Fecha
    {
        private int hora;
        private int minuto;
        private int segundo;

        public FechaCompleta()
        {
            dia = DateTime.Now.Day;
            mes = DateTime.Now.Month;
            año = DateTime.Now.Year;
            hora = DateTime.Now.Hour;
            minuto = DateTime.Now.Minute;
            segundo = DateTime.Now.Second;
        }

        public FechaCompleta(int dia, int mes, int año, int hora, int minuto, int segundo) : base(dia, mes, año)
        {
            this.hora = hora;
            this.minuto = minuto;
            this.segundo = segundo;
        }

        public int Hora
        {
            get { return hora; }
            set { hora = value; }
        }

        public int Minuto
        {
            get { return minuto; }
            set { minuto = value; }
        }

        public int Segundo
        {
            get { return segundo; }
            set { segundo = value; }
        }

        public override string EnTexto()
        {
            string textoFecha = $"{dia}/{mes}/{año} {hora}:{minuto}:{segundo}";
            return textoFecha;
        }
    }
}