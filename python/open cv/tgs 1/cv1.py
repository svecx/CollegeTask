import cv2
import numpy as np

img = cv2.imread('ps1.jpg')
px = img[100,100]
print("total px :", px)

blue = img[100,100,0]
print("total px : ", blue)