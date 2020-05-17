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
    for i in range(158, 275):
        for j in range(420, 450):
            if data[i, j] <= 84 :       
                hit("up")
                return
     # Draw the rectangle for birds
    for i in range(165, 200):
        for j in range(305, 399):
            if  data[i, j] <= 84:
                hit("down")
                return
    return
if __name__ == "__main__":
    time.sleep(2)
    print("Hey.. Dino game about to start in 3 seconds")
    # hit('up') 
    while True:
        image = ImageGrab.grab().convert('L')
        inverted_image = PIL.ImageOps.invert(image)
        data = inverted_image.load()
        isCollide(data)       
        
        # #     # Draw the rectangle for birds
        # for i in range(170, 200):
        #     for j in range(305, 395):
        #         data[i, j] = 0
            
        #     # Draw the rectangle for Catcus
        # for i in range(158, 275):
        #     for j in range(420, 450):   
        #         data[i, j] = 82

        # inverted_image.show()
        # break
            
