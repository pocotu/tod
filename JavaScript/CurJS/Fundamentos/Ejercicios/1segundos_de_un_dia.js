// Escribir un programa que calcule el número de segundos que existen en un día.
// Para ello debemos multiplicar los segundos de un minuto, por los minutos de
// una hora, por las horas de un día. Como todo el mundo sabe, un día tiene 86400 segundos.

var segundos = 60;
var minutos = 60;
var horas = 24;
var segundo_en_un_dia = segundos*minutos*horas;
console.log(segundo_en_un_dia);
