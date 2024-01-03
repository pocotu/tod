#include <iostream>
#include <sstream>

using namespace std;

int main() {
    string line;
    int correctAnswers = 0;

    cout << "Ingrese las preguntas y respuestas. Escriba 'fin' para detener la entrada:\n";

    while (getline(cin, line)) {
        // Verifique si se debe detener la entrada
        if (line == "fin") {
            break;
        }

        // Parse la línea para obtener los valores a, b y c
        int a, b, c;
        char operation;
        stringstream ss(line);
        ss >> a >> operation >> b >> c;

        // Realice la operación y verifique si la respuesta es correcta
        int calculatedResult;
        if (operation == '+') {
            calculatedResult = a + b;
        } else {
            calculatedResult = a - b;
        }

        // Compruebe si la respuesta calculada coincide con c o si c es '?'
        if (calculatedResult == c || c == '?') {
            correctAnswers++;
        }
    }

    // Imprima el número de respuestas correctas
    cout << "Número de respuestas correctas: " << correctAnswers << endl;

    return 0;
}
