import pyautogui
import time
import math

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


def spam(start, end, spd):
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

spam(1, 2000, 0.1)
# WEED: Syntax: spam(start number, end number, speed(in seconds))
# WEED: configure speed, based on you internet speed, if it is slow, increase the parameter, and test it before you run the bot, so that 
# WEED: discord does not have to tell you to slow down.
# WEED: Also don't mind the WEED its just for VSCode to color my commentsPython script to spam numbers on DiscordPython script to spam numbers on Discord
