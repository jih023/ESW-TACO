import numpy as np

class Flour:
    def __init__(self, x, y, width, height):
        self.position = np.array([x, y])
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.reset_position()
        self.pixel_map = [
            "...aaaaaaab...",
            "...baaaaaaa...",
            "...bbbababb...",
            "..aaaabaaaab..",
            "..aaaawyaaab..",
            "..aaawyaaaaa..",
            ".baawyaaaaaaa.",
            ".babybgggggaa.",
            ".bawygcccgcgb.",
            ".bbybgcgcgcgb.",
            ".awywgcccgcga.",
            "abybagggggggab",
            "abyaagcccccgab",
            "aayaagggggcgab",
            "bayaagcccccgaa",
            "baayagcgggggaa",
            "baaaagcccccgab",
            ".baaaagggggaa.",
            "..aaaaaaabbb.."
        ]     
    def reset_position(self):
        start_x = random.choice([0, self.screen_width])
        start_y = random.randint(50, self.screen_height)
        self.position = np.array([start_x, start_y], dtype=float)
        speed = speed = random.uniform(2.0, 5.0)
        self.velocity = np.array([-speed if start_x == self.screen_width else speed, 0])

    def move(self):
        self.position += self.velocity
        
        if self.position[0] < -len(self.pixel_map[0]) * 4 or self.position[0] > self.screen_width:
            self.reset_position()
        
        if self.position[0] < -len(self.pixel_map[0]) * 4 or self.position[0] > self.screen_width:
            self.reset_position()

    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "a": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (204, 153, 0))
                if pixel == "b": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (77, 57, 0))
                if pixel == "y": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (255, 214, 51))
                if pixel == "w": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (255, 255, 255))
                if pixel == "g": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (204, 204, 204))
                if pixel == "c": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (51, 51, 51))
                
class Onion:
    def __init__(self, x, y, width, height):
        self.position = np.array([x, y])
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.reset_position()
        self.pixel_map = [
            "......aab",
            "......aa.",
            "......aab",
            ".....aaa.",
            ".....aab.",
            "aaa..aab.",
            ".baa.aa..",
            "..aa.aa..",
            "..babaa..",
            "...aaab..",
            "...aaab..",
            "...baac..",
            "...baac..",
            "....cac..",
            "....ccc..",
            "....ccc..",
            "....ccd..",
            "....dcd..",
            "....ddd..",
            "....ddd..",
            "....ddw..",
            "....wdw..",
            "....www..",
            "....www.."
            ]
    def reset_position(self):
        start_x = random.choice([0, self.screen_width])
        start_y = random.randint(50, self.screen_height)
        self.position = np.array([start_x, start_y], dtype=float)
        speed = speed = random.uniform(2.0, 5.0)
        self.velocity = np.array([-speed if start_x == self.screen_width else speed, 0])

    def move(self):
        self.position += self.velocity
        
        if self.position[0] < -len(self.pixel_map[0]) * 4 or self.position[0] > self.screen_width:
            self.reset_position()
        
        if self.position[0] < -len(self.pixel_map[0]) * 4 or self.position[0] > self.screen_width:
            self.reset_position()

    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "a": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (41, 163, 41))
                if pixel == "b": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (20, 82, 20))
                if pixel == "c": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (153, 255, 51))
                if pixel == "d": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (2206, 255, 153))
                if pixel == "w": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (255, 255, 255))

class Sauce1:
    def __init__(self, x, y, width, height):
        self.position = np.array([x, y])
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.reset_position()
        self.pixel_map = [
            "..baab..",
            "..baab..",
            "..cddc..",
            ".cdedec.",
            "cdededec",
            "ywwwwwwa",
            "yyywwwaa",
            "ycccccca",
            "ycccccca",
            "yaaaaaaa",
            "aaaaaaaa",
            "cdededec",
            "cedededc",
            "cedededc",
            ".dddddd.",
            "cdededec",
            "cedededc",
            "cdededec",
            "cdededec",
            "cdededec",
            "cdededec",
            "cdededec",
            "cedededc",
            ".cccccc."
            ]
    def reset_position(self):
        start_x = random.choice([0, self.screen_width])
        start_y = random.randint(50, self.screen_height)
        self.position = np.array([start_x, start_y], dtype=float)
        speed = speed = random.uniform(2.0, 5.0)
        self.velocity = np.array([-speed if start_x == self.screen_width else speed, 0])

    def move(self):
        self.position += self.velocity
        
        if self.position[0] < -len(self.pixel_map[0]) * 4 or self.position[0] > self.screen_width:
            self.reset_position()
        
        if self.position[0] < -len(self.pixel_map[0]) * 4 or self.position[0] > self.screen_width:
            self.reset_position()

    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "a": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (255, 0, 0))
                if pixel == "b": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (128, 0, 0))
                if pixel == "c": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (102, 51, 0))
                if pixel == "d": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (153, 77, 0))
                if pixel == "e": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (255, 128, 0))
                if pixel == "y": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (255, 204, 0))
                if pixel == "w": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (255, 255, 255))

