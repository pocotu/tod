import mysql.connector

# Establecer la conexión
conexion = mysql.connector.connect(
    host="localhost",
    user="usuario",
    password="contraseña",
    database="basededatos"
)

# Crear un cursor
cursor = conexion.cursor()

# Ejecutar la consulta
codigo_curso = "ABC123"
consulta = "SELECT * FROM alumnos WHERE curso_id = %s"
cursor.execute(consulta, (codigo_curso,))

# Recuperar los resultados
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()


#import requests
#from bs4 import BeautifulSoup
#
## URL de la página y código de curso
#url = "http://ccomputo.unsaac.edu.pe/index.php?op=alcurso"
#codigo_curso = "DE901AME"
#
## Parámetros para enviar en la consulta
#parametros = {"codigo": codigo_curso}
#
## Realizar la consulta GET
#response = requests.get(url, params=parametros)
#
## Verificar el código de estado de la respuesta
#if response.status_code == 200:
#    # Analizar el contenido HTML con Beautiful Soup
#    soup = BeautifulSoup(response.content, 'html.parser')
#    
#    # Encuentra la etiqueta o clase que contiene la lista de alumnos
#    lista_alumnos = soup.find('div', class_='ttexto')
#    
#    if lista_alumnos:
#        # Imprime la lista de alumnos
#        print(lista_alumnos.get_text())
#    else:
#        print("No se encontró la lista de alumnos en la página.")
#else:
#    print("Error al realizar la consulta:", response.status_code)
