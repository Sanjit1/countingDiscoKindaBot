import pyautogui as bot
import time

time.sleep(5)
number = 0
for each in range(4, 40):
    bot.moveTo(555, 175, .3)
    time.sleep(.5)
    bot.click()
    time.sleep(.5)
    bot.moveTo(811, 465, .3)
    time.sleep(.5)
    bot.click()
    time.sleep(.5)
    bot.click()
    for each in range(0, 4):
        bot.moveTo(690, 450, .3)
        time.sleep(.5)
        bot.click()
        time.sleep(.7)
        bot.press(str(number))
        number = number + 1
        time.sleep(.7)
        bot.moveTo(690, 435, .3)
        bot.click()
        time.sleep(.5)
    time.sleep(4)