class Sauce2:
    def __init__(self, x, y, width, height):
        self.position = np.array([x, y])
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.reset_position()
        self.pixel_map = [
            "...ytty...",
            "...gggg...",
            "...baaa...",
            "...aaab...",
            "...aaaa...",
            "..caaaaa..",
            "..aaaaab..",
            "..aaaaaa..",
            ".baaaaaaa.",
            ".caaaaaab.",
            ".aaaaaaaa.",
            "baaaaaaaaa",
            "caaaaaaaaa",
            "caaayyaaac",
            "aaayttyaac",
            "aaytyytyac",
            "aayttytyac",
            "aaayttyaac",
            "caaayyaaab",
            "baaaaaaaab",
            "caaaaaaaab",
            "aaaaaaaaac",
            ".aaaaaaac.",
            "..aaccbb.."
            ]
    def reset_position(self):
        start_x = random.choice([0, self.screen_width])
        start_y = random.randint(50, self.screen_height)
        self.position = np.array([start_x, start_y], dtype=float)
        speed = speed = random.uniform(2.0, 5.0)
        self.velocity = np.array([-speed if start_x == self.screen_width else speed, 0])

    def move(self):
        self.position += self.velocity
        
        if self.position[0] < -len(self.pixel_map[0]) * 4 or self.position[0] > self.screen_width:
            self.reset_position()
        
        if self.position[0] < -len(self.pixel_map[0]) * 4 or self.position[0] > self.screen_width:
            self.reset_position()

    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "a": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (255, 230, 179))
                if pixel == "b": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (153, 77, 0))
                if pixel == "c": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (255, 153, 51))
                if pixel == "g": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (128, 128, 128))
                if pixel == "y": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (255, 204, 0))
                if pixel == "t": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (255, 235, 153))

class Katsuo:
    def __init__(self, x, y, width, height):
        self.position = np.array([x, y])
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.reset_position()
        self.pixel_map = [
            "aabbccccbbba",
            "bbbbccccbbba",
            ".dddeeezddd.",
            ".bdzzzezddb.",
            ".bddezezzdb.",
            ".bbzzeezdbb.",
            ".bbdeeezdbb.",
            ".bbbeeeebba.",
            ".bbbzeezbba.",
            ".bbzezzezba.",
            ".bbzezzezbb.",
            ".abbeeeebbb.",
            ".abzzzzzzbb.",
            "bbbbeeeebbba",
            "aabbccccbaaa"
            ]
    def reset_position(self):
        start_x = random.choice([0, self.screen_width])
        start_y = random.randint(50, self.screen_height)
        self.position = np.array([start_x, start_y], dtype=float)
        speed = speed = random.uniform(2.0, 5.0)
        self.velocity = np.array([-speed if start_x == self.screen_width else speed, 0])

    def move(self):
        self.position += self.velocity
        
        if self.position[0] < -len(self.pixel_map[0]) * 4 or self.position[0] > self.screen_width:
            self.reset_position()
        
        if self.position[0] < -len(self.pixel_map[0]) * 4 or self.position[0] > self.screen_width:
            self.reset_position()

    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "a": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (204, 82, 0))
                if pixel == "b": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (255, 117, 26))
                if pixel == "c": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (255, 209, 179))
                if pixel == "d": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (255, 179, 128))
                if pixel == "e": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (255, 242, 230))
                if pixel == "z": 
                    x0 = x_start + x * 2
                    y0 = y_start + y * 2
                    draw_tool.rectangle([x0, y0, x0 + 2, y0 + 2], fill = (26, 12, 0))