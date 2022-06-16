import pyautogui
from time import sleep, time
import os
import json
import numpy as np
import glob
import cv2
# from skimage import color
from PIL import Image

def initializePyAutoGUI():
    # Initialized PyAutoGUI
    # https://pyautogui.readthedocs.io/en/latest/introduction.html
    # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
    pyautogui.FAILSAFE = True

def createScreenshot():
    filename='testScreenshot.png'
    script_dir = os.path.dirname(__file__)

    needle_path = os.path.join(
        script_dir,
        'screenshots',
        filename
    )
    print(needle_path)
    image = pyautogui.screenshot(needle_path)
    print(image)

def clickImage(images_to_check,confidence =0.9):
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
        image_pos = pyautogui.locateOnScreen(needle_path, grayscale="False", confidence=confidence)
        if image_pos:
            print("imageFound: {} at pos: {}".format(image_filename, image_pos))
            print(image_pos)
            center = pyautogui.center(image_pos)
            width, height = pyautogui.size()
            pyautogui.click(center.x, center.y)
            sleep(np.abs(np.random.randn(1)[0]))
            return True

    print('image not found')
    return False

def checkRunEnd():
    images_to_check = [
        "sw_Repeatbattleend.PNG"
    ]
    # loop over images until one is found, then return the index of the found
    # image
    for index, image_filename in enumerate(images_to_check):
        script_dir = os.path.dirname(__file__)
        # print(__file__)

        needle_path = os.path.join(
        script_dir,
        'needles',
        image_filename
        )
        # print(needle_path)
        image_pos = pyautogui.locateOnScreen(needle_path, grayscale="False", confidence=0.8)
        # createScreenshot()
        if image_pos:
            # print("imageFound: {} at pos: {}".format(image_filename, image_pos))
            # print(image_pos)
            return True


    # print('image not found')
    return False

def checkOk():
    images_to_check = [
        "sw_ok.PNG"
    ]
    # loop over images until one is found, then return the index of the found
    for index, image_filename in enumerate(images_to_check):
        script_dir = os.path.dirname(__file__)
        # print(__file__)

        needle_path = os.path.join(
            script_dir,
            'needles',
            image_filename
        )
        # print(needle_path)
        image_pos = pyautogui.locateOnScreen(needle_path, grayscale="False", confidence=0.9)
        # createScreenshot()
        if image_pos:
            # print("ok found: {} at pos: {}".format(image_filename, image_pos))
            # print(image_pos)
            center = pyautogui.center(image_pos)
            width, height = pyautogui.size()

            pyautogui.click(center.x, center.y)
            sleep(np.abs(np.random.randn(1)[0]))

    print('ok not found')


def checkSell():
    images_to_check = [
        "sw_yes.PNG",
        "sw_cancel.PNG"
    ]
    # loop over images until one is found, then return the index of the found
    for index, image_filename in enumerate(images_to_check):
        script_dir = os.path.dirname(__file__)
        # print(__file__)

        needle_path = os.path.join(
            script_dir,
            'needles',
            image_filename
        )
        # print(needle_path)
        image_pos = pyautogui.locateOnScreen(needle_path, grayscale="False", confidence=0.9)
        # createScreenshot()
        if image_pos:
            # print("imageFound: {} at pos: {}".format(image_filename, image_pos))
            # print(image_pos)
            center = pyautogui.center(image_pos)
            width, height = pyautogui.size()

            pyautogui.click(center.x, center.y)
            sleep(np.abs(np.random.randn(1)[0]))
            return True


    # print('image not found')
    return False

def checkRefill():
    images_to_check = [
        "sw_notenoughenergy.PNG"

    ]
    # loop over images until one is found, then return the index of the found
    for index, image_filename in enumerate(images_to_check):
        script_dir = os.path.dirname(__file__)
        # print(__file__)

        needle_path = os.path.join(
            script_dir,
            'needles',
            image_filename
        )
        # print(needle_path)
        image_pos = pyautogui.locateOnScreen(needle_path, grayscale="False", confidence=0.9)
        # createScreenshot()
        if image_pos:
            # print("imageFound: {} at pos: {}".format(image_filename, image_pos))
            # print(image_pos)
            return True

    # print('image not found')
    return False

def checkPurchase():
    images_to_check = [
        "sw_purchasesucces.PNG"

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
        # print(needle_path)
        image_pos = pyautogui.locateOnScreen(needle_path, grayscale="False", confidence=0.9)
        # createScreenshot()
        if image_pos:
            # print("imageFound: {} at pos: {}".format(image_filename, image_pos))
            # print(image_pos)
            return True

    # print('image not found')
    return False

def findMonster():
    script_dir = os.path.dirname(__file__)
    monster_dir = os.path.join(script_dir,'needles','bosses','grey')
    images_to_check = (os.listdir(monster_dir))
    print(monster_dir)
    # images_to_check = [
        # "sw_assassin.PNG",
        # "sw_drago.PNG",
        # "sw_drunk.PNG"
    # ]
    # loop over images until one is found, then return the index of the found
    for index, image_filename in enumerate(images_to_check):

        needle_path = os.path.join(
            monster_dir,
            image_filename
        )
        # print(needle_path)
        h = (750, 550, 1000, 500)
        image_pos = pyautogui.locateOnScreen(needle_path, grayscale="True", confidence=0.75)
        # createScreenshot()
        if image_pos:
            print(__file__)
            print("imageFound: {} at pos: {}".format(image_filename, image_pos))
            print(image_pos)
            center = pyautogui.center(image_pos)
            width, height = pyautogui.size()

            pyautogui.click(center.x, center.y)
            # sleep(np.abs(np.random.randn(1)[0]))


    print('image not found')
    return False
# createScreenshot()
# findMonster()

def grayOutImg():
    script_dir = os.path.dirname(__file__)
    monster_dir = os.path.join(script_dir,'needles','bosses')
    images_to_check = (os.listdir(monster_dir))
    clicklist = []

    for index, image_filename in enumerate(images_to_check):
        if 'Grey' in image_filename:
            continue
        needle_path = os.path.join(
            monster_dir,
            image_filename
        )
    #     tempimg = cv2.imread(needle_path)
        img = Image.open(needle_path)
        print(needle_path)
        tempimg = img.convert('L')
        cv2.imwrite(needle_path[:-4]+'_gray.png',np.array(tempimg))

# grayOutImg()

