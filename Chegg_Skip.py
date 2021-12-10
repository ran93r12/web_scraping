import pyautogui 
from pynput import keyboard



def Skip():
    pyautogui.click(549,1040, button='left')
        
    pyautogui.press('up')

    pyautogui.press('tab')

    pyautogui.press('enter')


def Answer():
    pyautogui.click(425,1037)


def Exit():
    pyautogui.click(639,1040)




with keyboard.GlobalHotKeys({
        '1': Answer,
        '2': Skip,
        '3': Exit}) as h:
    h.join()