import numpy as np
import cv2
import math


img = cv2.imread('Gudhal.png',1)
img_cmy = np.empty(img.shape, dtype=np.uint8)




for c in (range(3)):
    
    img_cmy[:, :, c] = ([255-x for x in img[:, :, c]])
       

    
cv2.imwrite("cmy.png", img_cmy)              


