import numpy as np

class Btn_1:
    def __init__(self, x, y):
        self.position = np.array([x, y])
        self.pixel_map = [
            ".....a.....",
            "....aaa....",
            "...aaaaa...",
            "..aaabaaa..",
            ".aaaabaaaa.",
            "aaaaabaaaaa",
            ".aaaabaaaa.",
            "..aaabaaa..",
            "...aaaaa...",
            "....aaa....",
            ".....a....."
        ]  
    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "a": 
                    x0 = x_start + x * 1
                    y0 = y_start + y * 1
                    draw_tool.rectangle([x0, y0, x0 + 1, y0 + 1], fill = (204, 242, 255))
                if pixel == "b": 
                    x0 = x_start + x * 1
                    y0 = y_start + y * 1
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (0, 115, 153))  

import numpy as np

class Btn_2:
    def __init__(self, x, y):
        self.position = np.array([x, y])
        self.pixel_map = [
            ".....a.....",
            "....aaa....",
            "...aaaaa...",
            "..aabbbaa..",
            ".aaaaabaaa.",
            "aaaabbbaaaa",
            ".aaabaaaaa.",
            "..aabbbaa..",
            "...aaaaa...",
            "....aaa....",
            ".....a....."
        ]  
    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "a": 
                    x0 = x_start + x * 1
                    y0 = y_start + y * 1
                    draw_tool.rectangle([x0, y0, x0 + 1, y0 + 1], fill = (204, 242, 255))
                if pixel == "b": 
                    x0 = x_start + x * 1
                    y0 = y_start + y * 1
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (0, 115, 153))   