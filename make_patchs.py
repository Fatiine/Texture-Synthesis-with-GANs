from PIL import Image
import os, sys
import numpy as np
    
main_image = np.array(Image.open("water-texture-main.png").convert('RGB'))

patch_size = 128

npatches = 1000

for i in range(npatches):
    i1 = np.random.randint(0,main_image.shape[0]-patch_size)
    i2 = np.random.randint(0,main_image.shape[1]-patch_size)
    patch = main_image[i1:i1+patch_size,i2:i2+patch_size,:]
    im = Image.fromarray(patch)
    #im = im.resize((32, 32), Image.ANTIALIAS)
    im.save("patchset3/patchno"+str(i)+".jpg",'JPEG', quality=90)