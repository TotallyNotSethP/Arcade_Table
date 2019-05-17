from __future__ import print_function # This function prints to the screen. The __future__ version is used in lambdas.
from time import sleep # This function causes the program to wait a specified amount of seconds. 
from joystick_class import Joystick # This class reads the data from the joysticks.
from os import system # This function runs a bash command.

try: # This gets ready to catch exceptions.
    system("clear") # This clears the screen.
    js0 = Joystick(0) # This initializes joystick 0.
    js0.inputListener("up", lambda: print("UP0!")) # This prints a message on joystick up.
    js0.inputListener("down", lambda: print("DOWN0!")) # This prints a message on joystick down.
    js0.inputListener("left", lambda: print("LEFT0!")) # This prints a message on joystick left.
    js0.inputListener("right", lambda: print("RIGHT0!")) # This prints a message on joystick right.
    js0.inputListener("a", lambda: print("A0!")) # This prints a message on a button.
    js0.inputListener("b", lambda: print("B0!")) # This prints a message on b button.
    js1 = Joystick(1) # This initializes joystick 1.
    js1.inputListener("up", lambda: print("UP1!")) # This prints a message on joystick up.
    js1.inputListener("down", lambda: print("DOWN1!")) # This prints a message on joystick down.
    js1.inputListener("left", lambda: print("LEFT1!")) # This prints a message on joystick left.
    js1.inputListener("right", lambda: print("RIGHT1!")) # This prints a message on joystick right.
    js1.inputListener("a", lambda: print("A1!")) # This prints a message on a button.
    js1.inputListener("b", lambda: print("B1!")) # This prints a message on b button.
    sleep(10) # This waits 10 seconds.
except: # This catches excpetions.
    print(0) # This does nothing.
js0.endListeners() # This ends the listeners (so the threads end and the program will exit).
js1.endListeners() # This ends the listeners (so the threads end and the program will exit).
system("clear") # This clears the screen.