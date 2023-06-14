/**
 *  Operadores
 *
 */

/**
 * Operadores de asignacion
 */

// operador de asignacion
var a = 2;

// operador de asignacion de adicion ( += )
var x = 3;
var y= 5;

x += y
console.log(x);

// operador de asignacion de sustraccion ( -= )

y -= y
console.log(y);

// operador condicional ( ? )
console.log(2 > 5 ? 'el mayor' : 'es menor');

// operador de desestructuracion
var persona = {
    nombre: 'Carlos',
    apellido: 'Rodri'
}

var {nombre, apellido} = persona;
console.log(nombre);
console.log(apellido);
console.log(persona);

// desestructuracion de arreglos
var arreglo = [1, 2, 3, 4, 5, 6]
var [primera] = arreglo;
var [pri, segundo] = arreglo;
console.log(primera);
console.log(segundo);

/**
 *  Operador de miembro o acceso de propiedad
 */

// notacion punto
var persona = {
    nombre: 'Aurelio',
    apellido: "Bellido"
}
console.log(persona.nombre);
console.log(persona.apellido);

// notacion por corchetes
var persona = {
    nombre: 'Aurelio',
    apellido: "Bellido"
}
console.log(persona['nombre']);

// notacion por corchetes en arreglos
var arreglo = [1, 2, 3, 4, 5, 6]
console.log(arreglo[2]);
console.log(arreglo[-1]); // no existe

// operacion de determinacion de tipo de dato
console.log(typeof 'Bellido');
console.log(typeof 2);
console.log(typeof persona);
console.log(typeof arreglo);
