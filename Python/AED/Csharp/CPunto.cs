using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace appPOOEjercicio1

{
    class CPunto
    {
    // Atributos  
    private int aX;
    private int aY;

    // Constructores
    // Constructor por defecto
    public CPunto()
    {
        aX = 0;
        aY = 0;
    }

    // Constructor con parametros
    public CPunto(int pX, int pY)
    {
        aX = pX;
        aY = pY;
    }

    // Propiedades (Getters y Setters)
    // x y y son las propiedades de los atributos aX y aY
    public int X
    {
        get { return aX; }
        set { aX = value; }
    }

    public int y
    {
        get { return aY; }
        set { aY = value; }
    }

    // Metodos

    // Metodo de calculo de la distancia entre dos puntos
    public double CalcularDistancia(CPunto pPunto)
    {
        return Math.Sqrt(Math.Pow(pPunto.X - aX, 2) + Math.Pow(pPunto.y - aY, 2));

    }
    }
}