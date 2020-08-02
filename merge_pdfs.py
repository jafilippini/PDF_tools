# herramienta para concatenar files .pdf
# invocación: python merge_pdfs.py out.pdf in_1.pdf in_2.pdf.....in_n.pdf
# out.pdf será el file con la concatenación de archivos de entrada in_1.pdf.....in_n.pdf
# todos los files (merge_pdfs.py y in_1.pdf.....in_n.pdf) deben estar en el mismo directorio, de lo contrario en las entradas colocar el path de
# cada archivo. El archivo de salida out.pdf será creado por default en el mismo directorio que merge_pdfs.py, de lo contrario, colocar el path
# deseado

import PyPDF2
import sys


def pdf_combiner(input, output):
    merge = PyPDF2.PdfFileMerger()
    for pdf in input:
        print(pdf)
        merge.append(pdf)
    merge.write(output)


output = sys.argv[1]
inputs = sys.argv[2:]
pdf_combiner(inputs, output)
print(f'All done!. Files concatenated on {output} file')
