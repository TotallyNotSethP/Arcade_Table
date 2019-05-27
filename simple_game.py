from __future__       import print_function
from classes.screen   import Screen
from classes.joystick import Joystick
from classes.block    import Block
from os               import system
from time             import sleep
            
def simple_game():
    screen   = Screen(17, 33)
    joystick = Joystick(0)
    avatar   = Block(screen, 16, 8, 255, 255, 255, 0, 0, 0)
    
    try:
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
