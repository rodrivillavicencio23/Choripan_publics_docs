import pyautogui
import time

mensaje = pyautogui.prompt(text='Que mensaje deseas spamear?', title='FRAUDE' , default='')
time.sleep(5)
while True:
    time.sleep(0.7)
    pyautogui.typewrite(mensaje)
    pyautogui.press('enter')