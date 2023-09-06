document.addEventListener('DOMContentLoaded', function () {
  const csvTable = document.getElementById('csvTable');

  // Ruta al archivo CSV que quieres leer
  const archivoCSV = '/workspaces/tod/Proy/Horario/DR.csv';

  fetch(archivoCSV)
      .then(response => response.text())
      .then(data => {
          const rows = data.trim().split('\n');
          const headers = rows[0].split(',');
          const table = document.createElement('table');
          const thead = document.createElement('thead');
          const tbody = document.createElement('tbody');

          // Crear encabezados de la tabla
          const headerRow = document.createElement('tr');
          for (const header of headers) {
              const th = document.createElement('th');
              th.textContent = header;
              headerRow.appendChild(th);
          }
          thead.appendChild(headerRow);
          table.appendChild(thead);

          // Crear filas de datos
          for (let i = 1; i < rows.length; i++) {
              const rowData = rows[i].split(',');
              const row = document.createElement('tr');
              for (const cellData of rowData) {
                  const td = document.createElement('td');
                  td.textContent = cellData;
                  row.appendChild(td);
              }
              tbody.appendChild(row);
          }
          table.appendChild(tbody);

          // Agregar la tabla al elemento HTML
          csvTable.appendChild(table);
      })
      .catch(error => console.error('Error al cargar el archivo CSV:', error));
});
