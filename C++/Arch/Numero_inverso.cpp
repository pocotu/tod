/*
Escriba un programa que solicite al usuario un numero de
tres digitos y que lo imprima en orden inverso. 
Por ejemplo
	una entrada de 592 debe enviar como salida 295.
*/
#include<iostream>
using namespace std;

int main(){
	//declarion de variables
	int numero, uds, dec, cent;
	cout<<"Ingresar numero de 3 digitos : ";
	cin>>numero;
		uds = (numero % 100) % 10;
		dec = (numero % 100) / 10;
		cent = numero / 100;
	cout<<"\n =  "<<uds<<dec<<cent;
	return 0;
}



