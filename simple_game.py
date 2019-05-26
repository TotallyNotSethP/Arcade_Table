from classes.screen   import Screen
from classes.joystick import Joystick
from os               import system
from time             import sleep

screen = Screen(17, 33, height = 400)

class Block:
    def __init__(self, starting_x, starting_y, red, green, blue):
        screen.changePixel(starting_x, starting_y, red, green, blue)
        self.red      = red
        self.green    = green
        self.blue     = blue
        self.position = {"x": starting_x,
                         "y": starting_y}
        
    def move(self, direction):
        if(direction == "up"):
            screen.changePixel(self.position["x"], self.position["y"], 0, 0, 0)
            self.position["y"] += 1
            screen.changePixel(self.position["x"], self.position["y"], self.red, self.green, self.blue)
        elif(direction == "down"):
            screen.changePixel(self.position["x"], self.position["y"], 0, 0, 0)
            self.position["y"] -= 1
            screen.changePixel(self.position["x"], self.position["y"], self.red, self.green, self.blue)
        elif(direction == "left"):
            screen.changePixel(self.position["x"], self.position["y"], 0, 0, 0)
            self.position["x"] += 1
            screen.changePixel(self.position["x"], self.position["y"], self.red, self.green, self.blue)
        elif(direction == "right"):
            screen.changePixel(self.position["x"], self.position["y"], 0, 0, 0)
            self.position["x"] -= 1
            screen.changePixel(self.position["x"], self.position["y"], self.red, self.green, self.blue)
            
def simple_game():
    joystick = Joystick(0)
    avatar   = Block(16, 8, 255, 255, 255)
    
    try:
        system("clear")
        joystick.inputListener("up",    lambda: avatar.move("up"))
        joystick.inputListener("down",  lambda: avatar.move("down"))
        joystick.inputListener("left",  lambda: avatar.move("left"))
        joystick.inputListener("right", lambda: avatar.move("right"))
        while(not screen.threadEnded):
            sleep(0.1)
    except:
        sleep(0)
        
    joystick.endListeners()
    system("clear")

if(__name__ == "__main__"):
    simple_game()
