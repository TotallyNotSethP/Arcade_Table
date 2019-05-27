from classes.screen   import Screen
from classes.joystick import Joystick
from classes.block    import Block
from time             import sleep
from os               import system

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
    global color
    screen   = Screen(17, 33)
    cursor   = Block(screen, 16, 8, 127, 127, 127, 255, 255, 255)
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
