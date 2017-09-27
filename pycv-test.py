#
# Autor: Luiz Duarte
# E-mail: duarte.luizneto@gmail.com
#
# Deenvolvido em Python 3.6, Opencv 3.3
#
#
# Notas: Fiquei com algumas dúvidas nas medidas exatas dos circulos
#
#




from matplotlib import pyplot as plt
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2

################Função Distancia Euclidiana#################
def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)
############################################################

#####################Imagem de Entrada#################
bgr_img = cv2.imread('circles.png')
image_input = bgr_img.copy() # read as it is
#######################################################

#######################################################
if bgr_img.shape[-1] == 3:           # color image
    b,g,r = cv2.split(bgr_img)       # get b,g,r
    rgb_img = cv2.merge([r,g,b])     # switch it to rgb
    gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
else:
    gray_img = bgr_img
#######################################################

################Construção dos Filtros##################
img = cv2.medianBlur(gray_img, 5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

img_erosion = cv2.erode(img, kernel, iterations=2)
img_dilation = cv2.dilate(img_erosion, kernel, iterations=1)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img_erosion, cv2.MORPH_CLOSE, kernel)
opening1 = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)

gradient = cv2.morphologyEx(img_dilation, cv2.MORPH_GRADIENT, kernel)
############################################################

##################Transformada de Hough#####################
circles = cv2.HoughCircles(
							opening1,
							cv2.HOUGH_GRADIENT,
							1,
							100,
							param1=20,
							param2=15,
							minRadius=1,
							maxRadius=500)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
	# draw the outer circle
	cv2.circle(bgr_img,(i[0],i[1]),i[2],(0,255,255),2)
	# draw the center of the circle
	#cv2.circle(bgr_img,(i[0],i[1]),2,(0,255,255),2)
	diametroCirculo = 2*i[2]
	raio = i[2]

	print("RAIO DO CÍRCULO NA POSIÇÃO (%d,%d) =  %d" % (i[0],i[1],raio))
	print("DIÂMETRO DO CÍRCULO NA POSIÇÃO (%d,%d) =  %d" % (i[0],i[1],diametroCirculo))



####################Imagem de Saída#########################
cv2.imshow("Input Image", image_input)
cv2.imshow("Hough Transform", bgr_img)
#cv2.imshow("img_erosion",img_erosion)
#cv2.imshow("img_dilation",img_dilation)
#cv2.imshow("img_dilation",closing)
#cv2.imshow("circles",XXX)
#cv2.imshow("gradient",gradient)
#cv2.imshow("tophat", tophat)
#cv2.imshow("GRAY1", GRAY)
#cv2.imshow("edged", edged.copy())
cv2.waitKey(0)
#############################################################
