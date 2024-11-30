import numpy as np

class Bouble1:
    def __init__(self, x, y):
        self.position = np.array([x, y])
        self.pixel_map = [
            ".aaa.",
            "aaawa",
            "aaawa",
            "aaaaa",
            ".aaa.",
            ]
    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "a":
                    x0 = x_start + x * 5
                    y0 = y_start + y * 5
                    draw_tool.rectangle([x0, y0, x0 + 5, y0 + 5], fill = (102, 204, 255))
                if pixel == "w":
                    x0 = x_start + x * 5
                    y0 = y_start + y * 5
                    draw_tool.rectangle([x0, y0, x0 + 5, y0 + 5], fill = (255, 255, 255))

class Bouble2:
    def __init__(self, x, y):
        self.position = np.array([x, y])
        self.pixel_map = [
            ".bb.",
            "bbwb",
            "bbbb",
            ".bb.",
            ]
    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "b":
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (77, 166, 255))
                if pixel == "w":
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 255, 255))

class flower1:
    def __init__(self, x, y):
        self.position = np.array([x, y])
        self.pixel_map = [
            "..cc....cc...",
            ".c..c..c..c..",
            ".c..c.c...c..",
            ".c...c...c...",
            "..c.....c....",
            "..c......ccc.",
            ".c..........c",
            "c...c..cc...c",
            "c..cc..c.ccc.",
            ".cc.c..c.....",
            "....c..c.....",
            ".....cc......",
            ]
    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "c":
                    x0 = x_start + x * 3
                    y0 = y_start + y * 3
                    draw_tool.rectangle([x0, y0, x0 + 3, y0 + 3], fill = (255, 153, 204))

class flower2:
    def __init__(self, x, y):
        self.position = np.array([x, y])
        self.pixel_map = [
            ".....ddd.......",
            "....d...d......",
            "....d....d.....",
            ".dd..d...d.ddd.",
            "d..d.d..ddd...d",
            "d...dd........d",
            "d.............d",
            "d..........d.dd",
            ".d..d...d...dd.",
            "..ddd...dd...d.",
            "...d....dd....d",
            "...d....d.dd..d",
            "...d...d...ddd.",
            "....ddd........"
            ]
    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "d":
                    x0 = x_start + x * 3
                    y0 = y_start + y * 3
                    draw_tool.rectangle([x0, y0, x0 + 3, y0 + 3], fill = (46, 184, 46))

class Flower3:
    def __init__(self, x, y):
        self.position = np.array([x, y])
        self.pixel_map = [
            "....ee.......",
            "...e..e.eee..",
            "...e...e...e.",
            ".eee...e...e.",
            "e..ee......e.",
            "e..........e.",
            "e........ee..",
            ".ee.......ee.",
            "...ee.......e",
            "...e...e....e",
            "...e...ee..e.",
            "...ee..e.eee.",
            ".....ee......"
            ]
    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "e":
                    x0 = x_start + x * 3
                    y0 = y_start + y * 3
                    draw_tool.rectangle([x0, y0, x0 + 3, y0 + 3], fill = (255, 204, 0))