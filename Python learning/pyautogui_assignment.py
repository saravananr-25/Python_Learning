import pyautogui
import time
import pyperclip
import pyscreeze    
import PIL
import datetime
from datetime import date

pyautogui.FAILSAFE=True
pyautogui.PAUSE=0.5

print("Lets open the chrome browser...")
time.sleep(0.5)
pyautogui.hotkey('win', 'r')
time.sleep(0.5)
pyautogui.typewrite('chrome\n', interval=0.3)
pyautogui.press('enter')
time.sleep(1)

print("Opening the NSE india website...")
pyautogui.typewrite('https://www.nseindia.com/market-data/top-gainers-losers#gainers\n',interval=0.1)
time.sleep(1)

'''
pyautogui.hotkey('alt','space')
pyautogui.press('x')
'''

print("Copying the data from the website...")

pyautogui.PAUSE=2
pyautogui.moveTo(520,650, duration=0.5)
pyautogui.dragTo(960, 1160, duration=1, button='left')
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)
print("Lets open the excel window..")
time.sleep(0.5)
pyautogui.hotkey('win', 'r')
time.sleep(0.5)
pyautogui.typewrite('excel\n', interval=0.3)
pyautogui.press('enter')
pyautogui.press('enter')
time.sleep(1)

current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S")
pyautogui.write(current_datetime)
pyautogui.press ('enter')
time.sleep(1)

pyautogui.hotkey('ctrl', 'v')
time.sleep(1)



pyautogui.hotkey('ctrl','s')
filename = f"Report_as_on_{current_datetime}.xlsx"
time.sleep(1)
pyautogui.write(filename, interval=0.4)

pyautogui.press('enter')

pyautogui.screenshot("Final-sheet.png")
screenshot_name=f"Final-sheet-{current_datetime}.png"

pyautogui.screenshot(r"C:\Users\SARAVANAN\Gen AI program\daily-report-bot" + "\\" + screenshot_name)
time.sleep(1)
print("All done..")






