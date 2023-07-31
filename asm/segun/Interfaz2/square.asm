section .text
global square
square:
    mov eax, edi       ;Mueve el argumento a EAX
    imul eax, eax      ;Multiplica EAX por si mismo (calcula el cuadrado)
    ret                ;Devuelve el resultado

