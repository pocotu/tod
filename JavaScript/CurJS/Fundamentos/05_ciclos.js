/**
 * Ciclos
 */

// while

var n = 0;
while (n <= 5) {
    n++; // n = n + 1
    console.log('hola ' + n);
}

// do while
/**
 * primero se ejecuta el codigo y luego se evalua la condicion
 * al menos se ejecuta una vez el codigo dentro del ciclo do while
 */
var contador = 2;
do {
    console.log('Hola' + contador);
    contador++; 
} while (contador <= 5);

// for
for(let n = 5; n <= 10; n+=2) {
    console.log('Hola'+ n);
}

// for in
/**
 * recorre las propiedades de un objeto y las imprime
 * 
 * for in solo funciona con objetos
 */
var persona = {
    nombre: 'Carlos',
    apellido: 'Rodriguez',
    edad: 22,
    sexo: 'M'

}
for (let clave in persona) {
    console.log(clave, persona[clave]);
}

// for of
/**
 * recorre los elementos de un arreglo y los imprime
 *  
 * for of solo funciona con arreglos
 * 
 */
var arreglo = [1, 2, 3, 4, 5, 6];
for(let valor of arreglo) {
    console.log('Hola '+ valor);
}