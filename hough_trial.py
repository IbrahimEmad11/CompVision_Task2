import numpy as np
import cv2
import math



def draw_hough_elipses(path):
    img = cv2.imread(path)
    img = cv2.resize(img,(512,512))
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # ret , threshold = cv2.threshold(imgray,20,255,0)
    edges = cv2.Canny(imgray,100, 200)

    contours, hierarchy = cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    img= cv2.drawContours(img,contours,-1,(0,255,0),2)
    return img

