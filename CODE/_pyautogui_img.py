import pyautogui

i = pyautogui.locateOnScreen('nbuy.png')
i_center = pyautogui.center(i)
print(i_center)
pyautogui.click(i_center)
