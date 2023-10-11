#include <bits/stdc++.h>
#define ll long long

#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <chrono> // Para medir el tiempo

using namespace std;
using namespace std::chrono;

// Definición de la estructura de los nodos del árbol Huffman
struct NodoHuffman {
    char dato; // Carácter o símbolo
    int frecuencia; // Frecuencia
    NodoHuffman* izquierdo;
    NodoHuffman* derecho;

    // Constructor
    NodoHuffman(char d, int f) : dato(d), frecuencia(f), izquierdo(nullptr), derecho(nullptr) {}
};

// Función de comparación para la cola de prioridad
struct CompararNodos {
    bool operator()(NodoHuffman* a, NodoHuffman* b) {
        return a->frecuencia > b->frecuencia;
    }
};

// Función para construir el árbol Huffman
NodoHuffman* construirArbolHuffman(vector<pair<char, int>>& S, int& comparaciones) {
    // Paso 1: Construir una cola de prioridad
    priority_queue<NodoHuffman*, vector<NodoHuffman*>, CompararNodos> colaPrioridad;
    // Complejidad del paso 1: O(1)

    // Inicialmente, agregamos todos los caracteres a la cola de prioridad como nodos individuales
    for (auto& par : S) {
        colaPrioridad.push(new NodoHuffman(par.first, par.second));
    }
    // Complejidad del bucle for: O(n*log(n)), donde "n" es el número de caracteres únicos en S

    // Paso 2: Construir el árbol Huffman
    while (colaPrioridad.size() > 1) {
        // Paso 3: Extraer los dos nodos con las frecuencias mínimas
        NodoHuffman* x1 = colaPrioridad.top();
        colaPrioridad.pop();
        NodoHuffman* x2 = colaPrioridad.top();
        colaPrioridad.pop();
        // Complejidad del bucle while: O(n*log(n))

        // Paso 5: Crear un nuevo nodo con la suma de las frecuencias de x1 y x2
        NodoHuffman* nuevoNodo = new NodoHuffman('\0', x1->frecuencia + x2->frecuencia);
        nuevoNodo->izquierdo = x1;
        nuevoNodo->derecho = x2;

        // Paso 7: Insertar el nuevo nodo en la cola de prioridad
        colaPrioridad.push(nuevoNodo);
        comparaciones++; // Aumentar el contador de comparaciones
    }

    // Paso 8: Devolver el árbol construido
    return colaPrioridad.top();
    // Complejidad del paso 8: O(1)
}

// Función para asignar códigos binarios a los caracteres
void asignarCodigosHuffman(NodoHuffman* raiz, string codigo, unordered_map<char, string>& codigosHuffman) {
    if (raiz) {
        if (!raiz->izquierdo && !raiz->derecho) {
            codigosHuffman[raiz->dato] = codigo;
        }
        asignarCodigosHuffman(raiz->izquierdo, codigo + "0", codigosHuffman);
        asignarCodigosHuffman(raiz->derecho, codigo + "1", codigosHuffman);
    }
    // Complejidad de la función asignarCodigosHuffman: O(n)
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    // Solicitar al usuario una cadena de texto
    cout << "Ingrese una cadena de texto: ";
    string entrada;
    cin >> entrada;
    // Complejidad de la lectura de entrada: O(m), donde "m" es la longitud de la cadena de entrada

    // Calcular las frecuencias de los caracteres en la entrada
    unordered_map<char, int> mapaFrecuencias;
    for (char c : entrada) {
        mapaFrecuencias[c]++;
    }
    // Complejidad del bucle for: O(m)

    // Crear un vector de pares (carácter, frecuencia) a partir del mapa
    vector<pair<char, int>> datos;
    for (const auto& par : mapaFrecuencias) {
        datos.push_back(par);
    }
    // Complejidad del bucle for: O(n), donde "n" es el número de caracteres únicos en la entrada

    // Contador de comparaciones
    int comparaciones = 0;

    // Iniciar el reloj
    auto inicio = high_resolution_clock::now();

    // Construir el árbol de Huffman
    NodoHuffman* raiz = construirArbolHuffman(datos, comparaciones);
    // Complejidad de construirArbolHuffman: O(n*log(n))

    // Asignar códigos binarios a los caracteres
    unordered_map<char, string> codigosHuffman;
    asignarCodigosHuffman(raiz, "", codigosHuffman);
    // Complejidad de asignarCodigosHuffman: O(n)

    // Detener el reloj
    auto fin = high_resolution_clock::now();
    auto tiempo = duration_cast<milliseconds>(fin - inicio);

    // Mostrar los códigos Huffman resultantes
    cout << "Codigos Huffman:" << endl;
    for (const auto& par : codigosHuffman) {
        cout << par.first << ": " << par.second << endl;
    }

    cout << "Numero de comparaciones realizadas: " << comparaciones << endl;
    cout << "Tiempo de ejecucion: " << tiempo.count() << " ms" << endl;

    return 0;
}
