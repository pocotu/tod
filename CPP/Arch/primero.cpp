// crea una clase que sume dos numeros

#include <iostream>
using namespace std;

class Suma {
    public:
        int sumar(int num1, int num2) {
            return num1 + num2;
        }
};

int main() {
    Suma s;
    cout << "La suma de 3 y 4 es: " << s.sumar(3, 4) << endl;
    return 0;
}