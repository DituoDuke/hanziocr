import cv2
import numpy as np

# read image
img = cv2.imread('image.png')
# show image
cv2.imshow('image', img)

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
            cv2.rectangle(display, (vetor1[0],vetor1[1]),(vetor2[0],vetor2[1]),(0,255,0),3)
            cv2.imshow('image', display)
        except:
            print("waiting for second vector")
    #     # font for left click event
    #     font = cv2.FONT_HERSHEY_TRIPLEX
    #     LB = 'Left Button'
        
    #     # display that left button 
    #     # was clicked.
    #     cv2.putText(img, LB, (x, y), 
    #                 font, 1, 
    #                 (255, 255, 0), 
    #                 2) 
    #     cv2.imshow('image', img)
        
        
    # # to check if right mouse 
    # # button was clicked
    # if event == cv2.EVENT_RBUTTONDOWN:
         
    #     # font for right click event
    #     font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    #     RB = 'Right Button'
        
    #     # display that right button 
    #     # was clicked.
    #     cv2.putText(img, RB, (x, y),
    #                 font, 1, 
    #                 (0, 255, 255),
    #                 2)
    #     cv2.imshow('image', img)

cv2.setMouseCallback('image', mouse_click)
cv2.waitKey(0)
print(vetor1)
print(vetor2)
# close all the opened windows.
cv2.destroyAllWindows()