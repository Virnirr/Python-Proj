import PyPDF2
import sys

# grab all the arguments besides the first argument into a list called inputs
inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    # merger object with PyPDF, gives us a merger object
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        # append or merge all of the pdfs that we are going to loop through
        # at the end of the loop, the merger will have all the of the pdfs
        merger.append(pdf)
    merger.write('super.pdf')

#
pdf_combiner(inputs)