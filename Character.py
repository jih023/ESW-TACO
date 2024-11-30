import numpy as np

class Octopus1:
    def __init__(self, x, y):
        self.position = np.array([x, y], dtype=float)  # ???? ???? ?? float ??
        self.velocity = np.array([0, 0], dtype=float)  # ?? ??
        self.acceleration = 1.0  # ??? ??
        self.max_speed = 5.0  # ?? ??
        self.resistance = 0.9  # ?? ?? (1?? ??? ?)
        self.pixel_map = [
            "..........aaaaaaa..........",
            "........bbbbbbbbbaa........",
            ".......bbbbbbbbbbbba.......",
            "......bbbbbbbbbbbbbba......",
            "......abbbbbbbbbbbbba......",
            ".....bbbbbbbbbbbbbbbba.....",
            ".....bbbbcbbbbbcbbbbba.....",
            ".....bbbbccwbbbccwbbba.....",
            ".....abbbbccbbbbccbbba.....",
            ".....abbbbccbbbbccbbba.....",
            ".....abdddbbbbbbbdddba.....",
            ".....abdddbbbbbbbdddbb.....",
            "......bbbbbbaaabbbbbb......",
            "......bbbbbbaaabbbbba......",
            ".......abbbbaaabbbba.......",
            ".........abbbbbbba.........",
            "..........abbbbba..........",
            "..........babbabe..........",
            ".........aeaaaabaa.........",
            ".eab....abaabaeaaba....bae.",
            ".rbea.abeaabaaaabaeba.aber.",
            "..tabaeatraeaaaaartaeabat..",
            "...raabr.baaaaaeab.reaar...",
            "....trt.baaaaeaaaab.trt....",
            "be......eaaat.taaae......eb",
            "aaba..abaaer...raaeba..abaa",
            "taaeabaaart.....traaabaeaat",
            ".rabaaeat.........taeaabar.",
            "..trtrtr...........rtrtrt.."
            ]
    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "a": 
                    x0 = x_start + x * 1
                    y0 = y_start + y * 1
                    draw_tool.rectangle([x0, y0, x0 + 1, y0 + 1], fill = (204, 41, 0))
                if pixel == "b": 
                    x0 = x_start + x * 1
                    y0 = y_start + y * 1
                    draw_tool.rectangle([x0, y0, x0 + 1, y0 + 1], fill = (230, 46, 0))
                if pixel == "c": 
                    x0 = x_start + x * 1
                    y0 = y_start + y * 1
                    draw_tool.rectangle([x0, y0, x0 + 1, y0 + 1], fill = (0, 0, 0))
                if pixel == "d": 
                    x0 = x_start + x * 1
                    y0 = y_start + y * 1
                    draw_tool.rectangle([x0, y0, x0 + 1, y0 + 1], fill = (255, 204, 0))
                if pixel == "w": 
                    x0 = x_start + x * 1
                    y0 = y_start + y * 1
                    draw_tool.rectangle([x0, y0, x0 + 1, y0 + 1], fill = (255, 255, 255))
                if pixel == "r": 
                    x0 = x_start + x * 1
                    y0 = y_start + y * 1
                    draw_tool.rectangle([x0, y0, x0 + 1, y0 + 1], fill = (134, 89, 45))
                if pixel == "t": 
                    x0 = x_start + x * 1
                    y0 = y_start + y * 1
                    draw_tool.rectangle([x0, y0, x0 + 1, y0 + 1], fill = (236, 217, 198))
                if pixel == "e": 
                    x0 = x_start + x * 1
                    y0 = y_start + y * 1
                    draw_tool.rectangle([x0, y0, x0 + 1, y0 + 1], fill = (255, 51, 0))
        
    def move(self, command=None, screen_width=None, screen_height=None):
        """Updates position based on velocity and user commands."""
        if not command['move']:  # ???? ?? ??
            self.velocity *= self.resistance  # ???? ?? ??
        else:  # ???? ?? ??
            target_velocity = np.array([0, 0], dtype=float)  # ?? ??
            
            if command['up_pressed']:
                target_velocity[1] -= self.max_speed
            if command['down_pressed']:
                target_velocity[1] += self.max_speed
            if command['left_pressed']:
                target_velocity[0] -= self.max_speed
            if command['right_pressed']:
                target_velocity[0] += self.max_speed
            
            # ?? ??? ??? ?? (???? ??)
            self.velocity += (target_velocity - self.velocity) * 0.1

        # ?? ??
        speed = np.linalg.norm(self.velocity)
        if speed > self.max_speed:
            self.velocity = self.velocity / speed * self.max_speed

        # ?? ????
        self.position += self.velocity

        # ?? ?? ??
        if screen_width and screen_height:
            self.position[0] = np.clip(self.position[0], 0, screen_width - len(self.pixel_map[0]))
            self.position[1] = np.clip(self.position[1], 0, screen_height - len(self.pixel_map))

