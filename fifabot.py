#Author: Juan Francisco Patino juan9patino9@gmail.com
#fifabot.py
#trading bot for FIFA coins

import time
import pyautogui
import random
speed = 0.6 #adjust based on the speed of your browser


#move to the home page and click
def calibrate():
    print("Recalibrating...")
    pyautogui.moveTo(100,250, duration = 3)
    pyautogui.click(pause = speed)
    time.sleep(2)

#go to the transfer market
def goMarket():
    print("Heading over to the market...")
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
    print("Searching for, ", player)
    pyautogui.press('tab', presses = 5, interval = speed)
    pyautogui.write(player)
    pyautogui.moveTo(600, 480, duration = speed)
    pyautogui.click(pause = speed)
    pyautogui.click(pause = speed)
    pyautogui.press('tab', presses = 3, interval = speed)
    time.sleep(1)
    pyautogui.write('650')
    pyautogui.moveTo(1600, 940, duration = speed)
    pyautogui.click(pause = speed)

def bid(n):
#place a bid
#assume search() has just been called
#assume you have the coins
    print("Placing a bid for ", n, "players")    
    #pyautogui.moveTo(1600, 670, duration = speed)
    #pyautogui.click(pause = speed)
    #pyautogui.moveTo(1200, 670, duration = speed)
    playerOnPage = 330
    topOfPage = True
    for x in range(n): #for now you can only bid three on one page
        pyautogui.moveTo(1200, playerOnPage, duration = speed)#middle of page
        time.sleep(1)
        pyautogui.click(pause = speed)
        pyautogui.moveTo(1600, 670, duration = speed)#click bid
        pyautogui.click(pause = speed)
        pyautogui.press('esc')  #incase of double bid
        playerOnPage = playerOnPage + 120
        if playerOnPage > 800:
            playerOnPage = 330
            if topOfPage == True:
                pyautogui.moveTo(1270, 910, duration = speed)#scroll
                topOfPage = False
            else:
                pyautogui.moveTo(1270, 910, duration = speed)#hit next page button
                topOfPage = True

    
#    for x in range(n): #for now you can only bid three on one page
#        #right now it's difficult to tell how many players are on a page
#        pyautogui.press('esc')
#        pyautogui.moveTo(1270, 945, duration = speed)#scroll
#        pyautogui.click(pause = speed)
 #       pyautogui.moveTo(1200, random.randint(350, 700), duration = speed)#middle of page
  #      time.sleep(1)
   #     pyautogui.press('esc')
    #    pyautogui.press('esc')
     #   pyautogui.click(pause = speed)
      #  pyautogui.click(pause = speed)
       # pyautogui.moveTo(1600, 670, duration = speed)#click bid
        #pyautogui.click(pause = speed)
        #pyautogui.press('esc')

    
   

def sell(n):
#sell items on transfer list, if any
    print("Selling players for 1000 coins")
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
    print("Sending won items to transfer list")
    pyautogui.moveTo(100,430, duration = speed)#mouse goes to "TRANSFERS"
    pyautogui.click(pause = speed)        
    pyautogui.moveTo(1200, 660, duration = speed)
    pyautogui.click(pause = speed)
    pyautogui.moveTo(1270, 945, duration = speed)#scroll down
    pyautogui.mouseDown()
    pyautogui.moveTo(700, 630, duration = speed)
    pyautogui.mouseUp()
    pyautogui.click(pause = speed)
    pyautogui.moveTo(1270, 870, duration = speed)#scroll
    for x in range(5):
        pyautogui.click(pause = speed)
        time.sleep(.1)
    pyautogui.moveTo(1200, 330, duration = speed)
    pyautogui.click()
    pyautogui.moveTo(1600, 750, duration = speed)
    pyautogui.click(pause = speed)

    for x in range(n):
        pyautogui.click(pause = speed)
    pyautogui.moveTo(1270, 995, duration = speed)#scroll
 
def test():
    #pyautogui.moveTo(1200,770, duration = speed)
    pyautogui.moveTo(1600, 750, duration = speed)
    #sendToTransferList(20)
    
def main():
    print(pyautogui.size())
    print("assuming screen size is 1920*1080 and you're already on the web app")
    while(True):
        calibrate()
        goMarket()
        rando = random.randint(1, 4)
        player = 'valencia'
        if rando == 1:
            player = 'valencia'
        elif rando == 2:
            player = 'deeney'
        elif rando == 3:
            player = 'calvert'
        else:
            player = 'gray'
        search(player) #rare gold discard player #nonrare for testing
        bid(8)
        for x in range(6):
            sendToTransferList(20)
            sell(20)
            time.sleep(600)
               
main()
#test()
