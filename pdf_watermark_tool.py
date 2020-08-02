# herramienta para sumar marca de agua (watermark) a documentos PDF
# invocación:  pythin pdf_watermark_tool.py source_pdf_file watermark_pdf_file output_pdf_file_name
# source_pdf_file: archivo fuente a estampar
# watermark_pdf_file: archivo donde se encuentra la marca de agua a utilizar
# output_pdf_file_name: archivo a ser creado con el resultado

import sys
import PyPDF2
import os

# leo los argumentos <file pdf origen> <file pdf watermark> <file pdf deseado de destino>
input_pdf_file = sys.argv[1]
wm_pdf_file = sys.argv[2]
output_pdf_file = sys.argv[3]

# abro el archivo pdf y lo asigno a un objeto <pdf_file.pdf>
in_file = open(input_pdf_file, 'rb')
pdf_file = PyPDF2.PdfFileReader(in_file)

# abro el archivo de marca de agua y lo asigno a un objeto <wm.pdf>
wm_input_file = open(wm_pdf_file, 'rb')
wm_file = PyPDF2.PdfFileReader(wm_input_file)

# obtengo el número de páginas del pdf_file
number_of_pages = pdf_file.getNumPages()
print(f'Páginas a estampar con marca de agua -> {number_of_pages}')

# extraigo la página con la marca de agua a estampar
wm = wm_file.getPage(0)

# generos el objeto "pdf file" de salida
out_file = PyPDF2.PdfFileWriter()

# en cada página del objeto <pdf_file.pdf> le hago un merge con la página 0 del objeto <wm.pdf> y cada página combinada la sumo al objeto
# de salida <out_file>
for page in range(0, number_of_pages):
    print(f'page -> {page}')
    pdf_page = pdf_file.getPage(page)
    pdf_page.mergePage(wm)
    out_file.addPage(pdf_page)

# ya con el objeto de salida <out_file> completo, lo grabo en un archivo con el nombre ingresado como parámetro
# with open(output_pdf_file, 'wb') as output_file:
#   out_file.write(output_file)
output_file = open(output_pdf_file, 'wb')
out_file.write(output_file)
