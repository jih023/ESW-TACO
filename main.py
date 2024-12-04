from PIL import Image, ImageDraw
import numpy as np
from Background import Bouble1
from Background import Bouble2
from Background import Flower1
from Background import Flower2
from Background import Flower3
from Character import Octopus
from obstacle import Flour
from obstacle import Onion
from obstacle import Sauce1
from obstacle import Sauce2
from obstacle import Katsuo
from Start import Btn_1
from Start import Btn_2
from Joystick import Joystick

import time
import random
from colorsys import hsv_to_rgb

def main():
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image) 
    
    screen_height = joystick.height
    screen_width = joystick.width

    my_bouble11 = Bouble1(190, 115)
    my_bouble12 = Bouble1(55, 65)
    my_bouble21 = Bouble2(210, 80)
    my_bouble22 = Bouble2(25, 35)
    my_bouble23 = Bouble2(30, 117)

    my_flower11 = Flower1(0, 210)
    my_flower21 = Flower2(40, 200)
    my_flower31 = Flower3(10, 170)
    my_flower12 = Flower1(170, 170)
    my_flower22 = Flower2(160, 200)
    my_flower32 = Flower3(200, 200)

    my_octopus1 = Octopus(98, 180)

    my_flour1 = Flour(0, 0, screen_width, screen_height)
    my_flour2 = Flour(0, 0, screen_width, screen_height)

    my_onion1 = Onion(0, 0, screen_width, screen_height)
    my_onion2 = Onion(0, 0, screen_width, screen_height)

    my_sauce11 = Sauce1(0, 0, screen_width, screen_height)
    my_sauce12 = Sauce1(0, 0, screen_width, screen_height)

    my_sauce21 = Sauce2(0, 0, screen_width, screen_height)
    my_sauce22 = Sauce2(0, 0, screen_width, screen_height)

    my_katsuo1 = Katsuo(0, 0, screen_width, screen_height)
    my_katsuo2 = Katsuo(0, 0, screen_width, screen_height)

    btn1 = Btn_1(110, 170)
    btn2 = Btn_2(175, 170)

    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(179, 230, 255, 100))

    while True:
        command = {'move': False, 'up_pressed': False , 'down_pressed': False, 'left_pressed': False, 'right_pressed': False}
        
        if not joystick.button_U.value:  # up pressed
            command['up_pressed'] = True
            command['move'] = True

        if not joystick.button_D.value:  # down pressed
            command['down_pressed'] = True
            command['move'] = True

        if not joystick.button_L.value:  # left pressed
            command['left_pressed'] = True
            command['move'] = True

        if not joystick.button_R.value:  # right pressed
            command['right_pressed'] = True
            command['move'] = True

        # btn1.draw(my_draw)
        # btn2.draw(my_draw)

        my_octopus1.move(command)
        my_flour1.move()
        my_flour2.move()
        my_onion1.move()
        my_onion2.move()
        my_sauce11.move()
        my_sauce12.move()
        my_sauce21.move()
        my_sauce22.move()
        my_katsuo1.move()
        my_katsuo2.move()
        
        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(179, 230, 255, 100))

        my_bouble11.draw(my_draw)
        my_bouble12.draw(my_draw)
        my_bouble21.draw(my_draw)
        my_bouble22.draw(my_draw)
        my_bouble23.draw(my_draw)

        my_flower11.draw(my_draw)
        my_flower21.draw(my_draw)
        my_flower31.draw(my_draw)
        my_flower12.draw(my_draw)
        my_flower22.draw(my_draw)
        my_flower32.draw(my_draw)

        my_flour1.draw(my_draw)
        my_flour2.draw(my_draw)
        my_onion1.draw(my_draw)
        my_onion2.draw(my_draw)
        my_sauce11.draw(my_draw)
        my_sauce12.draw(my_draw)
        my_sauce21.draw(my_draw)
        my_sauce22.draw(my_draw)
        my_katsuo1.draw(my_draw)
        my_katsuo2.draw(my_draw)

        my_octopus1.draw(my_draw)

        
        # my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(179, 230, 255, 100))
        # my_draw.ellipse(tuple(my_octopus1.position), outline = my_octopus1.outline, fill = (0, 0, 0))

        joystick.disp.image(my_image)
        # joystick.disp.update()