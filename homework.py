import os
from PIL import Image , ImageDraw , ImageFont , ImageFilter
files = os.listdir('photos2')
for photo in files:
    with Image.open('photos2/'+photo) as image:
        image = image.filter(ImageFilter.GaussianBlur(10))
        image.save('result2/' + photo)



