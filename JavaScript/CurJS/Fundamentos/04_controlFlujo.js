/**
 * Control de flujo
 */

// IF
// if (condicion) {

// }

var llueve = true;
if (llueve) {
    console.log("esta cayendo agua :v");
}

var administrador = 'administrador';
if (administrador == 'administrador') {
    console.log("Bienvenido administrador");
}


const MayorDeEdad = 18;
var edad1 = 15;
var edad2 = 20;

if (edad >= MayorDeEdad) {
    console.log("Es mayor de edad");
} else {
    console.log("Es menor de edad");
}

// ahora para las dos variables en una sola condicion
if (edad1 >= MayorDeEdad && edad2 >= MayorDeEdad) { // && = and
    console.log("Ambos son mayores de edad");
} else {
    console.log("Uno de los dos es menor de edad");
}

// ahora para las dos variables en una sola condicion
if (edad1 >= MayorDeEdad || edad2 >= MayorDeEdad) { // || = or
    console.log("Al menos uno es mayor de edad");
} else {
    console.log("Ninguno es mayor de edad");
}


