#include <iostream>
#include <vector>
#include <ctime>

using namespace std;

// Declaración de funciones
void heapify_down(vector<int>& A, vector<int>& key, int i, int& comparaciones); // Pasamos comparaciones como referencia
void heapify_up(vector<int>& A, vector<int>& key, int i, int& comparaciones); // Pasamos comparaciones como referencia

// Función para extraer el mínimo de un montículo
int extract_min(vector<int>& A, vector<int>& key, int& comparaciones) { // Pasamos comparaciones como referencia
    int ret = A[0]; // O(1)
    int last = A.back();
    int last_key = key.back();
    A.pop_back(); // O(1)
    key.pop_back(); // O(1)
    if (!A.empty()) {
        A[0] = last; // O(1)
        key[0] = last_key; // O(1)
        heapify_down(A, key, 0, comparaciones); // O(log N)
    }
    return ret; // O(1)
}

// Función para disminuir la clave de un elemento en el montículo
void decrease_key(vector<int>& A, vector<int>& key, int v, int key_val, int& comparaciones) { // Pasamos comparaciones como referencia
    key[v] = key_val; // O(1)
    heapify_up(A, key, v, comparaciones); // O(log N)
}

// Función para reorganizar hacia abajo (heapify down)
void heapify_down(vector<int>& A, vector<int>& key, int i, int& comparaciones) { // Pasamos comparaciones como referencia
    int s = A.size();
    while (2 * i + 1 < s) { // O(log N) en el peor caso
        int j = 2 * i + 1;
        if (2 * i + 2 < s && key[A[2 * i + 2]] < key[A[j]]) {
            j = 2 * i + 2;
        }
        comparaciones++; // Incrementamos el contador de comparaciones
        if (key[A[i]] <= key[A[j]]) {
            break;
        }
        swap(A[i], A[j]); // O(1)
        swap(key[A[i]], key[A[j]]); // O(1)
        i = j;
    }
}

// Función para reorganizar hacia arriba (heapify up)
void heapify_up(vector<int>& A, vector<int>& key, int i, int& comparaciones) { // Pasamos comparaciones como referencia
    while (i > 0 && key[A[i]] < key[A[(i - 1) / 2]]) { // O(log N) en el peor caso
        comparaciones++; // Incrementamos el contador de comparaciones
        swap(A[i], A[(i - 1) / 2]); // O(1)
        swap(key[A[i]], key[A[(i - 1) / 2]]); // O(1)
        i = (i - 1) / 2;
    }
}

int main() {
    // Datos de prueba
    vector<int> A = {10, 15, 30, 40, 50, 100};
    vector<int> key = {5, 12, 20, 7, 25, 15};

    // Variable para contar comparaciones
    int comparaciones = 0;

    // Inicio del cronómetro
    clock_t start_time = clock();

    // Prueba del algoritmo extract_min
    int min_element = extract_min(A, key, comparaciones);

    // Fin del cronómetro
    clock_t end_time = clock();

    // Cálculo de la duración de la ejecución
    double execution_time = double(end_time - start_time) / CLOCKS_PER_SEC;

    // Mostrar resultado
    cout << "Elemento mínimo: " << min_element << endl;
    cout << "Tiempo de ejecución: " << execution_time << " segundos" << endl;
    cout << "Comparaciones realizadas: " << comparaciones << endl;

    return 0;
}
