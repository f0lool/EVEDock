import cv2 as cv
from PIL import ImageGrab
from time import sleep
import pyautogui
import numpy as np
import win32gui
from windowcapture import WindowCapture
from vision import Vision
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

wincap = WindowCapture('EVE - f0lool')
needle = Vision('Undock.png')
ProcessCheck = False


if __name__ == '__main__':
    while(True and ProcessCheck == False):
        frame = wincap.get_screenshot()

        points = needle.find(frame, 0.7, 'points')

        if len(points) <= 0:
            sleep(6)
            pyautogui.moveTo(83,121)
            sleep(6)
            pyautogui.click()
            sleep(1)
            pyautogui.moveTo(141,216)
            sleep(1)
            pyautogui.click()
            pyautogui.moveTo(432, 217)
            sleep(1)
            pyautogui.click()
            pyautogui.moveTo(592, 253)
            sleep(1)
            pyautogui.click()
            ProcessCheck = True



        if cv.waitKey(25) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break