class Octopus2:
    def __init__(self, x, y):
        self.position = np.array([x, y])
        self.pixel_map = [
            "..........bffffbb..........",
            "........fffffffgabb........",
            ".......affggffffaaaf.......",
            "......aafffaaffgaaaff......",
            ".....gfgaaaaaaaaaaagfg.....",
            ".....ffgazaaaaazaaaafg.....",
            ".....gfgazzwaaazzwaaff.....",
            ".....gffaazzaaaazzaaaf.....",
            ".....gffgazzaaaazzaaab.....",
            ".....bffgyaaaaaaayyyab.....",
            ".....bagfyaaaaaaayyyaa.....",
            "......aagaaabbbaaaaaf......",
            "......faaaaabbbaaafag......",
            ".......baaaabbbaagfg.......",
            ".........baaaaaaaf.........",
            "..........baaaaab..........",
            "..........abaabac..........",
            ".g.......acaaaabaa.........",
            ".ffb....gfaabacaaba....bgf.",
            ".fbcf.afgaabaaaabacbg.ffbq.",
            "..xafacaftacaaaaatfafafgx..",
            "...taabt.baaaaacab.tfaat...",
            "....xfx.baaaacaaaab.xtx....",
            "fc......fgaax.xaaaf......fb",
            "aagf..fbafct...taagbg..gfgf",
            "gaafafgaatx.....xtaafbffgag",
            ".tabaafax.........xacaabat.",
            "..xtxtxt...........txtxtx.."
            ]
    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "b": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (153, 31, 0))
                if pixel == "f": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 217, 179))
                if pixel == "g": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 166, 77))
                if pixel == "a": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (230, 46, 0))
                if pixel == "z": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (0, 0, 0))
                if pixel == "w": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 255, 255))
                if pixel == "y": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 204, 0))
                if pixel == "c": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 102, 102))
                if pixel == "x": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 204, 204))
                if pixel == "t": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (204, 102, 0))

class Octopus3:
    def __init__(self, x, y):
        self.position = np.array([x, y])
        self.pixel_map = [
            "........cabbccb........",
            "......bbaaaaaagab......",
            ".....caaaabaaggghb.....",
            "....aaaabbbaaaaghhb....",
            "....bahhababaaaahhc....",
            "...cghhzaaaaazaaaabc...",
            ".t.bgghzzwaaazzwabba.t.",
            "qttaaaaazzaaaazzabaattq",
            ".rttaaaazzaaaazzabattr.",
            "..rrtpppaaaaaaappptrr..",
            "...atpppaarrrabpppta...",
            "...babbbaarrraagggac...",
            "....baaabarrrahggaa....",
            "....bbaabbaaahhhaac....",
            ".....bttaaaaahhatt.....",
            ".....ttrbaaaaaacrtt....",
            "...qttr.cbbbaac..rttq..",
            "....rq............qr..."
            ]
    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "a": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 217, 179))
                if pixel == "b": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 166, 77))
                if pixel == "c": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (204, 102, 0))
                if pixel == "g": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (41, 163, 41))
                if pixel == "h": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (20, 82, 20))
                if pixel == "w": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 255, 255))
                if pixel == "z": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (0, 0, 0))
                if pixel == "p": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 153, 204))
                if pixel == "r": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (153, 31, 0))
                if pixel == "t": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (230, 46, 0))
                if pixel == "q": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 153, 102))

