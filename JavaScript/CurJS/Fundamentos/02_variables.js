/*
Variables: son pequeñas cajas donde podemos guardar datos

3 formas de defenir variables:

var: se puede reasignar el valor de la variable y se puede usar fuera 
del bloque de codigo donde se definió

let: se puede reasignar el valor de la variable pero solo dentro 
del bloque de codigo donde se definió

CONST: no se puede reasignar el valor de la variable, no podemos cambiar 
el valor de la variable por fuera de la funcion donde se definió
*/

// variables con VAR
var nombre = 'Pedro'; //
console.log(nombre);

var edad = 27;
console.log(edad);

var persona = {
    nombre: 'Pedro',
    apellido: 'Arguello',
    edad: '27',
    direccion: {
        calle: 'Buena Vista',
        numero_de_casa: 4,
    },
    ciudades_visitadas: [
        'Bogota', 'Medellin', 'Cali'
    ]
}

var ciudad;
ciudad = 'Lima';
ciudad = 'Guayaquil'
ciudad = 12;
console.log(ciudad);

// variables con LET

let nombre2 = 'Thalia';
console.log(nombre2);

{
    let saludo = "Hola"; // let solo existe dentro del bloque de codigo
    console.log(saludo);

}

console.log(saludo);

{
    var saludo = "Hola"; // var existe fuera del bloque de codigo
    console.log(saludo);

}

console.log(saludo);


// variables con CONST
const PI = 3.1416;
//PI = 3.14; // no se puede reasignar el valor de una constante
console.log(PI);


var nombre = 'Pedro';
var saludo2 = `Hola ${nombre}`; // template string
console.log(saludo);
console.log(saludo2);