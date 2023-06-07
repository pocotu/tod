using System ;
namespace Ejercicio_propuesto_1
{
class Program
{
static void Main ( string [] args )
{
int NUM1 , NUM2 ;
double RESUL ;
string linea ;
Console . Write ( " NUMERO 1 : " ) ;
linea = Console.ReadLine() ;
NUM1 = int . Parse (linea) ;
Console . Write ( " NUMERO 2 : " ) ;
linea = Console.ReadLine() ;
NUM2 = int . Parse ( linea ) ;
RESUL = ( NUM1 + NUM2 ) * ( NUM1 - NUM2 ) ;
Console . WriteLine () ;
Console . WriteLine ( " El resultado es : " + RESUL);
Console . ReadLine () ;
}
}
}