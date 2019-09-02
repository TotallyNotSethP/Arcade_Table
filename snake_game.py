from .classes.screen   import Screen
from .classes.block    import Block
from .classes.joystick import Joystick

class Snake:
    def __init__(self, screen, head_starting_x, head_starting_y, starting_length, red, green, blue):
        self.blocks    = []
        self.turns     = []
        self.screen    = screen
        self.head_pos  = {"x": head_starting_x, "y": head_starting_y}
        for i in range(starting_length):
            self.blocks.append({"block": Block(self.screen,
                                               self.head_pos["x"] - i, self.head_pos["y"],
                                               self.red, self.green, self.blue, 0, 0, 0),
                                "direction": "right"})
    
    def turn(self, direction):
        if(direction == "up" or direction == "down" or direction == "left" or direction == "right"):
            self.turns.append({"x": self.head_pos["x"], "y": self.head_pos["y"],
                               "direction": direction})
        self.forward()
            
    def forward(self):
        i = 0
        for turn in self.turns:
            turn_valid = False
            for block in self.blocks:
                if(turn["x"] == block["block"].position["x"] and
                   turn["y"] == block["block"].position["y"]):
                    block["direction"] = turn["direction"]
                    turn_valid = True
            if(not turn_valid):
                self.turns.pop(i)
            i += 1
        for block in self.blocks:
            block["block"].move(block["direction"])
            
    def grow(self):
        if(self.blocks[-1]["direction"] == "up"):
            self.blocks.append({"block": Block(self.screen,
                                               self.blocks[-1]["block"].position["x"], self.blocks[-1]["block"].position["y"] - 1,
                                               self.red, self.green, self.blue, 0, 0, 0),
                                "direction": "up"})
        
if(__name__ == "__main__"):
    screen = Screen(17, 33)
    snake  = Snake(screen, 16, 8, 5, 0, 255, 0)