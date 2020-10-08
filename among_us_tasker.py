import time
import keyboard
from tasker import *
import python_imagesearch.imagesearch
from python_imagesearch.imagesearch import imagesearch

ACTIVATION_KEY = "f"
PRECISION = .8
SLOW_MODE = False
DEBUG = True
SCREEN_SIZE = (1920, 1080)

'''
List of all tasks this program can automate, marked with DONE:
Task that complete on selection are marked AUTO

- Align Engine Output        DONE
- Align Telescope
- Assemble Artifact          DONE
- Buy Beverage               DONE
- Calibrate Distributer      DONE
- Chart Course               DONE
- Clean O2 Filter            DONE
- Clear Asteroids            DONE (may need to activate more then once)
- Divert Power               DONE
- - Accept Diverted Power    DONE
- Empty Chute                DONE
- Empty Garbage              DONE
- Enter ID Code              DONE
- Fill Canisters
- Fix Weather Node
- Fix Wiring                 DONE
- Fuel Engines               DONE
- - Refuel Station           DONE
- Insert Keys                DONE
- Inspect Sample             DONE
- Measure Weather            DONE
- Monitor Tree
- Open Waterways
- Prime Shields              DONE
- Process Data               DONE
- Reboot Wifi
- Record Temperature         DONE
- Repair Drill               DONE
- Replace Water Jug
- Run Diagnostics            DONE
- Scan Boarding Pass         DONE
- Sort Samples               DONE
- Stabilize Steering         DONE
- Start Reactor              DONE
- Store Artifacts
- Submit Scan                AUTO
- Swipe Card                 DONE
- Unlock Manifolds           DONE
- Upload Data                DONE
- - Download Data            DONE
- Water Plants               DONE
- - Get Water Can            DONE
'''



def find_task_key(image_key_list) :
    task = ("","")
    im = python_imagesearch.imagesearch.region_grabber((400, 90, SCREEN_SIZE[0], SCREEN_SIZE[1]))
    
    for index, key_pair in enumerate(image_key_list) :
        pos = python_imagesearch.imagesearch.imagesearcharea(key_pair[0], 400, 90, 1540, 1000, precision=PRECISION, im=im)
    
        if pos[0] != -1 :
            task = (key_pair[1], pos)

            if DEBUG == True :
                print(f"Found at {pos}:\n{key_pair[1]}")
            return task
    
    return False

if __name__ == "__main__" :
    TD = TaskerDo(PRECISION, SLOW_MODE, DEBUG)

    print("Loaded and ready!")

    while True :
        keyboard.wait(ACTIVATION_KEY)
        
        last = time.perf_counter()
        
        task = find_task_key(TD.image_key_list)

        if task != False :
            if TD.debug :
                print(f"Task found in {time.perf_counter() - last} seconds")

            if task != ("", "") :
                
                if TD.debug :
                    print(task[0])
                    last = time.perf_counter()
                
                TD.switch(task[0])
                
                if TD.debug :
                    print(f"Task |{task[0]}| completed in {time.perf_counter() - last} seconds")

                '''try :
                    
                except Exception as e :
                    print(e)'''
        else :
            if TD.debug :
                print(f"Did not find task, taking {time.perf_counter() - last} seconds")
