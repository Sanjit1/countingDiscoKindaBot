listOfEmote = ["OKflex", "weeb", "thenking", "thonk", "thonkmonocole", "thunking", "ban", "tidepod", "thonkscioly", "thonksatan", "thonksalt", "thonkpoop", "thonkmonocle", "thonk", "thinkascension", "thenking", "themadmanOP", "scratchcat","PEPE", "owo", "OOFdab", "oof~1", "OKflex", "dank", "dabMAX", "boba"]
import pyautogui
import time
import math
import random

time.sleep(5)

def perfect_repetition(s):
    chars = "123456789"
    for char in chars:
        count = s.count(char)
        if count==len(s):
            return True
        else: 
            return False

def has69(s):
    return "69" in s

def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    # Calling reverse function 
    rev = reverse(s) 
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False

def isPerfectSquare(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 
  
# Returns true if n is a Fibinacci Number, else false 
def isFibonacci(n): 
  
    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both 
    # is a perferct square 
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) 


def spamNumbers(start, end, spd):
    for each in range(start, end+1):
        string_to_send = str(each)
        if isPerfectSquare(each):
            string_to_send  += " Perfect Square!"
        if isFibonacci(each):
            string_to_send += " Fibonacci!"
        if isPalindrome(str(each)):
            string_to_send += " Palindrome!!"
        if perfect_repetition(str(each)):
            string_to_send += " Perfect Repetition!"
        if has69(str(each)):
            string_to_send += " Nice"
        pyautogui.hotkey('\n')
        pyautogui.typewrite(string_to_send)
        pyautogui.press('enter')
        time.sleep(spd)

class spammable:
    def __init__(self, txt, wat):
        self.text= txt
        self.wait = wat


def spamText(text, numberOfTimes, period):
    for each in range(0, numberOfTimes):
        pyautogui.hotkey('\n')
        pyautogui.typewrite(text)
        pyautogui.press('enter')
        time.sleep(period)

        
def spamList(list, repeats, totalWaitAtLeast):
    for each in range(0, repeats):
        timeLeft = totalWaitAtLeast
        for spamThingie in list:
            totalWaitAtLeast -= spamThingie.wait
            pyautogui.hotkey('\n')
            pyautogui.typewrite(spamThingie.text)
            pyautogui.press('enter')
            time.sleep(spamThingie.wait)
        time.sleep(timeLeft if timeLeft>0 else 0)

def start():
    pyautogui.moveTo(200, None, 2, pyautogui.easeInElastic)
    for each in range(0,100):
        pyautogui.scroll(random.randint(-200, 500))
        pyautogui.scroll(random.randint(-200, 500))
        pyautogui.moveTo(200, random.randint(180, 700), .5, pyautogui.easeInElastic)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.hotkey('\n')
        pyautogui.typewrite(":"+random.choice(listOfEmote)+":")
        pyautogui.press('enter')
        time.sleep(0.1)

start()

# // spamNumbers(1, 2000, 0.1)



# //spamList([spammable("t!tg clean", 5), spammable("t!tg feed", 5), spammable("t!tg play", 5)], 2,21)


# WEED: Syntax: spam(start number, end number, speed(in seconds))
# WEED: configure speed, based on you internet speed, if it is slow, increase the parameter, and test it before you run the bot, so that 
# WEED: discord does not have to tell you to slow down.
# WEED: Also don't mind the WEED its just for VSCode to color my commentsPython script to spam numbers on DiscordPython script to spam numbers on Discord
