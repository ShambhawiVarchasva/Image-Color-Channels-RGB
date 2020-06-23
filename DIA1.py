import numpy as np
import cv2
import math
import matplotlib.pyplot as plt

pic = cv2.imread('Gudhal.png')



for c in (range(3)):
    
    
    split_img = np.zeros(pic.shape, dtype="uint8") 
    if(c==0):
     plt.title('R channel')
    if(c==1):
     plt.title('G channel')
    if(c==2):
     plt.title('B channel')
    plt.ylabel('Height {}'.format(pic.shape[0]))
    plt.xlabel('Width {}'.format(pic.shape[1]))
    
    split_img[ :, :, c] = pic[ :, :, c]
    cv2.imwrite("splitting_channel_"+str(c)+".png", split_img)  
    
    plt.imshow(split_img)
    plt.show()
