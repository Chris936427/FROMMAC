
from PIL import Image
im=Image.open('psc.jpg')
print(im.format)
im.save("psc.png",'PNG')
ik=Image.open('psc.png')
print(ik.format)