class Octopus4:
    def __init__(self, x, y):
        self.position = np.array([x, y])
        self.pixel_map = [
            ".....bbaabbb.....",
            "...bacaccaabbb...",
            "..bacacacacabbb..",
            ".bacaaaaaccacbbb.",
            ".bcaaaaaaaaacbbb.",
            "bacazaaaaazaaabbb",
            "baaazzwaaazzwaabb",
            "bcaaazzaaaazzaabb",
            "bababzzdbbazzbaab",
            "dbpppdddddbbpppaa",
            "ddpppddrrrddpppee",
            "eddddddrrrdddddee",
            ".ddddddrrrdddddd.",
            ".eddddddddddddde.",
            "..dddddddddddde..",
            "...edddddeeeee...",
            ".....eddeeee....."
            ]
    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "a": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (179, 107, 0))
                if pixel == "b": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (96, 64, 32))
                if pixel == "c": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 153, 0))
                if pixel == "d": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 170, 0))
                if pixel == "e": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (179, 119, 0))
                if pixel == "w": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 255, 255))
                if pixel == "z": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (0, 0, 0))
                if pixel == "p": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 153, 204))
                if pixel == "r": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (153, 31, 0))

class Octopus5:
    def __init__(self, x, y):
        self.position = np.array([x, y])
        self.pixel_map = [
            ".....bjhabbb.....",
            "...bhjjjjaabhj...",
            "..bhjacjjachjjj..",
            ".bhjjahjachjjbjj.",
            ".bjjaajjahjjabbj.",
            "bhjazjjaaajaaajjj",
            "bjaazzwaahjzwahjb",
            "bcaahzzajaazzhjbb",
            "babajzzhbbazzhjab",
            "dbppphjdddbbpppaa",
            "ddpppddrrrddpppee",
            "eddddddrrrdddddee",
            ".ddddddrrrdddddd.",
            ".eddddddddddddde.",
            "..dddddddddddde..",
            "...edddddeeeee...",
            ".....eddeeee....."
            ]
    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "a": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (179, 107, 0))
                if pixel == "b": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (96, 64, 32))
                if pixel == "c": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 153, 0))
                if pixel == "d": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 170, 0))
                if pixel == "e": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (179, 119, 0))
                if pixel == "w": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 255, 255))
                if pixel == "z": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (0, 0, 0))
                if pixel == "p": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 153, 204))
                if pixel == "r": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (153, 31, 0))
                if pixel == "h": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 230, 179))
                if pixel == "j": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 204, 102))

class Octopus6:
    def __init__(self, x, y):
        self.position = np.array([x, y])
        self.pixel_map = [
            ".........m.........",
            "....nl.lnlnml.l....",
            "..lnmlnmlnmlnlnl...",
            "..nllnllmlnlnlmlm..",
            ".nmbnnlnjlnmmljlm..",
            "mnbhnjamjamhjjnjnn..", #
            "..bjjaajjahjjabbj..",
            ".bhjazjjaaajaaajjj.",
            ".bjaazzwaahjzwahjb.",
            ".bcaahzzajaazzhjbb.",
            ".babajzzhbbazzhjab.",
            ".dbppphjdddbbpppaa.",
            ".ddpppddrrrddpppee.",
            ".eddddddrrrdddddee.",
            "..ddddddrrrdddddd..",
            "..eddddddddddddde..",
            "...dddddddddddde...",
            "....edddddeeeee....",
            "......eddeeee......"
            ]
    def draw(self, draw_tool):
        x_start, y_start = self.position
        for y, row in enumerate(self.pixel_map):
            for x, pixel in enumerate(row):
                if pixel == "a": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (179, 107, 0))
                if pixel == "b": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (96, 64, 32))
                if pixel == "c": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 153, 0))
                if pixel == "d": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 170, 0))
                if pixel == "e": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (179, 119, 0))
                if pixel == "w": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 255, 255))
                if pixel == "z": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (0, 0, 0))
                if pixel == "p": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 153, 204))
                if pixel == "r": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (153, 31, 0))
                if pixel == "h": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 230, 179))
                if pixel == "j": 
                    x0 = x_start + x * 4
                    y0 = y_start + y * 4
                    draw_tool.rectangle([x0, y0, x0 + 4, y0 + 4], fill = (255, 204, 102))



