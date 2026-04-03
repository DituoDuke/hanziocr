import cv2
import numpy as np
from screenshot import capture_region
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
capturePath = os.path.join(BASE_DIR, "results", "screenshot_full.png")

def initiateFullImage():
    # read image
    img = cv2.imread(capturePath)
    # show image
    # cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)
    cv2.imshow('image', img)
    cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, 1)

    #define the events for the
    # mouse_click.
    def mouse_click(event, x, y, 
                    flags, param):
        global mouseX, mouseY
        global vetor1, vetor2
        global changingFirst
        # # to check if left mouse 
        # # button was clicked
        if event == cv2.EVENT_LBUTTONDOWN:
            print(x,y)
            mouseX, mouseY = x,y
            try:
                if changingFirst:
                    vetor1 = [mouseX,mouseY]
                    changingFirst = False
                else:
                    vetor2 = [mouseX,mouseY]
                    changingFirst = True
            except:
                vetor1 = [mouseX,mouseY]
                changingFirst = False
            try:
                display = img.copy()
                cv2.rectangle(display, (vetor1[0],vetor1[1]),(vetor2[0],vetor2[1]),(0,255,0),2)
                cv2.imshow('image', display)
            except:
                print("waiting for second vector")
       

    cv2.setMouseCallback('image', mouse_click)
    cv2.waitKey(0)
    print(vetor1)
    print(vetor2)
    global left, right, up, down
    if vetor1[0] < vetor2[0]:
        left = vetor1[0]
        right = vetor2[0]
    else:
        left = vetor2[0]
        right = vetor1[0]
    if vetor1[1] < vetor2[1]:
        up = vetor1[1]
        down = vetor2[1]
    else:
        up = vetor2[1]
        down = vetor1[1]
    capture_region(left,up,right,down)
    # close all the opened windows.
    cv2.destroyAllWindows()
