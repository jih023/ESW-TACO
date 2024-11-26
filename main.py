from PIL import Image, ImageDraw
import numpy as np

from Background import Bouble1
from Background import Bouble2

def main():
    # joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(179, 230, 255, 100))


