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


def countdownTimer():
    # Countdown timer
    print("Starting", end="", flush=True)
    for i in range(0, 6):
        print(".", end="", flush=True)
        sleep(1)
    print("Go")




# convert pynput button keys into pyautogui keys
# https://pynput.readthedocs.io/en/latest/_modules/pynput/keyboard/_base.html#Key
# https://pyautogui.readthedocs.io/en/latest/keyboard.html
def convertKey(button):
    PYNPUT_SPECIAL_CASE_MAP = {
        'alt_l': 'altleft',
        'alt_r': 'altright',
        'alt_gr': 'altright',
        'caps_lock': 'capslock',
        'ctrl_l': 'ctrlleft',
        'ctrl_r': 'ctrlright',
        'page_down': 'pagedown',
        'page_up': 'pageup',
        'shift_l': 'shiftleft',
        'shift_r': 'shiftright',
        'num_lock': 'numlock',
        'print_screen': 'printscreen',
        'scroll_lock': 'scrolllock',
    }

    # example: 'Key.F9' should return 'F9', 'w' should return as 'w'
    cleaned_key = button.replace('Key.', '')

    if cleaned_key in PYNPUT_SPECIAL_CASE_MAP:
        return PYNPUT_SPECIAL_CASE_MAP[cleaned_key]

    return cleaned_key

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


# def match_all(image, template, threshold=0.7, debug=False):
#     """ Match all template occurrences which have a higher likelihood than the threshold """
#     width, height = template.shape[:2]
#     match_probability = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
#     match_locations = np.where(match_probability >= threshold)
#
#     # Add the match rectangle to the screen
#     locations = []
#     for x, y in zip(*match_locations[::-1]):
#         locations.append(((x, x + width), (y, y + height)))
#
#         if debug:
#             cv2.rectangle(image, (x, y), (x + width, y + height), color, 1)
#     return locations
# # import imutils
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



def pressKey(key, seconds=4.00):
    """Pressing Key Function"""
    pyautogui.keyDown(key)
    sleep((np.random.randint(2)/10)+0.1)
    pyautogui.keyUp(key)
    sleep(seconds)


# def playActions(filename):
#     # Read the file
#     script_dir = os.path.dirname(__file__)
#     filepath = os.path.join(
#         script_dir,
#         'recordings',
#         filename
#     )
#     with open(filepath, 'r') as jsonfile:
#         # parse the json
#         data = json.load(jsonfile)
#
#         # loop over each action
#         # Because we are not waiting any time before executing the first action, any delay before the initial
#         # action is recorded will not be reflected in the playback.
#         for index, action in enumerate(data):
#             action_start_time = time()
#
#             # look for escape input to exit
#             if action['button'] == 'Key.esc':
#                 break
#             randint = np.random.randint(0, 20)
#             randomchange = np.random.randn(1)[0] * randint
#             # perform the action
#             if action['type'] == 'keyDown':
#                 key = convertKey(action['button'])
#                 pyautogui.keyDown(key)
#                 print("keyDown on {}".format(key))
#             elif action['type'] == 'keyUp':
#                 key = convertKey(action['button'])
#                 pyautogui.keyUp(key)
#                 print("keyUp on {}".format(key))
#             elif action['type'] == 'click':
#                 pyautogui.click(action['pos'][0] + randomchange, action['pos'][1] + randomchange, duration=0.25)
#                 print("click on {}".format(action['pos']))
#
#             # then sleep until next action should occur
#             try:
#                 next_action = data[index + 1]
#             except IndexError:
#                 # this was the last action in the list
#                 break
#             elapsed_time = next_action['time'] - action['time']
#
#             # if elapsed_time is negative, that means our actions are not ordered correctly. throw an error
#             if elapsed_time < 0:
#                 raise Exception('Unexpected action ordering.')
#
#             # adjust elapsed_time to account for our code taking time to run
#             elapsed_time -= (time() - action_start_time)
#             if elapsed_time < 0:
#                 elapsed_time = 0
#             print('sleeping for {}'.format(elapsed_time))
#             sleep(elapsed_time)

# createScreenshot()
# #
# for i in range(0,100):
#     checkPlants()
#     sleep(1)
#     print('yolo')

