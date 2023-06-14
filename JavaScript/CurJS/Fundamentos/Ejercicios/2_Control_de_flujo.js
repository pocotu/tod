/*
1.Escribir un programa que según el día de la semana ingresado proporcione el día en inglés.
El programa debe ser escrito dos veces, una con la declaración if else y otra con la declaración switch
*/

let dia = 'lunes'

if (dia === 'lunes') {
    console.log('monday');
} else if (dia === 'martes') {
    console.log('tuesday');
} else if (dia === 'miercoles') {
    console.log('Wednesday');
} else if (dia === 'jueves') {
    console.log('thursday');
} else if (dia === 'viernes') {
    console.log('friday');
} else if (dia === 'sabado') {
    console.log('saturday');
} else if (dia === 'domingo') {
    console.log('sunday');
} else {
    console.log('dia invalido');
}

let day = 'lunes'
switch (day) {
    case 'lunes':
        console.log('monday');
        break;
    case 'martes':
        console.log('tuesday');
        break;
    case 'miercoles':
        console.log('wednesday');
        break;
    case 'jueves':
        console.log('thursday');
        break;
    case 'viernes':
        console.log('friday');
        break;
    case 'sabado':
        console.log('saturday');
        break;
    default:
        console.log('dia incorrecto');
}

/*
2.Escribir un programa que según el total de la compra, se agregue un valor de envio.
Si la compra es menor o igual a los $10 se agregará un gasto de envió de $3
Si la compra es menor o igual a los $20 y mayor a los $10 se agregará un gasto de envío de $5
Si la compra es menor o igual a los $50 y mayor a los $20 se agregará un gasto de envío de $7
Si la compra supera los $50 el gasto de envío será gratuito

El programa debe ser escrito dos veces, una con la declaración if else y otra con la declaración switch
*/
var precio = 23;

if (precio <= 10) {
    var gasto_envio = precio + 3;
    console.log('El precio total mas envio es '+gasto_envio);
} else if (10 <= precio < 20) {
    var gasto_envio = precio + 5;
    console.log('El precio total mas envio es '+gasto_envio);
} else if (20 <= precio <= 50) {
    var gasto_envio = precio + 7;
    console.log("El precio total mas envio es"+gasto_envio);
} else {
    console.log('Precio incorrecto');
}

var precio = 23;

switch (true) {
    case precio <= 10:
        var add_envio = precio + 3;
        console.log('Precio total mas envio es '+add_envio+" dolares");
        break;
    case precio>10 && precio< 20:
        var add_envio = precio + 5;
        console.log('Precio total mas envio es '+add_envio+" dolares")
        break;
    case precio>=20 && precio <= 50:
        var add_envio = precio + 7;
        console.log('Precio total mas envio es '+add_envio+" dolares");
        break;
    default:
        console.log("precio incorrecto");
} 