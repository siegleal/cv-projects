#!/usr/bin/python

import numpy as np
import cv2

img = cv2.imread('hearts-8.png', -1)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
corner = img_gray[30:175,20:80]

ret,thresh = cv2.threshold(corner,127,255,cv2.THRESH_BINARY)
#show a rectangle around the number and suit
#cv2.rectangle(img,(20,30),(80,175),(0,255,0),5)

im2,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
suit = contours[1]
value = contours[2]
x,y,w,h = cv2.boundingRect(suit)
cv2.rectangle(corner,(x,y),(x+w,y+h),(0,255,0),2)
x,y,w,h = cv2.boundingRect(value)
cv2.rectangle(corner,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('8 of diamonds', corner)
cv2.waitKey(0)
cv2.destroyAllWindows()
