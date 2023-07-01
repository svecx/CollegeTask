import cv2
import math

w = 200
h = 100

image1 = cv2.imread('ps1.jpg')
gray1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
resize1 = cv2.resize(gray1,(w,h))

image2 = cv2.imread('ps2.jpg')
gray2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
resize2 = cv2.resize(gray2,(w,h))

dist = 0;
for i in range(1,w):
    for j in range(1,h):
        dist = dist + ((int(resize1[j,i]) - int(resize2[j,i]))**2)


dist = math.sqrt(dist) / (w*h)
print(dist)