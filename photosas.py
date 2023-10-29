import os
from PIL import Image , ImageDraw , ImageFont , ImageFilter
files = os.listdir('photos')
for photo in files:
    with Image.open('photos/'+photo) as image:
        draw  = ImageDraw.Draw(image)
        font = ImageFont.truetype('Ghastly Panic Cyrillic/GhastlyPanicCyr.otf' , 30)
        draw.text((10 , 10)  , "pipidastr" , font=font  , fill="red")
        image.save('result/'+photo)