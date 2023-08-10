//; Seccion de codigo que calcula el cuadrado de un numero
//section .text
//global square
//square:
//    mov eax, edi       ;Mueve el argumento a EAX
//    imul eax, eax      ;Multiplica EAX por si mismo (calcula el cuadrado)
//    ret                ;Devuelve el resultado en EAX
//
//; Seccion de codigo que calcula el cubo de un numero
//section .text
//global cube
//cube:
//    mov eax, edi       ;Mueve el argumento a EAX
//    imul eax, edi      ;Multiplica EAX por el argumento (calcula el cubo)
//    imul eax, edi      ;Multiplica EAX por el argumento (calcula el cubo)
//    ret                ;Devuelve el resultado en EAX
//
//; Seccion de codigo que calcula el factorial de un numero
//section .text
//global factorial
//factorial:
//    mov eax, edi       ;Mueve el argumento a EAX
//    mov ecx, edi       ;Mueve el argumento a ECX
//    dec ecx            ;Decrementa ECX en 1
//    cmp ecx, 0         ;Compara ECX con 0
//    je .end            ;Si ECX es 0, salta a .end
//    .loop:             ;Etiqueta .loop
//        imul eax, ecx  ;Multiplica EAX por ECX
//        dec ecx        ;Decrementa ECX en 1
//       cmp ecx, 0     ;Compara ECX con 0
//        jne .loop      ;Si ECX no es 0, salta a .loop
//    .end:              ;Etiqueta .end
//    ret                ;Devuelve el resultado en EAX

// Implementar en C ese codigo en ensamblador

#include <stdio.h>

extern int square(int);
extern int cube(int);
extern int factorial(int);

int main(void)
{
    int n;
    printf("Ingrese un numero: ");
    scanf("%d", &n);
    printf("El cuadrado de %d es %d\n", n, square(n));
    printf("El cubo de %d es %d\n", n, cube(n));
    printf("El factorial de %d es %d\n", n, factorial(n));
    return 0;
}

// gcc -c main.c
// nasm -f elf32 -o funciones.o funciones.asm
//
