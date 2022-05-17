#Yasmin Esqueda Muñoz - Práctica 8

from matplotlib import pyplot as plt
from matplotlib import pylab 
import cv2
import imutils
import numpy as np

img = cv2.imread("donas.jpg",1)
img = cv2.resize(img,(300,300))
dst = cv2.Laplacian(img,cv2.CV_16S,ksize=3)   
dst = cv2.convertScaleAbs(dst) 
cv2.imshow("Original5",img)   
cv2.imshow("Laplace",dst)   

gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gauss = cv2.GaussianBlur(gris, (5,5), 0)
canny = cv2.Canny(gauss, 50, 150)
cv2.imshow("Canny",canny)   

rows = 300
cols = 300
ddept=cv2.CV_16S
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
x = cv2.Sobel(gray, ddept, 1,0, ksize=3, scale=1)
y = cv2.Sobel(gray, ddept, 0,1, ksize=3, scale=1)
absx= cv2.convertScaleAbs(x)
absy = cv2.convertScaleAbs(y)
edge = cv2.addWeighted(absx, 0.5, absy, 0.5,0)
cv2.imshow('Solb x & Solb y', edge)
cv2.waitKey(0) 