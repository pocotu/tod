#import requests
#import os
#
## URL directa del archivo TA.xls
#file_url = "http://ccomputo.unsaac.edu.pe/pdfreports.php?op=cat&dt=2023-1|TA/TA.xls"
#
## Nombre del archivo de destino
#file_name = "TA.xls"
#
## Directorio de destino dentro de la misma ruta del archivo Python
#download_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "descargas")
#
## Crear el directorio si no existe
#if not os.path.exists(download_dir):
#    os.makedirs(download_dir)
#
## Ruta completa del archivo de destino
#file_path = os.path.join(download_dir, file_name)
#
## Descargar el archivo
#response = requests.get(file_url)
#with open(file_path, 'wb') as file:
#    file.write(response.content)
#print(f"Archivo descargado: {file_path}")

import requests
import os

# Lista de prefijos de archivos a descargar
prefijos = ['AE', 'AN', 'AO', 'AQ', 'AT', 'BI', 'CC', 'CI', 'CO', 'DR', 'EE', 'EI', 'EN', 'EO', 'EU', 'EY', 'FI',
            'FL', 'FO', 'GI', 'HI', 'IA', 'IC', 'IN', 'IR', 'LI', 'MC', 'MD', 'ME', 'MI', 'MT', 'OD', 'OS', 'PQ',
            'PS', 'QF', 'QI', 'QM', 'TU', 'VE', 'VS', 'ZO']

# URL base
base_url = "http://ccomputo.unsaac.edu.pe/pdfreports.php?op=cat&dt=2023-1"

# Directorio de destino dentro de la misma ruta del archivo Python
download_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "descargas")

# Crear el directorio si no existe
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Iterar sobre los prefijos y descargar los archivos correspondientes
for prefijo in prefijos:
    # Construir la URL de descarga
    file_url = f"{base_url}|{prefijo}/{prefijo}.xls"
    
    # Nombre del archivo de destino
    file_name = f"{prefijo}.xls"

    # Ruta completa del archivo de destino
    file_path = os.path.join(download_dir, file_name)

    # Descargar el archivo
    response = requests.get(file_url)
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print(f"Archivo descargado: {file_path}")
