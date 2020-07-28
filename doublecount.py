import time
import pyautogui as bot

startingNumber = 6389
delay = 1.5
first = 'right'

time.sleep(3)

while True:
    if (first == 'left'):
        bot.moveTo(525, 720)
    else:
        bot.moveTo(1075, 720)
    
    bot.click()
    bot.write(str(startingNumber))
    startingNumber += 1
    bot.press('enter')
    time.sleep(delay)
    if (first == 'left'):
        bot.moveTo(1075, 720)
    else:
        bot.moveTo(525, 720)

    bot.click()
    bot.write(str(startingNumber))
    startingNumber += 1
    bot.press('enter')
    time.sleep(delay)
