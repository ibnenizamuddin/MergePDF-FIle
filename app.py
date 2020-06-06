from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger


def reversedpdf():

    output_pdf = PdfFileWriter()

    with open('pdffile.pdf', 'rb') as readfile:
        input_pdf = PdfFileReader(readfile)

        for page in reversed(input_pdf.pages):
            output_pdf.addPage(page)

        with open('PDF/New/output.pdf', "wb") as writefile:
            output_pdf.write(writefile)


def mergepdf():

    pdfs = ['1.pdf', '2.pdf']

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write("Output.pdf")
    merger.close()



