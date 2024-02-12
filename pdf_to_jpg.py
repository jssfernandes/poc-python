# import module
from pdf2image import convert_from_path

pages = convert_from_path('example.pdf')

for i in range(len(pages)):
    pages[i].save('page'+ str(i) +'.jpg', 'JPEG')
    
