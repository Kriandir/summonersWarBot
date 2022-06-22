from playback import initializePyAutoGUI,checkRunEnd,checkRefill,clickImage
from textrecogniztion import getLocationsCaptcha
from time import sleep
import numpy as np
import pyautogui
import os

def soldCheck(sold):

    sold = clickImage(['sw_yes.png'], confidence=0.85)
    if sold:
        sleep(np.random.rand(1)[0] * 2)
        return sold

    clickImage(['sw_ok.png'])
    sleep(np.random.rand(1)[0])
    sold = clickImage(['sw_cancel.png'])
    sleep(np.random.rand(1)[0] * 2)
    return sold


def main():
    
    initializePyAutoGUI()
    # countdownTimer()
    # get screen sizewt

    # This trade loop begins by docking at Loki Station
    LOOP_REPITITIONS = 5500
    for i in range(0, LOOP_REPITITIONS):
        sold = False
        sellRunes= False

        repeatEnd = checkRunEnd()

        if repeatEnd:
            if not sellRunes:
                sold = True
            else:
                clickImage(['sw_sellsellected.png'])
                sleep(np.random.rand(1)[0] *2)
                for i in range(1,2):
                    clickImage(['sw_sellsellected2.png'])
                sleep(np.random.rand(1)[0] *2)
                sold = clickImage(['sw_yes.png'],confidence=0.85)
                sleep(np.random.rand(1)[0]*1.5)
                clickImage(['sw_yes.png'], confidence=0.85)

                if not sold:
                    sold = soldCheck(sold)


        #TODO CATCH 6STAR

        if sold:
            for i in range(0,3):
                sleep(np.random.rand(1)[0] *2.5)
                clickState = clickImage(['sw_replay.png'])
                if clickState:
                    break

            sleep(np.random.rand(1)[0] * 1.5)
            clickImage(['sw_repeat.png'],confidence=0.8)

        energyRefill = checkRefill()
        if energyRefill:
            clickImage(['sw_shop.png'])
            sleep(np.random.rand(1)[0] * 2)
            clickImage(['sw_190recharge.PNG'])
            sleep(np.random.rand(1)[0] * 2.5)

            # catchBotException
            quiz = getLocationsCaptcha()
            print(quiz)
            if quiz:

                clickImage(['sw_ok2.png'], confidence=0.8)
            sleep(np.random.rand(1)[0] * 2.5)
            print('Are we out?')

            # TODO this one probably not necessary pay close attention next captcha
            clickImage(['sw_ok.png'],confidence=0.8)
            #

            sleep(np.random.rand(1)[0] * 1.5)
            clickImage(['sw_yes2.png'], confidence=0.8)
            sleep(np.random.rand(1)[0] * 2.5)
            clickImage(['sw_ok.png'], confidence=0.8)
            sleep(np.random.rand(1)[0] * 2.5)
            clickImage(['sw_close.png'])
            sleep(np.random.rand(1)[0] * 1.5)
            clickImage(['sw_repeat.png'])



        print("sleeping for 10 sec")
        sleep(10)
        # Completed loop
        print("Completed loop")

    print("Done")






if __name__ == "__main__":
    main()
