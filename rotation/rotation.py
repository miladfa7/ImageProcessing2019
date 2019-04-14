
#rotaion image
import numpy as np 
import cv2
import math as m 
import sys
import matplotlib.pyplot as plt  

img = cv2.imread('ronaldo.jpg')
angle45 = 45
angle60 = 60
angle90 = 90 
angle120 = 120
angle180 = 180 


#get rotation matrix
def rotation_matrix(cx, cy, angle):
    a = m.cos(angle*np.pi/180)
    b = m.sin(angle*np.pi/180)
    u = (1-a)*cx-b*cy
    v = b*cx+(1-a)*cy
    return np.array([[a,b,u], [-b,a,v]]) 

#determine shape of img
h = img.shape[0]
w = img.shape[1]
#print h, w
#determine center of image
cx, cy = (w / 2, h / 2)

#calculate rotation matrix 
#then grab sine and cosine of the matrix
def rotation(angle):
    #determine shape of img
    h = img.shape[0]
    w = img.shape[1]
    #determine center of image
    cx, cy = (w / 2, h / 2)

    #calculate rotation matrix 
    #then grab sine and cosine of the matrix

    mat = rotation_matrix(cx,cy, int(angle))
    cos = np.abs(mat[0,0])
    sin  = np.abs(mat[0,1])
    #calculate new height and width to account for rotation
    newWidth = int((h * sin) + (w * cos))
    newHeight = int((h * cos) + (w * sin))

    mat[0,2] += (newWidth / 2) - cx
    mat[1,2] += (newHeight / 2) - cy
    
    return mat,newWidth,newHeight

R45,newWidth45,newHeight45 = rotation(angle45)
R60,newWidth60,newHeight60 = rotation(angle60)
R90,newWidth90,newHeight90 = rotation(angle90)
R120,newWidth120,newHeight120 = rotation(angle120)
R180,newWidth180,newHeight180 = rotation(angle180)

#this is how the image SHOULD look
img45 = cv2.warpAffine(img, R45, (newWidth45,newHeight45))
img60 = cv2.warpAffine(img, R60, (newWidth60,newHeight60))
img90 = cv2.warpAffine(img, R90, (newWidth90,newHeight90))
img120 = cv2.warpAffine(img, R120, (newWidth120,newHeight120))
img180 = cv2.warpAffine(img, R180, (newWidth180,newHeight180))

plt.figure(figsize=(12,10))
plt.subplot(231),plt.imshow(img),plt.title('Original image')
plt.subplot(232),plt.imshow(img45),plt.title('Rotation 45°')
plt.subplot(233),plt.imshow(img60),plt.title('Rotation 60°')

plt.figure(figsize=(12,10))
plt.subplot(231),plt.imshow(img90),plt.title('Rotation 90°')
plt.subplot(232),plt.imshow(img120),plt.title('Rotation 120°')
plt.subplot(233),plt.imshow(img180),plt.title('Rotation 180°')

plt.show()

#cv2.imshow('dst', dst)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


