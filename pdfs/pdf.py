import PyPDF2

# open as read + binary (rb) mode since python reads binary for files
# convert the file object to binary mode so that the PyPDF2 reads the binary object
with open('./dummy.pdf', "rb") as file:
    # allows us to read pdf files using the method PdfFileReader()
    reader = PyPDF2.PdfFileReader(file) 
    print(reader.numPages) # method tells us the number of pages in the pdf

    # get first page
    print(reader.getPage(0)) # method that tells us the page object

    # PyPDF2 needs to know what to rotate, so we need to get the page of the reader
    # to rotate it 
    page = reader.getPage(0)
    # gives back an object, but in computer memory, so original pdf does not change
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter() # create a writer variable that allows us to write the object in memory
    writer.addPage(page) # give writer the page that we rotated
    with open("tilt.pdf", 'wb') as new_file:
        writer.write(new_file)  