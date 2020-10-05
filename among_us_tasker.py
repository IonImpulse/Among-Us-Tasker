from pyautogui import *
from pyautogui import press, typewrite, hotkey
import random
import time
import pydirectinput
from python_imagesearch.imagesearch import imagesearch

SCREEN_SIZE = (1920, 1080)
ACTIVATION_KEY = "f"

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
- Divert Power
- Empty Chute
- Empty Garbage
- Enter ID Code
- Fill Canisters
- Fix Weather Node
- Fix Wiring
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
- Start Reactor
- Store Artifacts
- Submit Scan
- Swipe Card
- Unlock Manifolds
- Upload Data
- Water Plants



'''

def do_wiring() :
