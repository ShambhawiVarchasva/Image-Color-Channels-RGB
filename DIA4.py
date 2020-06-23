import numpy as np
import cv2
from math import sqrt,cos,sin,radians


matrix = [[1,0,0],[0,1,0],[0,0,1]]
theta=0.94248

cosA = cos(theta)
sinA = sin(theta)
matrix[0][0] = cosA + (1.0 - cosA) / 3.0
matrix[0][1] = 1./3. * (1.0 - cosA) - sqrt(1./3.) * sinA
matrix[0][2] = 1./3. * (1.0 - cosA) + sqrt(1./3.) * sinA
matrix[1][0] = 1./3. * (1.0 - cosA) + sqrt(1./3.) * sinA
matrix[1][1] = cosA + 1./3.*(1.0 - cosA)
matrix[1][2] = 1./3. * (1.0 - cosA) - sqrt(1./3.) * sinA
matrix[2][0] = 1./3. * (1.0 - cosA) - sqrt(1./3.) * sinA
matrix[2][1] = 1./3. * (1.0 - cosA) + sqrt(1./3.) * sinA
matrix[2][2] = cosA + 1./3. * (1.0 - cosA)



img = cv2.imread('Gudhal.png',1)
img_hsv = np.empty(img.shape, dtype=np.uint8)


a=np.array([matrix[0][0]*x for x in img[:,:,0]])
b=np.array([matrix[0][1]*x for x in img[:,:,1]])
c=[matrix[0][2]*x for x in img[:,:,2]]

img_hsv[:, :, 0]=a+b+c


a=np.array([matrix[1][0]*x for x in img[:,:,0]])
b=np.array([matrix[1][1]*x for x in img[:,:,1]])
c=[matrix[1][2]*x for x in img[:,:,2]]

img_hsv[:, :, 1]=a+b+c

a=np.array([matrix[2][0]*x for x in img[:,:,0]])
b=np.array([matrix[2][1]*x for x in img[:,:,1]])
c=[matrix[2][2]*x for x in img[:,:,2]]

img_hsv[:, :, 2]=a+b+c
cv2.imwrite("hsv_"+str(theta)+".png", img_hsv)              


