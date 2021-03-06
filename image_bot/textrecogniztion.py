import pyautogui
from time import sleep, time
import os
import json
import copy
import pytesseract
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def getText(image_pos):

    textx = image_pos[0]
    texty = image_pos[1]
    textx -= 300
    texty += 75
    h = (textx, texty, 800, 100)
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
    image = (pyautogui.screenshot(needle_path))
    pyautogui.screenshot(needle_path2,region=h)
    print(s)
    for index, i in enumerate(s):
        if s[index - 1] == '(':
            numImages = int(i)
            break
    if 'excluding' in s:
        return 'monsters',numImages
    elif 'Ellia' in s:
        return 'ellia',numImages
    else:
        return 'bosses',numImages

def getRegions(image_pos):

    x = image_pos[0]
    y = image_pos[1]
    x -= 220
    y += 185
    adjustx = 0
    adjusty = 0

    # actual try
    #
    x -= 20
    y += 25
    adjustx = 15
    adjusty = 20

    regionDict = {}
    for i in range(4):
        if i != 0:
            x += 130
            x += adjustx
        for j in range(2):
            if j != 0:
                y += 110
                y += adjusty
            regionDict[(x, y, 130, 125)] = None
        y -= 110
        y -= adjusty
    return regionDict

def removeEntriesUntilTotal(numImages,matches,monsters=False):

    if not monsters:
        while len(matches) > numImages :
            max = 0
            for index, i in enumerate(matches):
                if max < i[0]:
                    max = i[0]
                    maxIndex = index

            print(matches.pop(maxIndex)[-1])

    else:
        while len(matches) > numImages :
            min = 1000
            for index, i in enumerate(matches):
                if min > i[0]:
                    min = i[0]
                    minIndex = index

            print(matches.pop(minIndex)[-1])
    return matches

def cleanList(listToClean):
    indexList = []
    eleList=[]
    for index,ele in enumerate(listToClean):
        if ele[-1] not in eleList:
            eleList.append(ele[-1])
        else:
            indexList.append(index)

    return [i for j, i in enumerate(listToClean) if j not in indexList]

def createScreenshot(screenname='testScreenShot'):
    filename=f'{screenname}.png'
    script_dir = os.path.dirname(__file__)

    needle_path = os.path.join(
        script_dir,
        'screenshots',
        filename
    )
    print(needle_path)
    image = pyautogui.screenshot(needle_path)
    print(image)


def getLocationsCaptcha(screenname='testScreenShot'):
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
            createScreenshot(screenname)
            print("imageFound: {} at pos: {}".format(image_filename, image_pos))
            print(image_pos)

            # Get regions and text
            regionDict = getRegions(image_pos)
            directory,numImages = getText(image_pos)

            # Check Region Locations (make images of the locations and store in Dict)
            regionDict = storeLocations(regionDict, script_dir)
            # directory = 'monsters'
            matchList = []

            if directory =='monsters':
                numImages = 8 -numImages
                print(numImages)
                directoryList = ['ellia','Bosses']
                matchMaster = []
                for i in directoryList:
                    matchList = []
                    for k, v in regionDict.items():
                        matchList.append(matchOrb(k,v,i))
                    matches = list(filter(None, matchList))

                    matchMaster +=matches

                print('before cleaning')
                print([i[-1] for i in matchMaster])
                print(len(matchMaster))
                matchMaster = cleanList(matchMaster)
                print('after cleaning')
                print(len(matchMaster))
                filteredMatches = removeEntriesUntilTotal(numImages, matchMaster,True)
                print('after filtering:')
                print(len(filteredMatches))
                for i in filteredMatches:
                    # f, axarr = plt.subplots(2, 1)
                    # axarr[0].imshow(i[1])
                    # axarr[1].imshow(i[2])
                    # plt.show()
                    regionDict.pop(i[-1])



                print([k for k,v in regionDict.items()])
                print("________________________________")
                print(regionDict)
                for k,v in regionDict.items():
                    # print(k)
                    center = pyautogui.center(k)
                    pyautogui.click(center.x, center.y)




            else:
                # print(directory)
                # print(numImages)
                for k,v in regionDict.items():
                    matchList.append(matchOrb(k,v,directory))
                matches = list(filter(None, matchList))
                # print(len(matches))
                filteredMatches = removeEntriesUntilTotal(numImages,matches)

                for i in filteredMatches:
                    if i:
                        # print(i[0])
                        center = pyautogui.center(i[3])
                        pyautogui.click(center.x, center.y)
                        # f, axarr = plt.subplots(2, 1)
                        # axarr[0].imshow(i[1])
                        # axarr[1].imshow(i[2])
                        # plt.show()


            return True
    print('image not found')
    return False

def storeLocations(regionDict,script_dir):

    """make images of the regions and store them on the computer for later verification"""
    print(f'regionDict: {len(regionDict)}')
    for k,v in regionDict.items():
        needle_path2 = os.path.join(
            script_dir,
            'screenshots',
            f'location_{k}.png'
        )
        img = np.array(pyautogui.screenshot(needle_path2, region=k))
        dim = (133,133)
        # 133 133 seems best for detecting bosses
        resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
        cv.imwrite(f'{needle_path2}', resized)
        grayed = cv.imread(f'{needle_path2}', cv.IMREAD_GRAYSCALE)
        cv.imwrite(f'{needle_path2}', grayed)
        regionDict[k] = needle_path2
    return regionDict


def matchOrb(k,imgLocation,directory):

    """matching script that matches the stored images against the images in the needles"""
    script_dir = os.path.dirname(__file__)
    monster_dir = os.path.join(script_dir, 'needles', directory, 'Grey')
    images_to_check = (os.listdir(monster_dir))
    good = []
    # loop over images until one is found, then return the index of the found
    for index, image_filename in enumerate(images_to_check):

        needle_path = os.path.join(
            monster_dir,
            image_filename
        )

        matched = False
        # read images
        imgToMatch = cv.imread(imgLocation,0)
        img = cv.imread(needle_path,0)

        # Initiate ORB detector
        orb = cv.ORB_create()
        # find the keypoints with ORB
        kp1, des1 = orb.detectAndCompute(img,None)
        kp2, des2= orb.detectAndCompute(imgToMatch, None)
        bf = cv.BFMatcher()
        matches = bf.knnMatch(des1, des2, k=2)

        # Apply ratio test
        for m, n in matches:

            if m.distance < 0.51 * n.distance:
                # img3 = cv.drawMatches(img, kp1, imgToMatch, kp2,matches, None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
                # good.append([m,n,img,imgToMatch,k])
                # matched = True
                # break
                return m.distance/n.distance,img,imgToMatch,k
        if matched:
            return good
            # break
    return False



getLocationsCaptcha()


