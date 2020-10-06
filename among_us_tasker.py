import pyautogui
import random
import time
import pydirectinput
import os
import keyboard
from tasker import *
from python_imagesearch.imagesearch import imagesearch

ACTIVATION_KEY = "f"
PRECISION = .8
SLOW_MODE = False
DEBUG = True


'''
List of all tasks this program can automate, marked with DONE:

- Align Engine Output
- Align Telescope
- Assemble Artifact
- Buy Beverage
- Calibrate Distributer
- Chart Course
- Clean O2 Filter
- Clear Asteroids
- Divert Power               DONE
- - Accept Diverted Power    DONE
- Empty Chute
- Empty Garbage
- Enter ID Code
- Fill Canisters
- Fix Weather Node
- Fix Wiring                 DONE
- Fuel Engines
- Insert Keys
- Inspect Sample
- Measure Weather
- Monitor Tree
- Open Waterways
- Prime Shields
- Process Data
- Reboot Wifi
- Record Temperature
- Repair Drill
- Replace Water Jug
- Run Diagnostics
- Scan Boarding Pass
- Sort Samples
- Stabilize Steering
- Start Reactor              DONE
- Store Artifacts
- Submit Scan
- Swipe Card                 DONE (slow)
- Unlock Manifolds           DONE
- Upload Data                DONE
- - Download Data            DONE
- Water Plants
'''



def find_task_key(image_key_list) :
    found = False
    task = ("","")

    for key in image_key_list :
        pos = imagesearch(key, precision=PRECISION)
        if pos[0] != -1 :
            found = True
            task = (key, pos)

            if DEBUG == True :
                print(f"Found at {pos}:\n{key}")
    
    return task

if __name__ == "__main__" :
    TD = TaskerDo(PRECISION, SLOW_MODE, DEBUG)

    print("Loaded and ready!")

    while True :
        keyboard.wait(ACTIVATION_KEY)
        task = find_task_key(TD.image_key_list)

        if task != ("", "") :
            task_to_do_name = task[0][:-8][::-1]
            task_to_do_name = task_to_do_name[:task_to_do_name.find("\\",)][::-1]
            
            if TD.debug :
                print(task_to_do_name)
            
            try :
                TD.switch(task_to_do_name)
            except Exception as e :
                print(e)
