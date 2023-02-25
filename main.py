import numpy as np
import matplotlib.pyplot as plt
import cv2

##############
## VARIABLE ##
##############

# True while mouse button down
drawing = False
ix = -1
iy = -1

##############
## FUNCTION ##
##############

def draw_rectangle(event, x, y, flags, params):
    global ix,iy,drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        # this updates each frame, and updates the drawing of the rectangle while mouse moves
        # if you omit the mouse move, it still draws the rectangle, but at the end of the mouse down and up events

        if drawing == True:
            cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False;
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)


##########################
## SHOW IMG WITH OPENCV ##
##########################

img = np.zeros(shape=(512,512,3))

"""These connect the draw_circle function to the imshow() below"""
# set the window to do actions in
cv2.namedWindow(winname="my_drawing")

# add mouse events, then tie them to a window AND tie them to a method
cv2.setMouseCallback("my_drawing", draw_rectangle)

while True:

    cv2.imshow("my_drawing", img)

    # close window if ESC key pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows