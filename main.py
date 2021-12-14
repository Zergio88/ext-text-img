import sys
import os
from PIL import Image #python imagine library
import pytesseract
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#filename = 'C:\\Users\\Sergio\\Documents\\ext-text-img\\imagen2.jpg'
filename = 'C:\\Users\\Sergio\\Desktop\\img-prueba\\netbookblk.jpeg'
outfile = 'extraccion.txt'
f = open(outfile, 'a')
text = str(((pytesseract.image_to_string(Image.open(filename)))))
text = text.replace('-\n','')
f.write(text)
f.close()
print("Terminado")