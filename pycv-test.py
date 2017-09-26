#Algoritmo para detectar círculos com diâmetro superior a 10 pixels

from matplotlib import pyplot as plt
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2

# Função para calculo do diametro do circulo
def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

bgr_img = cv2.imread('circles.png')
Input = cv2.imread('circles.png') # read as it is

if bgr_img.shape[-1] == 3:           # color image
    b,g,r = cv2.split(bgr_img)       # get b,g,r
    rgb_img = cv2.merge([r,g,b])     # switch it to rgb
    gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
else:
    gray_img = bgr_img

img = cv2.medianBlur(gray_img, 5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))


#####################Filtros#############################
img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img_erosion, kernel, iterations=1)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img_erosion, cv2.MORPH_CLOSE, kernel)
opening1 = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
gradient = cv2.morphologyEx(img_dilation, cv2.MORPH_GRADIENT, kernel)
