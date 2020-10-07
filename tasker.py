import os
import pyautogui
import time
from pyautogui import sleep
from python_imagesearch.imagesearch import imagesearch
from python_imagesearch.imagesearch import region_grabber
from python_imagesearch.imagesearch import imagesearcharea
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
            for path2 in os.listdir(main_path + "\\task_images\\" + path) :
                if path2[:3] == "key" :
                    image_key_list.append((main_path + "\\task_images\\" + path + "\\" + path2, path))


        if self.debug :
            print(f"Loaded {len(image_key_list)} image keys")
            
        return image_key_list

    def is_approximate(self, rgb1, rgb2, tolerance) :
        if rgb1[0] > rgb2[0] - tolerance and rgb1[0] < rgb2[0] + tolerance :
            if rgb1[1] > rgb2[1] - tolerance and rgb1[1] < rgb2[1] + tolerance :
                if rgb1[2] > rgb2[2] - tolerance and rgb1[2] < rgb2[2] + tolerance :
                    return True
        
        return False
    
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
        pyautogui.mouseDown()
        pyautogui.mouseUp()

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
                
                    pix2 = (70, 77, 20)

                    if self.is_approximate(pix, pix2, 9):
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
    
    def do_chart_course(self) :
        x_locs = (560, 763, 959, 1156, 1358)
        ship_color = (35, 111, 159)
        loc_color = (35, 111, 160)

        im = pyautogui.screenshot()
        y_locs = [270, 270, 270, 270, 270]

        for i in range(5) :
            j = 270
            found = False
            
            while found == False and j < 810 :
                pix = im.getpixel((x_locs[i], j))

                if i == 0 :
                    if self.is_approximate(pix, ship_color, 5) :
                        y_locs[i] = (j)
                        found = True
                else :
                    if self.is_approximate(pix, loc_color, 5) :
                        y_locs[i] = (j)
                        found = True

                j += 1
        
        if self.debug :
            print(x_locs)
            print(y_locs)
        for i, x in enumerate(x_locs) :
            if i != 0 :
                pyautogui.mouseDown()
            pyautogui.moveTo(x + 10, y_locs[i] + 10, .1)
            pyautogui.mouseUp()

    def do_align_engine(self) :
        top = (1318, 198)
        bottom = (1308, 874)

        im = pyautogui.screenshot()
        top_pix = im.getpixel(top)
        

        if self.is_approximate(top_pix, (202, 202, 216), 1) :
            pyautogui.moveTo(top[0], top[1])
        else :
            pyautogui.moveTo(bottom[0], bottom[1])

        pyautogui.mouseDown()
        pyautogui.moveTo(1244, 538)
        pyautogui.mouseUp() 
    
    def do_clear_asteroids(self) :
        a_color = (55, 112, 66)
        keep_going = True
        
        im = pyautogui.screenshot()


        while keep_going :
            keep_going = False
            for x in range(557, 1363, 5) :
                for y in range(137, 940, 5) :
                    if self.is_approximate(a_color, im.getpixel((x,y)), 1) :
                        pyautogui.moveTo(x, y)
                        pyautogui.mouseDown()
                        pyautogui.mouseUp()
                        
                        
                        keep_going = True
                        im = pyautogui.screenshot()
    
    def do_measure_weather(self) :
        pyautogui.moveTo(1220, 852)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
    
    def do_buy_beverage(self) :
        x_locs = (480, 680, 880, 1080)
        y_locs = (270, 650, 990)

        beverage = (None, None)

        for drawing in os.listdir(self.main_path + "\\task_images\\buy_beverage\\drawings") :
            
            if self.debug :
                print(drawing)

            pos = imagesearch(self.main_path + "\\task_images\\buy_beverage\\drawings\\" + drawing, precision=.6)

            if pos[0] != -1 :
                beverage = (pos, drawing)
    
        beverage_to_get = [imagesearch_loop(self.main_path + "\\task_images\\buy_beverage\\beverages\\" + beverage[1], 0), 0, 0]

        if self.debug:
            print(f"need to get {beverage}")
            print(beverage_to_get)

        letters = [(1240, 400), (1350, 400), (1480, 400)]
        numbers = [(1240, 520), (1350, 520), (1480, 520), (1350, 640)]

        if beverage_to_get[0][0] < x_locs[0] :
            beverage_to_get[1] = 0

        elif beverage_to_get[0][0] < x_locs[1] :
            beverage_to_get[1] = 1
        
        elif beverage_to_get[0][0] < x_locs[2] :
            beverage_to_get[1] = 2
        
        elif beverage_to_get[0][0] < x_locs[3] :
            beverage_to_get[1] = 3
        

        if beverage_to_get[0][1] < y_locs[0] :
            beverage_to_get[2] = 0

        elif beverage_to_get[0][1] < y_locs[1] :
            beverage_to_get[2] = 1
        
        elif beverage_to_get[0][1] < y_locs[2] :
            beverage_to_get[2] = 2

        pyautogui.moveTo(letters[beverage_to_get[2]][0], letters[beverage_to_get[2]][1])
        pyautogui.mouseDown()
        pyautogui.mouseUp()

        pyautogui.moveTo(numbers[beverage_to_get[1]][0], numbers[beverage_to_get[1]][1])
        pyautogui.mouseDown()
        pyautogui.mouseUp()

        pyautogui.moveTo(1475, 645)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
    
    def do_enter_id_code(self) :
        pyautogui.moveTo(800, 910)
        pyautogui.mouseDown()
        pyautogui.mouseUp()

        search_region = ((788, 710), (824, 770))
        region_shift = 28
        number_list = []

        sleep(.7)
        im = region_grabber((0, 0, 1920, 1080))

        for i in range(5) :
            for number in range(10) :
                if len(number_list) == i : 
                    temp_search = [search_region[0][0] + (region_shift * i), search_region[0][1], search_region[1][0] + (region_shift * i), search_region[1][1]]
                    pos = imagesearcharea(self.main_path + "\\task_images\\enter_id_code\\numbers\\" + str(number) + ".jpg", temp_search[0], temp_search[1], temp_search[2], temp_search[3])
                    

                    if pos[0] != -1 :
                        number_list.append(number)
                        if self.debug :
                            print(f"found {number}!")
        
        if self.debug :
            print(f"ID code is {number_list}")
        
        x_locs = (836, 960, 1075)
        y_locs = (130, 240, 350, 460)

        for number in number_list :
            
            if number == 0 :
              temp_x = x_locs[1]
              temp_y = y_locs[3]
            else :  
                if number < 4 :
                    temp_y = y_locs[0]
                elif number < 7 :
                    temp_y = y_locs[1]
                else :
                    temp_y = y_locs[2]

                if (number - 1) % 3 == 0 :
                    temp_x = x_locs[0]
                elif (number - 2) % 3 == 0 :
                    temp_x = x_locs[1]
                else :
                    temp_x = x_locs[2]
            
            pyautogui.moveTo((temp_x, temp_y))
            pyautogui.mouseDown()
            pyautogui.mouseUp()
        
        pyautogui.moveTo((x_locs[2], y_locs[3]))
        pyautogui.mouseDown()
        pyautogui.mouseUp()
    
    def do_get_water_can(self) :
        pos1 = imagesearch(self.main_path + "\\task_images\\get_water_can\\can1.jpg")
        pos2 = imagesearch(self.main_path + "\\task_images\\get_water_can\\can2.jpg")
        
        if pos1[0] != -1 :
            pyautogui.moveTo((pos1[0] + 7, pos1[1] + 7))
        else :
            pyautogui.moveTo((pos2[0] + 7, pos2[1] + 7))
        
        pyautogui.mouseDown()
        pyautogui.mouseUp()
    
    def do_water_plants(self) :
        pyautogui.moveTo((500, 580))
        pyautogui.mouseDown()
        pyautogui.mouseUp()

        pyautogui.moveTo((824, 640))
        pyautogui.mouseDown()
        pyautogui.mouseUp()

        pyautogui.moveTo((1130, 590))
        pyautogui.mouseDown()
        pyautogui.mouseUp()

        pyautogui.moveTo((1417, 617))
        pyautogui.mouseDown()
        pyautogui.mouseUp()
    
    def do_assemble_artifact(self) :
        x_loc = 950
        y_locs = (185, 300, 423, 550, 665)

        search_area = (420, 890, 1500, 1030)

        for i in range(5) :
            pos = imagesearcharea(self.main_path + "\\task_images\\assemble_artifact\\pieces\\" + str(i) + ".jpg", search_area[0], search_area[1], search_area[2], search_area[3])

            print(pos[0] + search_area[0], pos[1] + search_area[1])

            pyautogui.moveTo((pos[0] + search_area[0] + 30, pos[1] + search_area[1] + 30))
            pyautogui.mouseDown()
            pyautogui.moveTo((x_loc, y_locs[i]))
            pyautogui.mouseUp()

    def do_inspect_sample(self) :
        null_button_color = (189, 189, 189)
        button_loc = (1256, 940)
        im = pyautogui.screenshot()

        x_locs = (732, 845, 960, 1075, 1190)
        y_locs = (480, 850)
        blue = (125, 126, 239)
        
        if self.is_approximate(null_button_color, im.getpixel(button_loc), 3) :
            for i in range(5) :
                if not self.is_approximate(blue, im.getpixel((x_locs[i], y_locs[0])), 10) :
                    pyautogui.moveTo(x_locs[i], y_locs[1])
                    pyautogui.mouseDown()
                    pyautogui.mouseUp()
                    break
        else :
            pyautogui.moveTo(button_loc[0], button_loc[1])
            pyautogui.mouseDown()
            pyautogui.mouseUp()
    
    def do_run_diagnostics(self) :
        null_button_color = (211, 211, 211)
        button_loc = (777, 945)
        red = (255, 0, 0)
        selection_locs = ((756, 246), (670, 355), (702, 454), (813, 414))

        im = pyautogui.screenshot()
        pos = imagesearcharea(self.main_path + "\\task_images\\run_diagnostics\\begin.jpg", 535, 585, 993, 683)

        if pos[0] == -1 :
            for i in selection_locs :
                if self.is_approximate(red, im.getpixel(i), 4) :
                    pyautogui.moveTo(i[0], i[1] + 20)
                    pyautogui.mouseDown()
                    pyautogui.mouseUp()
                    break
        else :
            pyautogui.moveTo(button_loc[0], button_loc[1])
            pyautogui.mouseDown()
            pyautogui.mouseUp()