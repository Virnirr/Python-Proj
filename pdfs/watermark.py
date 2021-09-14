import PyPDF2
import sys
import os

inputs = sys.argv[1:]

def watermark(pdf_list):
    with open('./wtr.pdf', "rb") as file:
        watermark = PyPDF2.PdfFileReader(file)
        for pdf in pdf_list:
            clean_name = os.path.splitext(pdf)[0]
            with open(f'./{pdf}', "rb") as pdf_files:
                working = PyPDF2.PdfFileReader(pdf_files)
                watermark_page = watermark.getPage(0)
                pdf_writer = PyPDF2.PdfFileWriter()
                for page in range(working.getNumPages()):
                    filtered_pages = working.getPage(page)

                    filtered_pages.mergePage(watermark_page)

                    pdf_writer.addPage(filtered_pages)
                    
                with open(f'./watermark/{clean_name}.pdf', "ab") as file_output:
                    pdf_writer.write(file_output)

watermark(inputs)