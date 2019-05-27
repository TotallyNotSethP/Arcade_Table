from __future__       import print_function
from classes.screen   import Screen
from classes.joystick import Joystick
from os               import system
from time             import sleep

class Block:
    def __init__(self, screen, starting_x, starting_y, red, green, blue):
        self.screen   = screen
        self.red      = red
        self.green    = green
        self.blue     = blue
        self.position = {"x": starting_x,
                         "y": starting_y}
        self.screen.changePixel(starting_x, starting_y, red, green, blue)
        print(self.position)
        
    def move(self, direction):
        if(direction == "up" and self.position["y"] < 16):
            self.screen.changePixel(self.position["x"], self.position["y"], 0, 0, 0)
            self.position["y"] += 1
            self.screen.changePixel(self.position["x"], self.position["y"], self.red, self.green, self.blue)
        elif(direction == "down" and self.position["y"] > 0):
            self.screen.changePixel(self.position["x"], self.position["y"], 0, 0, 0)
            self.position["y"] -= 1
            self.screen.changePixel(self.position["x"], self.position["y"], self.red, self.green, self.blue)
        elif(direction == "left" and self.position["x"] < 32):
            self.screen.changePixel(self.position["x"], self.position["y"], 0, 0, 0)
            self.position["x"] += 1
            self.screen.changePixel(self.position["x"], self.position["y"], self.red, self.green, self.blue)
        elif(direction == "right" and self.position["x"] > 0):
            self.screen.changePixel(self.position["x"], self.position["y"], 0, 0, 0)
            self.position["x"] -= 1
            self.screen.changePixel(self.position["x"], self.position["y"], self.red, self.green, self.blue)
            
def simple_game():
    screen   = Screen(17, 33, height = 400)
    joystick = Joystick(0)
    avatar   = Block(screen, 16, 8, 255, 255, 255)
    
    try:
        joystick.inputListener("up",    lambda: avatar.move("up"))
        joystick.inputListener("down",  lambda: avatar.move("down"))
        joystick.inputListener("left",  lambda: avatar.move("left"))
        joystick.inputListener("right", lambda: avatar.move("right"))
        for i in range(5):
            avatar.move("up")
        while(not screen.threadEnded):
            sleep(0.1)
    except:
        sleep(0)
    joystick.endListeners()
    system("clear")

if(__name__ == "__main__"):
    simple_game()
