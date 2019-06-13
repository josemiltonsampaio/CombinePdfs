#! python3
# combinePdfs.py - Combines all the PDFs in the current working directory into
# a single PDF.

import PyPDF2
import os
import argparse

parser = argparse.ArgumentParser(prog="JuntaPDF's",
                                 description="Junta PDF's em um único arquivo (combinado.pdf)")
parser.add_argument(
    '--caminho', help="Caminho da pasta onde estão os PDF's, se não for informado, utiliza a pasta atual", default=".")
args = parser.parse_args()

if os.path.exists(args.caminho) == False:
    input("O caminho informado não existe, por favor verifique.")
    exit()


# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir(args.caminho):
    if filename.endswith('.pdf') and filename != 'combinado.pdf':
        pdfFiles.append(args.caminho + '\\' + filename)
pdfFiles.sort()

if len(pdfFiles) == 0:
    input("O caminho informado não possui PDF's, por favor verifique.")
    exit()

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Loop through all the pages (except the first) and add them.
    for pageNum in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open(args.caminho + '\combinado.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
