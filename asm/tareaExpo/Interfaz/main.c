// Ejemplo de llamada a una funcion en ensamblador desde C
// Compilar: gcc -o main main.c square.s
#include <stdio.h>
extern int square(int x);  // Declaracion de la funcion en ensamblador
int main() {
    int num = 5;
    int result = square(num);  // Llamada a la funcion en ensamblador
    printf("El cuadrado de %d es %d\n", num, result);
    return 0;
}

