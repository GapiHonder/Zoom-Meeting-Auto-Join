import pyautogui
import time

# Meeting ID
meet_id = '900900900'
password = '1223'

# Esc key to ensure that the Win key will open up correctly in the next step
pyautogui.press('esc', interval=0.1)
time.sleep(0.2)

# Simulating starting up Zoom by pressing Win key, typing "zoom" to open the program
pyautogui.press('win', interval=0.1)
pyautogui.write('zoom')
pyautogui.press('enter', interval=0.5)

# Time delay to account for Zoom app to load up (adjust as needed)
time.sleep(30)

# Simulating clicking the "Join Meeting" button and entering the meeting ID
join_button_coords = pyautogui.locateCenterOnScreen('joinButtonB.PNG')
if join_button_coords is None:
    join_button_coords = pyautogui.locateCenterOnScreen('joinButtonW.PNG')

if join_button_coords is not None:
    x, y = join_button_coords
    pyautogui.click(x, y)

pyautogui.press('enter', interval=1)
pyautogui.write(meet_id)
pyautogui.press('enter', interval=1)

# Time delay to account for Zoom to log into the meeting (adjust as needed)
time.sleep(30)

pyautogui.write(password)
pyautogui.press('enter', interval=1)

# Time delay to account for Zoom to connect to the meeting (adjust as needed)
time.sleep(15)

allow_button_coords = pyautogui.locateCenterOnScreen('Allow.PNG')
if allow_button_coords is not None:
    x, y = allow_button_coords
    pyautogui.click(x, y)

# Waiting time before closing the meeting (2 hours and 20 minutes)
time_to_wait = 2 * 60 * 60 + 20 * 60  # 2 hours and 20 minutes
time.sleep(time_to_wait)

# Closing Zoom
time.sleep(5)  # Allow time for joining the meeting
pyautogui.hotkey('alt', 'f4')
time.sleep(0.5)
pyautogui.hotkey('alt', 'f4')
