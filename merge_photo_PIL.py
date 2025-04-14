# requirement pillow
import sys
import os
from PIL import Image, ImageFilter
from PIL import ImageFont
from PIL import ImageDraw 

os.chdir('<DIRETORIO DE LOCALIZACAO DAS FOTOS>')
print(os.getcwd())

image_list= ['IMG_1.jpg','IMG_2.jpg','IMG_3.jpg', 'IMG_4.jpg' ]

image = [Image.open(x) for x in image_list]  # list
im_1 = image[0].rotate(270)
im_2 = image[1].rotate(270)
im_3 = image[2].rotate(270)
#im_4 = image[3].rotate(270)

height = image[0].size[0]
width = image[0].size[1]
# Create an empty white image frame
new_im = Image.new('RGB',(height*2,width*2),(255,255,255))

new_im.paste(im_1,(0,0))
new_im.paste(im_2,(height,0))
new_im.paste(im_3,(0,width))
new_im.paste(im_4,(height,width))


draw = ImageDraw.Draw(new_im)
font = ImageFont.truetype('arial',200)

draw.text((0, 0), '(a)', fill='white', font=font)
draw.text((height, 0), '(b)', fill='white', font=font)
draw.text((0, width), '(c)', fill='white', font=font)
#draw.text((height, width), '(d)', fill='white', font=font)

new_im.show()
new_im.save('NEW_JOINED_IMG.jpg')   
