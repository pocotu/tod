from pdf2docx import parse
from typing import Tuple

def convertidorPDF_WORD(input_file: str, output_file: str, pages: Tuple = None):
    #Convertidor de PDF a WORD
    if pages:
        pages = [int(i) for i in list(pages) if i.isnumeric()]
    result = parse(pdf_file = input_file, docx_file = output_file, pages = pages)

    summary = {'File': input_file, 'Pages': str(pages), 'Output File': output_file}

    print('## summary #####################################')
    print('\n'.join('{}: {}'.format(i, j) for i, j in summary.items()))
    print('## summary #####################################')
    return result

# para ver si esta siendo ejecutado
if __name__ == '__main__':
    # ruta y nombre de archivo de entrada
    input_file = 'E:\prueba.pdf'
    # ruta y nombre de archivo de salida
    output_file = 'E:\pc.docx'
    convertidorPDF_WORD(input_file, output_file)

