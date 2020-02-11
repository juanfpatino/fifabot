#Author: Juan Francisco Patino juan9patino9@gmail.com
#fifabot.py
#trading bot for FIFA coins

import pyautogui
speed = 0.25 #make it look human?
    
def calibrate():
    #move to top left corner of screen
    pyautogui.moveTo(5,5, duration = speed)

def goMarket():
    #go to the transfer market
    pyautogui.moveTo(100,430, duration = speed)
    pyautogui.click()
    pyautogui.moveTo(600, 430, duration = speed)
    pyautogui.click()
    #pyautogui.moveTo(600, 480, duration = speed)
    #pyautogui.click()
    #pyautogui.moveTo(600, 600, duration = speed)
    #pyautogui.click()

def search(player):
    #begin trading
    pyautogui.press('tab', presses = 5, interval = speed)
    pyautogui.write(player)
    pyautogui.moveTo(600, 480, duration = speed)
    pyautogui.click(pause = speed)
    pyautogui.click(pause = speed)
    pyautogui.press('tab', presses = 5, interval = speed)
    pyautogui.write('650')
    pyautogui.moveTo(1600, 940, duration = speed)
    pyautogui.click(pause = speed)

def bid():
    #assume search() has just been called
    

def main():
    print(pyautogui.size())
    calibrate()
    #assume you're already in the webapp and logged in(https://www.easports.com/fifa/ultimate-team/web-app/)
    goMarket()
    search('valencia')

main()
