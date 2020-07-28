import pyautogui as bot
import time

time.sleep(5)
bot.keyDown('p')
time.sleep(.05)
bot.keyUp('p')
bot.keyDown('q')
time.sleep(.25)
bot.keyUp('q')

for each in range(0,1):
    bot.keyDown('p')
    time.sleep(.05)
    bot.keyUp('p')
    bot.keyDown('w')
    time.sleep(.12)
    bot.keyUp('w')                