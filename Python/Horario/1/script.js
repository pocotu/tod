// Función para convertir una cadena de caracteres a un elemento HTML
function htmlToElement(html) {
    var template = document.createElement('template');
    template.innerHTML = html.trim();
    return template.content.firstChild;
  }
  
  // Cargar y procesar el archivo Excel
  var input = document.createElement('input');
  input.type = 'file';
  input.accept = '.xls';
  
  input.addEventListener('change', function(e) {
    var file = e.target.files[0];
    var reader = new FileReader();
  
    reader.onload = function(e) {
      var data = new Uint8Array(e.target.result);
      var workbook = XLSX.read(data, { type: 'array' });
      var worksheet = workbook.Sheets[workbook.SheetNames[0]];
      var jsonData = XLSX.utils.sheet_to_json(worksheet, { header: 1 });
  
      var tableBody = document.querySelector('#catalogo tbody');
  
      // Generar filas de tabla a partir de los datos del archivo Excel
      jsonData.forEach(function(row, rowIndex) {
        if (rowIndex === 0) return; // Ignorar la primera fila (encabezados)
  
        var curso = row[0];
        var horario = row[1];
  
        var html = `<tr><td>${curso}</td><td>${horario}</td></tr>`;
        var tableRow = htmlToElement(html);
        tableBody.appendChild(tableRow);
      });
    };
  
    reader.readAsArrayBuffer(file);
  });
  
  // Adjuntar el input al cuerpo del documento y mostrarlo
  document.body.appendChild(input);
  