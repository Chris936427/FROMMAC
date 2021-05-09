from PIL import Image
im=Image.open('psc.jpg')
r,g,b=im.split()
om=Image.merge("RGB",(b,g,r))
om.resize((128,128))
om.show()

