# Zoom-Meeting-and-Recording
The python scripts lets you join and record a zoom meeting automatically (this is my first project, any feedback and help is appreciated)

  # Edit: 
   - I deleted from the script the option to record the meeting.
   - I added a function that allow the host to controll your Microphone if it's asked.
   - The programm auto close the zoom session after 2h 20m. You can delete this function by erasing line 47-49.
   - The programm take a bit more time to run completly because i added some waiting time between some tasks.
   - The programm can now detect "Join" button in Light and Dark theme.
   - It is the first time i do Python, there can be some mistakes.
   - The script doesn't lunch automatically, you have to make it automatic by your own (Ex: Put the compilled script in the "startup" folder of Windows)
   - Fork of "BigchillRK/Zoom-Meeting-and-Recording" Thank You for the original script !

Read Me for Zoom Recording Template
					

Please read through this to understand how the code works so that you can implement system properly. This is my first-time coding something like this with my very limited CS background, I understand that my method may be very inefficient and there are probably much easier ways to implement this. All feedback is welcome and appreciated. Thank you for helping me learn.

Requirements

•	Python (Obviously)

•	Changing settings on Zoom

•	Sleep Settings

•	Pyautogui Library

Sleep Settings

Warning!!!

Your computer needs to be AWAKE and SIGNED IN for this method to work. If your computer is normally on, then this won’t be a problem.

Sign In Settings


For this program to work (you will see why as I explain the script itself) your computer needs to be in the desktop directly after waking and must skip the sign in splash screen. To do this, go to start and open up ‘Sign in options’ (just type that in). Find the setting that reads “Require sign-in”, underneath which says, “if you’ve been away, when should Windows require you to sign in again?” and change the setting to “never”. 

Zoom Settings

There’s some zoom settings you must alter so that the script runs smoothly, mainly settings that automatically join you into the call without clicking join with audio. You can also ensure settings to see that you join with your mic and camera muted but that is optional. Check the boxes of the settings I’ve outlined below


General 

•	Enter full screen automatically when starting or joining a meeting 

  o	This is so that screen capture will capture the entire screen properly

Video 

•	Turn off my video when joining meeting

  o	Optional and case specific
  
Audio

•	Automatically join audio by computer when joining a meeting

  o	Very Critical for script to work (NOT OPTIONAL)
  
•	Mute my microphone when joining a meeting

  o	Optional and case specific


Essential Outline

•	Create new task

•	Enter the path to python 

•	Enter the path to the script file itself

•	Enter schedule time as require

REQUIRED

Under the Conditions Tab when creating task, under the Power heading ENSURE YOU CLICK “WAKE THE COMPUTER TO RUN THIS TASK” else the computer will not wake up to run the task and it WILL NOT WORK. For laptops, also check/uncheck settings such as “start the task only if the computer is on AC power” and “stop the computer switches to battery power” as required. 


Python Script

The script uses the PyAutoGUI library to control your keyboard and mouse to emulate how you would normally launch zoom, enter your meeting id and join and record the meeting. Due to this reason, the computer needs to be in the desktop and not behind the sign in screen as the script emulates keystrokes and mouse clicks and this will not work if the pc is in the sign in screen. The code file itself has been documented thoroughly as details required. The documentation for PyAutoGUI is here for you to look at if need be. The code is split into 2 sections: Joining meeting and recording meeting. You may not need both and run which you need and comment the rest. 

https://pyautogui.readthedocs.io/en/latest/index.html
