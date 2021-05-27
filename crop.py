from PIL import Image
import os

left = 2073
top = 300
right = 3590
bottom = 2400
directory = r'Images'
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        
        im = Image.open(directory+r"\\"+filename)
        # Cropped image of above dimension
        # (It will not change orginal image)
        im1 = im.crop((left, top, right, bottom))
        new_save = r"Images\\"
        new_save = new_save+filename
        print(filename)
        im1.save(new_save)