import pandas as pd

# Leer el archivo XLS y convertirlo en un DataFrame
file_path = "ruta/al/archivo.xls"  # Ruta al archivo descargado
df = pd.read_excel(file_path, engine="openpyxl")

# Generar el código HTML de la tabla
table_html = df.to_html(index=False)

# Mostrar la tabla en una página web
html = f"""
<html>
<head>
    <title>Tabla de Cursos</title>
    <style>
        table {{border-collapse: collapse;}}
        th, td {{border: 1px solid black; padding: 8px;}}
    </style>
</head>
<body>
    {table_html}
</body>
</html>
"""

# Guardar el código HTML en un archivo
with open("tabla_cursos.html", "w") as file:
    file.write(html)
