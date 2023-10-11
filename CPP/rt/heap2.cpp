#include <bits/stdc++.h>
#define ll long long

#include <iostream>
#include <vector>
#include <chrono>

using namespace std;
using namespace std::chrono;

// Declaración de funciones
void heapify_down(vector<int>& A, vector<int>& key, int i, int& comparaciones);
void heapify_up(vector<int>& A, vector<int>& key, int i, int& comparaciones);

// Función para extraer el mínimo de un montículo
int extract_min(vector<int>& A, vector<int>& key, int& comparaciones) {
    int ret = A[0];
    int last = A.back();
    int last_key = key.back();
    A.pop_back();
    key.pop_back();
    if (!A.empty()) {
        A[0] = last;
        key[0] = last_key;
        heapify_down(A, key, 0, comparaciones);
    }
    return ret;
}

// Función para disminuir la clave de un elemento en el montículo
void decrease_key(vector<int>& A, vector<int>& key, int v, int key_val, int& comparaciones) {
    key[v] = key_val;
    heapify_up(A, key, v, comparaciones);
}

// Función para reorganizar hacia abajo (heapify down)
void heapify_down(vector<int>& A, vector<int>& key, int i, int& comparaciones) {
    int s = A.size();
    while (2 * i + 1 < s) {
        int j = 2 * i + 1;
        if (2 * i + 2 < s && key[A[2 * i + 2]] < key[A[j]]) {
            j = 2 * i + 2;
        }
        comparaciones++;
        if (key[A[i]] <= key[A[j]]) {
            break;
        }
        swap(A[i], A[j]);
        swap(key[A[i]], key[A[j]]);
        i = j;
    }
}

// Función para reorganizar hacia arriba (heapify up)
void heapify_up(vector<int>& A, vector<int>& key, int i, int& comparaciones) {
    while (i > 0 && key[A[i]] < key[A[(i - 1) / 2]]) {
        comparaciones++;
        swap(A[i], A[(i - 1) / 2]);
        swap(key[A[i]], key[A[(i - 1) / 2]]);
        i = (i - 1) / 2;
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);

    // Datos de prueba
    vector<int> A = {10, 5, 15, 30, 40, 50, 100};
    vector<int> key = {5, 4, 12, 20, 7, 25, 15};

    // Variable para contar comparaciones
    int comparaciones = 0;

    // Inicio del cronómetro
    high_resolution_clock::time_point start_time = high_resolution_clock::now();

    // Prueba del algoritmo extract_min
    int min_element = extract_min(A, key, comparaciones);

    // Fin del cronómetro
    high_resolution_clock::time_point end_time = high_resolution_clock::now();

    // Cálculo de la duración de la ejecución en microsegundos
    auto duration = duration_cast<microseconds>(end_time - start_time);

    // Mostrar resultado
    cout << "Elemento minimo: " << min_element << endl;
    cout << "Tiempo de ejecucion: " << duration.count() << " microsegundos" << endl;
    cout << "Comparaciones realizadas: " << comparaciones << endl;

    return 0;
}
