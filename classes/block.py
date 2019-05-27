from random import choice
from os     import system
from time   import sleep

class Block:
    def __init__(self, screen, starting_x, starting_y, red, green, blue, trailRed, trailGreen, trailBlue):
        self.red2     = red
        self.red      = trailRed
        self.green2   = green
        self.green    = trailGreen
        self.blue2    = blue
        self.blue     = trailBlue
        self.position = {"x": starting_x,
                         "y": starting_y}
        self.screen   = screen
        self.screen.changePixel(starting_x, starting_y, red, green, blue)
        
    def move(self, direction):
        if(direction == "up" and self.position["y"] < 16):
            self.screen.changePixel(self.position["x"], self.position["y"], self.red, self.green, self.blue)
            self.position["y"] += 1
            self.screen.changePixel(self.position["x"], self.position["y"], self.red2, self.green2, self.blue2)
        elif(direction == "down" and self.position["y"] > 0):
            self.screen.changePixel(self.position["x"], self.position["y"], self.red, self.green, self.blue)
            self.position["y"] -= 1
            self.screen.changePixel(self.position["x"], self.position["y"], self.red2, self.green2, self.blue2)
        elif(direction == "left" and self.position["x"] < 32):
            self.screen.changePixel(self.position["x"], self.position["y"], self.red, self.green, self.blue)
            self.position["x"] += 1
            self.screen.changePixel(self.position["x"], self.position["y"], self.red2, self.green2, self.blue2)
        elif(direction == "right" and self.position["x"] > 0):
            self.screen.changePixel(self.position["x"], self.position["y"], self.red, self.green, self.blue)
            self.position["x"] -= 1
            self.screen.changePixel(self.position["x"], self.position["y"], self.red2, self.green2, self.blue2)
            
    def changeColor(self, trailRed, trailGreen, trailBlue, red, green, blue):
        self.red2   = red
        self.red    = trailRed
        self.green2 = green
        self.green  = trailGreen
        self.blue2  = blue
        self.blue   = trailBlue
        self.screen.changePixel(self.position["x"], self.position["y"], self.red2, self.green2, self.blue2)
        
if(__name__ == "__main__"):
    print("Block Class Test")
    print("----------------")
    print("")
    raw_input("Hit ENTER To Have a block randomly move about.")
    system("clear")
    screen = Screen(17, 33)
    block  = Block(screen, 16, 8, 0, 0, 0, 255, 255, 255)
    while(True):
        block.move(choice(["up", "down", "left", "right"]))
        sleep(0.1)