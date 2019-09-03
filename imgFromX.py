from tkinter.filedialog import *
from tkinter import *
from pdf2image import *
import zipfile
import filetype
import fitz

Tk().withdraw()
filename = askopenfilename()


def getFiles(path):
    EmbeddedFiles = zipfile.ZipFile(path).namelist()
    ImageFiles = [F for F in EmbeddedFiles if F.count('.jpg') or F.count('.jpeg') or F.count('.png') ]
    for Image in ImageFiles:
        zipfile.ZipFile(path).extract(Image)

def fromPdf(path):
    i = 0
    doc = fitz.open(path)
    while i < doc.pageCount:
        try:
            page = doc.loadPage(i) #number of page
            pix = page.getPixmap()
            output = "outfile"+str(i)+".png"
            pix.writePNG(output)
            i += 1
        except:
            break


#getFiles(filename)
try:
    if filetype.guess(filename).extension == 'pdf':
        fromPdf(filename)
    else:
        getFiles(filename)
except AttributeError:
    print("You selected an unsupported file type")