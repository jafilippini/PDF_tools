import PyPDF2
import sys

def pdf_combiner(input,output):
    merge=PyPDF2.PdfFileMerger()
    for pdf in input:
        print(pdf)
        merge.append(pdf)
    merge.write(output)
    
output=sys.argv[1]
inputs=sys.argv[2:]
pdf_combiner(inputs,output)

