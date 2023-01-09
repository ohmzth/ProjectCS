# importing the required packages
from importlib.resources import path
from statistics import mode
import torch
from PIL import Image,ImageTk
import pyautogui as pg
import cv2
import numpy as np
import selectinwindow
import sys
from time import time
sys.setrecursionlimit(10 ** 9)


    def class_to_label(self, x):
        return self.classes[int(x)]

    def plot_boxes(self, results, frame):
        labels, cord = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        for i in range(n):
            row = cord[i]
            if row[4] >= 0.2:
                x1, y1, x2, y2 = int(row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)
                bgr = (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                cv2.putText(frame, self.class_to_label(labels[i]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)

        return frame
    def __call__(self):
        # Initialize the  drag object# 
        wName = "Live"

        resolution = (1920, 1080)

        fps = 60.0 
        # Create an Empty window
        cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
        # Resize this window
        #cv2.resizeWindow("Live", 2000, 800)
        img = pg.screenshot()
        # Convert the screenshot to a numpy array
        frame = np.array(img)
         # Convert it from BGR(Blue, Green, Red) to
         # RGB(Red, Green, Blue)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rectI = selectinwindow.DragRectangle(frame, wName, resolution[0], resolution[1])
        cv2.namedWindow(rectI.wname)
        cv2.setMouseCallback(rectI.wname, selectinwindow.dragrect, rectI)

        # keep looping until rectangle finalized
        while True:
            # display the image
            cv2.imshow(wName, rectI.image)
            key = cv2.waitKey(1) & 0xFF
            # if return flag is True, break from the loop
            if rectI.returnflag:
                break

        #print("Dragged rectangle coordinates")
        print(str(rectI.outRect.x) + ',' + str(rectI.outRect.y) + ',' + \
              str(rectI.outRect.w) + ',' + str(rectI.outRect.h))

        # close all open windows
        cv2.destroyAllWindows()

        cv2.namedWindow("LiveCap")
        cv2.resizeWindow("LiveCap", rectI.outRect.w, rectI.outRect.h)
        while True:
            img = pg.screenshot(region=(rectI.outRect.x,rectI.outRect.y,rectI.outRect.w,rectI.outRect.h));
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            #out.write(frame)
            cv2.imshow('LiveCap', frame)
            if cv2.waitKey(1) == ord('q'):
                break

    
detector = detection(capture_index=0,model_name='best.pt')
detector()
cv2.destroyAllWindows()

