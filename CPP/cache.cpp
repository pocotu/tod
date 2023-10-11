#include <iostream>
#include <vector>
#include <unordered_map>
#include <chrono>

using namespace std;
using namespace std::chrono;

// Implementación de la función furthest-in-future
void furthestInFuture(vector<int>& pages, int cacheSize) {
    int T = pages.size();
    unordered_map<int, int> cache; // Caché para almacenar páginas
    int comparisons = 0; // Contador de comparaciones realizadas

    for (int t = 0; t < T; ++t) { // Complejidad: O(T)
        int pt = pages[t]; // Acceso a la página actual

        if (cache.find(pt) != cache.end()) { // Complejidad: O(1)
            // La página pt ya está en caché, no se hace nada.
        } else if (cache.size() < cacheSize) { // Complejidad: O(1)
            // Hay una página vacía en caché, cargar pt en el caché.
            cache[pt] = t;
        } else {
            // Encontrar la página en caché que no se utiliza furthest-in-the-future.
            int pStar = -1; // Variable para almacenar la página a desalojar
            int farthest = -1; // Variable para almacenar la posición más lejana
            for (const auto& entry : cache) { // Complejidad: O(C), donde C es el tamaño de la caché
                if (entry.second > farthest) {
                    farthest = entry.second;
                    pStar = entry.first;
                }
                comparisons++; // Incrementar el contador de comparaciones
            }

            // Desalojar la página pStar y cargar pt en el caché.
            cache.erase(pStar); // Complejidad: O(1)
            cache[pt] = t; // Complejidad: O(1)
        }
    }

    cout << "Comparaciones realizadas: " << comparisons << endl;
}

int main() {
    vector<int> pages = {1, 2, 3, 4, 5, 1, 2, 6, 7, 8}; // Conjunto de datos de ejemplo
    int cacheSize = 3; // Tamaño de la caché

    auto start = high_resolution_clock::now();
    furthestInFuture(pages, cacheSize);
    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<microseconds>(stop - start);
    cout << "Tiempo de ejecución: " << duration.count() << " microsegundos" << endl;

    return 0;
}
