#! python3
# combinePdfs.py - Combines all the PDFs in the current working directory into
# a single PDF.

import PyPDF2
import os
import argparse
import sys

dragPath = ""
parameterPath = "."

# parser = argparse.ArgumentParser(prog="JuntaPDF's",
#                                 description="Junta PDF's em um único arquivo (combinado.pdf)")
# parser.add_argument(
#    '--caminho', help="Caminho da pasta onde estão os PDF's, se não for informado, utiliza a pasta atual", default=".")
#args = parser.parse_known_args()

#print("args", args)

print(sys.argv)
print('teste')

x = 0

for atributo in sys.argv[1:]:
    x += 1
    if atributo.startswith("caminho"):
        parameterPath = atributo[8:]
        print("caminho", x, parameterPath)
    else:
        if atributo.strip != "":
            dragPath = atributo
            print("caminho2", x, atributo)


if dragPath != "":
    parameterPath = dragPath

if os.path.exists(parameterPath) == False:
    print("caminho", parameterPath)
    input("O caminho informado não existe, por favor verifique.")
    sys.exit()

if len(dragPath) > 0:
    if parameterPath == '.':
        if os.path.exists(dragPath):
            parameterPath = dragPath

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir(parameterPath):
    if filename.endswith('.pdf') and filename != 'combinado.pdf':
        pdfFiles.append(parameterPath + '\\' + filename)
pdfFiles.sort()

if len(pdfFiles) == 0:
    input("O caminho informado não possui PDF's, por favor verifique.")
    sys.exit()

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
pdfOutput = open(parameterPath + '\combinado.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
