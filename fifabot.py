#Author: Juan Francisco Patino juan9patino9@gmail.com
#fifabot.py
#trading bot for FIFA coins

import time
import pyautogui
import random
speed = 0.6 #adjust based on the speed of your browser


#move to the home page and click
def calibrate():
    pyautogui.moveTo(100,250, duration = 3)
    pyautogui.click(pause = speed)
    time.sleep(.5)

#go to the transfer market
def goMarket():
    pyautogui.moveTo(100,430, duration = speed)
    pyautogui.click()
    pyautogui.moveTo(600, 430, duration = speed)
    pyautogui.click()
    #pyautogui.moveTo(600, 480, duration = speed)
    #pyautogui.click()
    #pyautogui.moveTo(600, 600, duration = speed)
    #pyautogui.click()


#search for a player on the tranfer market
def search(player):

    pyautogui.press('tab', presses = 5, interval = speed)
    pyautogui.write(player)
    pyautogui.moveTo(600, 480, duration = speed)
    pyautogui.click(pause = speed)
    pyautogui.click(pause = speed)
    pyautogui.press('tab', presses = 4, interval = speed)
    pyautogui.write('650')
    pyautogui.moveTo(1600, 940, duration = speed)
    pyautogui.click(pause = speed)

def bid(n):
#place a bid
#assume search() has just been called
#assume you have the coins
    
    pyautogui.moveTo(1600, 670, duration = speed)
    pyautogui.click(pause = speed)
    pyautogui.moveTo(1200, 670, duration = speed)
    for x in range(n): #for now you can only bid three on one page
        #right now it's difficult to tell how many players are on a page
        pyautogui.moveTo(1270, 945, duration = speed)#scroll
        pyautogui.click(pause = speed)
        pyautogui.moveTo(1200, random.randint(350, 700), duration = speed)#middle of page
        time.sleep(1)
        pyautogui.press('esc')
        pyautogui.press('esc')
        pyautogui.click(pause = speed)
        pyautogui.click(pause = speed)
        pyautogui.moveTo(1600, 670, duration = speed)#click bid
        pyautogui.click(pause = speed)


def sell(n):
#sell items on transfer list, if any
    for x in range(n):
        pyautogui.moveTo(100,430, duration = speed)#mouse goes to "TRANSFERS"
        pyautogui.click(pause = speed)
        pyautogui.moveTo(600, 660, duration = speed)
        pyautogui.click(pause = speed)
        pyautogui.moveTo(1270, 945, duration = speed)#scroll down
        pyautogui.mouseDown()
        pyautogui.moveTo(550, 630, duration = speed)
        pyautogui.mouseUp()
        pyautogui.moveTo(1600, 620, duration = speed)
        pyautogui.click(pause = speed)
        pyautogui.press('tab', presses = 4, interval = speed)
        pyautogui.write('1000')
        pyautogui.moveTo(1600, 920, duration = speed)
        pyautogui.click(pause = speed)

def sendToTransferList(n):
    #send 'won' items to transfer list, if any    
    pyautogui.moveTo(100,430, duration = speed)#mouse goes to "TRANSFERS"
    pyautogui.click(pause = speed)        
    pyautogui.moveTo(1200, 660, duration = speed)
    pyautogui.click(pause = speed)
    pyautogui.moveTo(1270, 945, duration = speed)#scroll down
    pyautogui.mouseDown()
    pyautogui.moveTo(700, 630, duration = speed)
    pyautogui.mouseUp()
    pyautogui.click(pause = speed)
    pyautogui.moveTo(1600, 770, duration = speed)
    for x in range(n):
        pyautogui.click(pause = speed)
 

    
def main():
    print(pyautogui.size())
    print("assuming screen size is 1920*1080 and you're already on the web app")
    while(True):
        calibrate()
        goMarket()
        search('valencia') #rare gold discard player #nonrare for testing
        bid(8)
        sell(8)
        sendToTransferList(8)
        time.sleep(3700) #wait an hour + 100 seconds to repeat, allow things to sell/expire
main()
