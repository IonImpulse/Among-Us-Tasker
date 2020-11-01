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
- Fix Weather Node           DONE
- - Fix Weather Node Switch  DONE
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
- Reboot Wifi                DONE
- Record Temperature         DONE
- Repair Drill               DONE
- Replace Water Jug          DONE
- Run Diagnostics            DONE
- Scan Boarding Pass         DONE
- Sort Samples               DONE
- Stabilize Steering         DONE
- Start Reactor              DONE
- Store Artifacts            DONE
- Submit Scan                AUTO
- Swipe Card                 DONE
- Unlock Manifolds           DONE
- Upload Data                DONE
- - Download Data            DONE
- Water Plants               DONE
- - Get Water Can            DONE
'''

SKELD_TASKS = ["inspect_sample", "fix_wiring", "fuel_engines", "download_data", "empty_garbage", "empty_chute", "chart_course", "calibrate_distributer", "align_engine_output", "clear_asteroids", "clean_o2_filter", "divert_power", "accept_diverted_power", "stabilize_steering", "prime_shields", "submit_scan", "start_reactor", "unlock_manifolds", "swipe_card", "refuel_station", "upload_data"]
MIRA_TASKS = ["assemble_artifact", "buy_beverage", "chart_course", "clean_o2_filter", "clear_asteroids", "divert_power", "accept_diverted_power", "empty_garbage", "enter_id_code", "fix_wiring", "fuel_engines", "measure_weather", "prime_shields", "process_data", "run_diagnostics", "sort_samples", "start_reactor", "submit_scan", "unlock_manifolds", "refuel_station", "water_plants", "upload_data", "get_water_can"]
POLUS_TASKS = ["insert_keys", "fuel_engines", "fix_wiring", "empty_garbage", "fill_canisters", "fix_weather_node", "align_telescope", "chart_course", "clear_asteroids", "replace_water_jug", "record_temperature", "reboot_wifi", "scan_boarding_pass", "repair_drill", "monitor_tree", "inspect_sample", "open_waterways", "submit_scan", "store_artifacts", "start_reactor", "swipe_card", "refuel_station", "unlock_manifolds", "upload_data", "download_data"]

def find_task_key(image_key_list, current_map) :
    task = ("","")
    im = python_imagesearch.imagesearch.region_grabber((400, 90, SCREEN_SIZE[0], SCREEN_SIZE[1]))
    
    for index, key_pair in enumerate(image_key_list) :
        if key_pair[1] in current_map :

            pos = python_imagesearch.imagesearch.imagesearcharea(key_pair[0], 400, 90, 1540, 1000, precision=PRECISION, im=im)
        
            if pos[0] != -1 :
                task = (key_pair[1], pos)

                if DEBUG == True :
                    print(f"Found at {pos}:\n{key_pair[1]}")
                return task
    
    return False

if __name__ == "__main__" :
    TD = TaskerDo(PRECISION, SLOW_MODE, DEBUG)

    keep_going = True
    while keep_going :
        os.system('cls')
        print("=== Loaded and ready! ===")
        print("Which map?")
        print("1: Skeld")
        print("2: Mira")
        print("3: Polus")
        
        choice = input(":")

        keep_going = False

        if choice == "1" :
            current_map = SKELD_TASKS
        elif choice == "2" :
            current_map = MIRA_TASKS
        elif choice == "3" :
            current_map = POLUS_TASKS
        else :
            keep_going = True

    task_list = []

    os.system('cls')

    print("=== Waiting for task activation button... ===")
    
    while True :
        keyboard.wait(ACTIVATION_KEY)
        
        last = time.perf_counter()
        
        task = find_task_key(TD.image_key_list, current_map)

        if task != False :
            
            task_list.append(task[0])

            time_to_find = time.perf_counter() - last

            if task != ("", "") :
                
                if TD.debug :
                    print(task[0])
                    last = time.perf_counter()
                
                TD.switch(task[0])
                
                os.system('cls')

                if TD.debug :
                    print(f"=== Task found in {time_to_find} seconds ===")

                print("Completed:")
                for i in task_list :
                    print(f"- {i}")

                if TD.debug :
                    print(f"Task |{task[0]}| completed in {time.perf_counter() - last} seconds")

                print("Waiting for task activation button...")
                '''try :
                    
                except Exception as e :
                    print(e)'''
        else :
            if TD.debug :
                print(f"Did not find task, taking {time.perf_counter() - last} seconds")
