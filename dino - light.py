#!/usr/bin/env python3

import pyautogui
from PIL import Image, ImageGrab
from numpy import asarray 
import PIL.ImageOps  
import time
def hit(key):
    pyautogui.press(key)
    return
def isCollide(data):
   #Draw  the rectangle for cactus
    for i in range(190, 238):
        for j in range(395, 460):  
            if data[i, j] < 100 :       
                hit("up")
                return
     # Draw the rectangle for birds
    for i in range(170, 210):
        for j in range(270, 395):
            if  data[i, j] < 100:
                hit("down")
                return
    return
if __name__ == "__main__":
    # time.sleep(2)
    print("Hey.. Dino game about to start in 3 seconds")
    # hit('up') 
    while True:
        image = ImageGrab.grab().convert('L')
        # inverted_image = PIL.ImageOps.invert(image)
        data =image.load()
        isCollide(data)       
        
        # # #Draw the rectangle for birds
        # for i in range(170, 210):
        #     for j in range(270, 395):
        #         data[i, j] = 82
            
        #     # Draw the rectangle for Catcus
        # for i in range(190, 238):
        #     for j in range(395, 460):   
        #         data[i, j] = 0

        # image.show()
        # break
            
