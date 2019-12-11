from PIL import Image
import os, sys

path = "/home/pedro/object_detection/data/images/raw/"
dirs = os.listdir( path )


def resize():
    i = 0 
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((720,540), Image.ANTIALIAS)
            imResize.save('Image_'+str(i)+'.JPG', 'JPEG', quality=90)
            i=i+1
            print("done image " + str(i))

resize()
