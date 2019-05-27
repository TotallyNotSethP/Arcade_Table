from classes.screen   import Screen
from classes.joystick import Joystick
from time             import sleep
from os               import system

class Cursor:
    def __init__(self, screen, starting_x, starting_y, trailRed, trailGreen, trailBlue, red, green, blue):
        self.red      = red
        self.red2     = trailRed
        self.green    = green
        self.green2   = trailGreen
        self.blue     = blue
        self.blue2    = trailBlue
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

def alt_draw(cursor):
    global color
    if(cursor.red == 255 or cursor.green == 255 or cursor.blue == 255):
        cursor.changeColor(  0,   0,   0,  64,  64,  64)
    else:
        if(color == "white"):
            cursor.changeColor(255, 255, 255, 127, 127, 127)
        elif(color == "red"):
            cursor.changeColor(255,   0,   0, 127,   0,   0)
        elif(color == "green"):
            cursor.changeColor(  0, 255,   0,   0, 127,   0)
        else:
            cursor.changeColor(  0,   0, 255,   0,   0, 127)

def alt_colors(cursor):
    global color
    if(cursor.red == 255 and cursor.green == 255 and cursor.blue == 255):
        cursor.changeColor(255,   0,   0, 127,   0,   0)
        color = "red"
    elif(cursor.red == 255):
        cursor.changeColor(  0, 255,   0,   0, 127,   0)
        color = "green"
    elif(cursor.green == 255):
        cursor.changeColor(  0,   0, 255,   0,   0, 127)
        color = "blue"
    elif(cursor.blue == 255):
        cursor.changeColor(255, 255, 255, 127, 127, 127)
        color = "white"

def drawing_game():
    screen   = Screen(17, 33, height = 300)
    cursor   = Cursor(screen, 16, 8, 127, 127, 127, 255, 255, 255)
    joystick = Joystick(0)
    color    = "white"
    
    try:
        system("clear")
        joystick.inputListener("up",    lambda: cursor.move("up"))
        joystick.inputListener("down",  lambda: cursor.move("down"))
        joystick.inputListener("left",  lambda: cursor.move("left"))
        joystick.inputListener("right", lambda: cursor.move("right"))
        joystick.inputListener("a",     lambda: alt_draw(cursor))
        joystick.inputListener("b",     lambda: alt_colors(cursor))
        while(not screen.threadEnded):
            sleep(0.1)
    except:
        sleep(0)
        
    joystick.endListeners()
    system("clear")

if(__name__ == "__main__"):
    drawing_game()
