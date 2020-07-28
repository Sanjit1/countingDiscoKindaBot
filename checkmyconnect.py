import pyautogui as bot
import pyperclip
import time

def check_if_string_in_file(file_name, string_to_search):
    """ Check if any line in the file contains given string """
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if string_to_search in line:
                return True
    return False



time.sleep(2)

list_of_working = []


for each in range(445, 10000):
    bot.moveTo(450, 50, .2)
    time.sleep(.1)
    bot.click()
    time.sleep(.1)
    bot.hotkey('ctrl', 'a')
    time.sleep(.1)
    bot.press('backspace')
    time.sleep(.1)
    bot.typewrite('poway.instructure.com/courses/'+str(each)+' ')
    time.sleep(.1)
    bot.press('enter')
    time.sleep(.75)
    bot.moveTo(650, 350)
    time.sleep(.1)
    bot.click()
    time.sleep(.1)
    bot.click()
    time.sleep(.1)
    bot.hotkey('ctrl','c')
    time.sleep(.1)
    if(pyperclip.paste()=='Access ' or pyperclip.paste()=='Woops'):
        print('sad')
    else:
        print('happy')
        print('poway.instructure.com/courses/'+str(each)+' ')
        list_of_working.append('poway.instructure.com/courses/'+str(each)+' ')
        if(not check_if_string_in_file('classlist.txt', 'poway.instructure.com/courses/'+str(each)+' ')):
            print('here1')
            with open('classlist.txt', 'a') as file:
                file.write('poway.instructure.com/courses/'+str(each)+' \n')
        else:
            print('here2')
    pyperclip.copy('sadNow')


print(list_of_working)