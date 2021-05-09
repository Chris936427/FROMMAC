import os
from PIL import Image
image_path = 'psc.jpg'
size=(60,60)
f,e =os.path.splitext(image_path)
outfile=f+".thumbnail"
if image_path!=outfile:
    try:
        im= Image.open(image_path)
        im.thumbnail(size)
        im.save(outfile,'jpeg')
    except IOError:
        print("cannot convert", image_path)