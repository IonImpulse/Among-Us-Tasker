import os
import pyautogui
import time
from pyautogui import sleep
from python_imagesearch.imagesearch import imagesearch
from python_imagesearch.imagesearch import imagesearch_loop
from python_imagesearch.imagesearch import imagesearch_region_loop


class TaskerDo :
    def __init__(self, precision, slow_mode, debug) :
        self.main_path = os.path.dirname(os.path.abspath(__file__))
        
        self.precision = precision

        self.slow_mode = slow_mode

        self.debug = debug

        self.image_key_list = self.get_keys(self.main_path)

        return

    def get_keys(self, main_path) :
        image_key_list = []

        for path in os.listdir(main_path + "\\task_images") :
            image_key_list.append(main_path + "\\task_images\\" + path + "\\key.jpg")

        if self.debug :
            print(f"Loaded {len(image_key_list)} image keys")

        return image_key_list

    def switch(self, name):
        default = f"Error on {name}"
        return getattr(self, 'do_' + str(name), lambda: default)()
    
    def do_fix_wiring(self) :
        wires = ["blue", "red", "purple", "yellow"]

        for wire_pair in wires :
            tries = 0
            complete = False

            while tries < 5 and complete == False : 
                pos_left = imagesearch(self.main_path + "\\task_images\\fix_wiring\\left_" + wire_pair + ".jpg", precision=.8)
                pos_right = imagesearch(self.main_path + "\\task_images\\fix_wiring\\right_" + wire_pair + ".jpg", precision=.8)

                if pos_left[0] != -1 and pos_right[0] != -1 :
                    complete = True
                
                tries += 1
            
            if self.debug :
                print(pos_left, pos_right)

            pyautogui.moveTo(pos_left[0] + 10, pos_left[1] + 70)
            pyautogui.mouseDown()
            pyautogui.moveTo(pos_right[0] - 20, pos_right[1] + 70, .01)
            pyautogui.mouseUp()
            pyautogui.click()
    
    def do_start_reactor(self) :
        ''' keypad is:
        1 2 3
        4 5 6
        7 8 9
        '''
        
        pyautogui.press("esc")
        time.sleep(.5)
        pyautogui.press("space")

        button_coords = [(1130,470), (1250, 470), (1390, 470), (1130, 600), (1250, 600), (1390, 600), (1130, 725), (1250, 725), (1390, 725)]
        
        for i in range(6) :
            move_list = []
            for j in range(i) :
                print(i,j)
                
                pos = imagesearch_region_loop(self.main_path + "\\task_images\\start_reactor\\blue.jpg", 0, 470, 410, 840, 780)
                print(pos)

                if pos[0] != -1 :
                    if pos[0] > 0 and pos[0] < 40 :
                        if pos[1] > 0 and pos[1] < 40 :
                            move_list.append(1)
                        elif pos[1] > 100 and pos[1] < 140 :
                            move_list.append(4)
                        else :
                            move_list.append(7)
                    
                    elif pos[0] > 120 and pos[0] < 160 :
                        if pos[1] > 0 and pos[1] < 40 :
                            move_list.append(2)
                        elif pos[1] > 100 and pos[1] < 140 :
                            move_list.append(5)
                        else :
                            move_list.append(8)

                    else :
                        if pos[1] > 0 and pos[1] < 40 :
                            move_list.append(3)
                        elif pos[1] > 100 and pos[1] < 140 :
                            move_list.append(6)
                        else :
                            move_list.append(9)
                if self.debug :
                    print(move_list)
                
                sleep(.3)

            for j in range(i) :
                sleep(.1)
                pyautogui.click(x=button_coords[move_list[j] - 1][0], y=button_coords[move_list[j] - 1][1])

    def do_divert_power(self) :
        pos = imagesearch_region_loop(self.main_path + "\\task_images\\divert_power\\to_divert.jpg", 0, 560, 745, 1352, 830)
        
        if self.debug :
            print(pos)

        pyautogui.moveTo(pos[0] + 10 + 560, pos[1] + 20 + 745)
        pyautogui.mouseDown()
        pyautogui.moveTo(pos[0] + 20 + 560, pos[1] - 200 + 745, .01)
        pyautogui.mouseUp()
    
    def do_accept_diverted_power(self) :
        pos = imagesearch_loop(self.main_path + "\\task_images\\accept_diverted_power\\key.jpg", 0)

        pyautogui.click(x=pos[0] + 10, y=pos[1] + 40)