from PIL import Image

with Image.open('img.png')as pic_original:
    pic_gray  = pic_original.convert('L')
    pic_gray.save('gay.jpg')
    print('Зображення відкрито \nРозмір:' , pic_gray.size)
    print('Формат:' , pic_gray.format)
    print('тон :'  , pic_gray.mode)
    pic_gray.show()