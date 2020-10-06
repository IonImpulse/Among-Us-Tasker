import os
from re import match
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
        
        def match_color(rgb) :
            color = ""

            if rgb == (255, 0, 255) :
                color = "purple"
            elif rgb == (255, 235, 4) :
                color = "yellow"
            elif rgb == (0, 0, 255) :
                color = "blue"
            elif rgb == (255, 0, 0) :
                color = "red"
            
            return color

        wires = ["blue", "red", "purple", "yellow"]
        locations = [(555, 1370), (270, 462, 645, 830)]
        im = pyautogui.screenshot()

        left = []
        right = []

        for y in locations[1] :
            
            left_temp = im.getpixel((locations[0][0], y))
            right_temp = im.getpixel((locations[0][1], y))

            left.append(match_color(left_temp))
            right.append(match_color(right_temp))
            
        if self.debug :
            print(left, right)

        for index, color in enumerate(left) :
            
            left_loc = (555, locations[1][index])
            right_loc = (1370, locations[1][right.index(color)])
            
            pyautogui.moveTo(left_loc[0] + 10, left_loc[1] + 20)
            pyautogui.mouseDown()
            pyautogui.moveTo(right_loc[0] - 20, right_loc[1] + 20)
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
        pos = imagesearch_region_loop(self.main_path + "\\task_images\\divert_power\\to_divert.jpg", 0, 560, 745, 1352, 830, precision=.5)
        
        if self.debug :
            print(pos)

        pyautogui.moveTo(pos[0] + 10 + 560, pos[1] + 20 + 745)
        pyautogui.mouseDown()
        pyautogui.moveTo(pos[0] + 20 + 560, pos[1] - 200 + 745, .01)
        pyautogui.mouseUp()
    
    def do_accept_diverted_power(self) :
        pos = imagesearch_loop(self.main_path + "\\task_images\\accept_diverted_power\\key.jpg", 0)

        pyautogui.click(x=pos[0] + 10, y=pos[1] + 40)

    def do_download_data(self) :
        pos = imagesearch_loop(self.main_path + "\\task_images\\download_data\\key.jpg", 0)

        pyautogui.click(x=pos[0] + 40, y=pos[1] + 5)
    
    def do_upload_data(self) :
        pos = imagesearch_loop(self.main_path + "\\task_images\\upload_data\\key.jpg", 0)

        pyautogui.click(x=pos[0] + 40, y=pos[1] + 5)
    
    def do_swipe_card(self) :
        pyautogui.click(x=760, y=820)
        sleep(.3)
        pyautogui.moveTo(510, 490)
        pyautogui.mouseDown()
        pyautogui.moveTo(1430, 420, 3.2, pyautogui.easeInOutQuad)
        sleep(.1)
        pyautogui.mouseUp()
    
    def do_unlock_manifolds(self) :
        for i in range(10) :
            pos = imagesearch_loop(self.main_path + "\\task_images\\unlock_manifolds\\" + str(i + 1) + ".jpg", 0)

            pyautogui.click(x=pos[0] + 10, y=pos[1] + 10)

    def do_stabilize_steering(self) :
        pyautogui.moveTo(960, 540)
        sleep(.1)
        pyautogui.click()

    def do_empty_garbage(self) :
        print("daf")
        pyautogui.moveTo(1270, 430)
        pyautogui.mouseDown()
        pyautogui.moveTo(1270, 820, .2)
        sleep(3)
        pyautogui.mouseUp()

    def do_refuel_station(self) :
        pyautogui.moveTo(1470, 890)
        pyautogui.mouseDown()
        sleep(3.1)
        pyautogui.mouseUp()

    def do_fuel_engine(self) :
        pyautogui.moveTo(1470, 890)
        pyautogui.mouseDown()
        sleep(3.1)
        pyautogui.mouseUp()

    def do_calibrate_distributer(self) :
        
        locations = [1230, (230, 500, 780)]

        for i in range(3) :
            done = False
            while done == False :
                im = pyautogui.screenshot()
                matches = im.getpixel((locations[0], locations[1][i]))
                if matches != (0,0,0) :
                    pyautogui.click(x=locations[0], y=locations[1][i] + 90)
                    done = True
                sleep(.1)

    def do_prime_shields(self) :
        locations = [(963, 172), (739, 298), (1170, 298), (952, 422), (723, 550), (1170, 550), (952, 678)]
        im = pyautogui.screenshot()
                
        for index, loc in enumerate(locations) :
            matches = im.getpixel((locations[index][0], locations[index][1]))
            if self.debug :
                print(matches)
            if matches[1] < 200 :
                pyautogui.click(loc[0], loc[1] + 30)
    
    def do_clean_o2_filter(self) :
        keep_going = True
        while keep_going :
            im = pyautogui.screenshot()

            nothing_left = False
            
            for i in range(730, 1390, 5) :
                for j in range(120, 980, 5) :
                    pix = im.getpixel((i, j))
                    
                    if pix[0] > 60 and pix[0] < 80 and pix[1] > 70 and pix[1] < 85 and pix[2] > 14 and pix[2] < 25 :
                        if self.debug :
                            print(i,j)
                        pyautogui.moveTo(i, j)
                        pyautogui.mouseDown()
                        pyautogui.moveTo(620, 540)
                        pyautogui.moveTo(300, 540)
                        pyautogui.mouseUp()
                        sleep(.1)
                        im = pyautogui.screenshot()
                        nothing_left = True

            if nothing_left == False :
                keep_going = False