function limpiar() {
    document.getElementById('miFormulario').reset
}

function Sumar() {
    var x = parseInt(document.getElementById('Valor1').value);
    var y = parseInt(document.getElementById('valor2').value);
    document.getElementById('el-resultado').innerHTML = x+y;
}

function Restar() {
    var x = parseInt(document.getElementById('Valor1').value);
    var y = parseInt(document.getElementById('valor2').value);
    document.getElementById('el-resultado').innerHTML = x-y;
}

function Multiplicar() {
    var x = parseInt(document.getElementById('Valor1').value);
    var y = parseInt(document.getElementById('valor2').value);
    document.getElementById('el-resultado').innerHTML = x*y;
}

function Dividir() {
    var x = parseInt(document.getElementById('Valor1').value);
    var y = parseInt(document.getElementById('valor2').value);
    document.getElementById('el-resultado').innerHTML = x/y;
}
