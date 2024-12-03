from PIL import Image, ImageDraw
import numpy as np
from Background import Bouble1
from Background import Bouble2
from Start import Btn_1
from Start import Btn_2
from Joystick import Joystick

def main():
    joystick = Joystick()

    cs_pin = DigitalInOut(board.CE0)
    dc_pin = DigitalInOut(board.D25)
    reset_pin = DigitalInOut(board.D24)
    BAUDRATE = 24000000

    spi = board.SPI()
    disp = st7789.ST7789(
        spi,
        height=240,
        y_offset=80,
        rotation=180,
        cs=cs_pin,
        dc=dc_pin,
        rst=reset_pin,
        baudrate=BAUDRATE,
    )

    button_A = DigitalInOut(board.D5)
    button_A.direction = Direction.INPUT

    button_B = DigitalInOut(board.D6)
    button_B.direction = Direction.INPUT

    backlight = DigitalInOut(board.D26)
    backlight.switch_to_output()
    backlight.value = True

    pressedColorA = (255, 255, 255)
    pressedColorB = (255, 255, 255)

    width = disp.width
    height = disp.height
    image = Image.new("RGB", (width, height))

    draw = ImageDraw.Draw(image)

    draw.rectangle((0, 0, width, height), outline=0, fill=(255, 0, 0))
    disp.image(image)

    draw = ImageDraw.Draw(image)

    draw.rectangle((0, 0, width, height), outline=0, fill=0)


    btn1 = Btn_1(110, 170)
    btn2 = Btn_2(175, 170)

    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)

    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(179, 230, 255, 100))

    while True:
        btn1.draw(my_draw)
        btn2.draw(my_draw)

        if not button_A.value:  
            pressedColorA = (51, 133, 255)
        pressedColorA = (255, 255, 255)

        if not button_B.value:  
            pressedColorB = (51, 133, 255)
        pressedColorB = (255, 255, 255)

        time.sleep(0.01)


