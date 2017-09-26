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
