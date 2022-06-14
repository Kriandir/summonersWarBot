import pyautogui
from time import sleep, time
import os
import json

import pytesseract
import numpy as np
import cv2 as cv
# from matplotlib import pyplot as plt
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def getText(filename,h):
    img = np.array(pyautogui.screenshot(region=h))
    s = (pytesseract.image_to_string(img))

    filename = 'testScreenshot.png'
    filename2 = 'showbounded.png'
    script_dir = os.path.dirname(__file__)

    needle_path = os.path.join(
        script_dir,
        'screenshots',
        filename
    )
    needle_path2= os.path.join(
        script_dir,
        'screenshots',
        filename2
    )
    print(needle_path)
    image = (pyautogui.screenshot(needle_path))
    pyautogui.screenshot(needle_path2,region=h)
    print(image)
    if 'excluding' in s:
        print(s)

def getBounds(filename,h):
    script_dir = os.path.dirname(__file__)
    filename+='.png'
    needle_path = os.path.join(
        script_dir,
        'screenshots',
        filename
    )
    pyautogui.screenshot(needle_path, region=h)

def getLocationsCaptcha():
    images_to_check = [
        "sw_quiz.PNG",
        "sw_quiz2.PNG"
    ]
    # loop over images until one is found, then return the index of the found
    for index, image_filename in enumerate(images_to_check):
        script_dir = os.path.dirname(__file__)
        print(__file__)

        needle_path = os.path.join(
            script_dir,
            'needles',
            image_filename
        )
        print(needle_path)
        image_pos = pyautogui.locateOnScreen(needle_path, grayscale="False", confidence=0.7)
        if image_pos:
            print("imageFound: {} at pos: {}".format(image_filename, image_pos))
            print(image_pos)
            center = pyautogui.center(image_pos)
            # pyautogui.click(center.x, center.y)
            sleep(np.abs(np.random.randn(1)[0]))
            x = image_pos[0]
            y = image_pos[1]
            x -= 220
            y += 190
            # actual try
            x -= 15
            y +=15
            h = (x, y, 130, 120)
            regionList = []
            for i in range(4):
                if i !=0:
                    x += 130
                for j in range(2):
                    if j !=0:
                        y+=110
                    regionList.append((x, y, 125, 120))
                y-=110
            test = 2
            for h in regionList:

                matchImage(h,script_dir)
            testLocations(regionList, script_dir)
            pyautogui.screenshot(needle_path[:-4]+'testimage.png',region=regionList[test])


            return True


    print('image not found')
    return False

def testLocations(regionList,script_dir):
    print(f'RegionList: {len(regionList)}')
    for i in regionList:
        needle_path2 = os.path.join(
            script_dir,
            'screenshots',
            f'location_{i}.png'
        )
        pyautogui.screenshot(needle_path2, region=i)
        # center = pyautogui.center(i)
        # pyautogui.click(center.x, center.y)
        # sleep(0.5)




def matchImage(h,script_dir):
    script_dir = os.path.dirname(__file__)
    monster_dir = os.path.join(script_dir, 'needles', 'bosses', 'grey')
    images_to_check = (os.listdir(monster_dir))

    # loop over images until one is found, then return the index of the found
    for index, image_filename in enumerate(images_to_check):


        needle_path = os.path.join(
            monster_dir,
            image_filename
        )
        image_pos = pyautogui.locateOnScreen(needle_path,region=h,grayscale=True,confidence=0.7)
        if image_pos:
            print("imageFound: {} at pos: {}".format(image_filename, image_pos))
            print(image_pos)
            center = pyautogui.center(image_pos)
            pyautogui.click(center.x, center.y)
            return True
        else:
            print("image not found")



        # img = cv.imread(needle_path,0)
        # # Initiate ORB detector
        # orb = cv.ORB_create()
        # # find the keypoints with ORB
        # kp = orb.detect(img,None)
        # # compute the descriptors with ORB
        # kp, des = orb.compute(img, kp)
        # # draw only keypoints location,not size and orientation
        # img2 = cv.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)
        # cv.imwrite(needle_path[:-4]+'_gray.png',img2)

getLocationsCaptcha()