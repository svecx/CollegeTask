import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('pp.jpg',0)

template = cv2.imread('pp_face.jpg',0)
w,h = template.shape[::-1]

res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.4
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    img = cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

