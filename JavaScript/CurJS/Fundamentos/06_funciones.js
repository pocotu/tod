/**
 * Funciones
 */

// declarativas
/**
 * - estas funciones se pueden llamar antes de declararlas en el codigo 
 *   ya que el interprete de javascript las lee primero y luego las ejecuta
 * - estas funciones se guardan en memoria y se pueden reutilizar
 * - estas funciones tienen nombre
 */
function saludo() {
    console.log('Hola a todos');
}
saludo();
///////////////////////////////////////////
function saludo2(nombre){
    console.log('Hola ' + nombre);
}
saludo2('Carlos');
///////////////////////////////////////////
function saludo3(nombre) {
    console.log(`Hola ${nombre}`);
}
saludo3('Juan')
///////////////////////////////////////////
function saludo4(nombre) {
    return `Hola ${nombre}`
}
var saludar = saludo4('Gean');
console.log(saludar);

// expresion o anonimas
/**
- estas funciones no se pueden llamar antes de declararlas en el codigo
  ya que el interprete de javascript las lee primero y luego las ejecuta
- estas funciones se guardan en una variable y no en memoria
- estas funciones no tienen nombre
- estas funciones no se pueden reutilizar
 */
var suma = function(a, b) {
    return a+b;
}
console.log(suma(6, 8));


// arrow function (funciones flecha)
/**
-Se escriben con la sintaxis "() =>" en lugar de "function()".
-No tienen su propio this, en cambio heredan el this del contexto de su entorno.
-No tienen acceso a "arguments" (en cambio se tiene que usar el rest operator)
-No pueden ser usadas como constructores (no se pueden usar con new)
-No tienen el método "bind", "call" o "apply"
-No tienen un prototype
 */
var resta = (a, b) => {
    return a - b;
}
console.log("la resta es: " + resta(8, 3));
///////////////////////////////////////////
var multiplicar = (a, b) => {
    return a * b
}
console.log(multiplicar(4, 4));
///////////////////////////////////////////
var dividir = (a, b) => a/b;
console.log(dividir(8, 2));
///////////////////////////////////////////
var resta = (a, b) => {
    if (a < b) {
        console.log("no se puede operar en las Naturales");
        return 'Operacion invalida';
    } 
    var r = a-b;
    return r
} 
console.log(resta(3, 6));
console.log(resta(5, 2));
///////////////////////////////////////////
var resta = (a, b) => {
    if (typeof a === 'number' && typeof b === 'number') {
        return a - b;
    } else {
        return 'Ingrese solo numeros'
    }
}
console.log(resta('a', 'dos'));
console.log(resta(6, 2));