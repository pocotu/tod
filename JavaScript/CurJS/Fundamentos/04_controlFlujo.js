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
    console.log('Bienvenido tardes administrador');
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

// semaforo
var semaforo = 'azul';
if (semaforo == 'verde') {
    console.log('Continue');
} else if (semaforo == 'amarillo') {
    console.log('Listo?');
} else if (semaforo == 'rojo') {
    console.log('Detente');
} else {
    console.log('Color no valido');
}

// switch
var producto = 'papaya';
switch (producto) {
    case 'papaya': // se ejecuta si la expresion es igual a la expresion
        console.log('cuesta 1.50 soles');
        break;
    case 'naranja':
        console.log('cuesta 1.00 soles');
        break;
    case 'mango':
        console.log('cuesta 2.00 soles');
        break;
    default: // se ejecuta si no se cumple ninguna de las condiciones
        console.log('Producto no encontrado');
}