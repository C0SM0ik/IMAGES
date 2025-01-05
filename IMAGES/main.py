from PIL import Image
from PIL import ImageFitler

with Image.open('moped.jpg') as pic:
    pic.show()
    
    pic_gray = pic.convert('L')
    pic_gray.save('test.jpg')
    pic_gray.show()
    
    pic_up = pic.transpose(Image)
    pic_up.save('test2.jpg')
    pic_up.show()
    
    pic_blur = pic.fitler(ImageFitler.BLUR)
    pic_blur.save('test3.jpg')
    pic_blur.show()
    
    print("Розмір", pic.size)
    print("Формат", pic.format)
    print("Тип", pic.mode) 
    
    
    
       