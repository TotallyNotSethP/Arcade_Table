from time import sleep # This function causes the program to wait a specified amount of seconds. 
from joystick_class import Joystick # This class reads the data from the joysticks.
from os import system # This function runs a bash command.

try: # This gets ready to catch exceptions.
    js0 = Joystick(0) # This initializes Joystick 0.
    js1 = Joystick(1) # This initializes Joystick 1.
    i = 0 # This initializes the index variable.
    while(i != 100): # This loops 100 times.
        system("clear") # This clears the screen.
        print("Up0: " + str(js0.getInput("up"))) # This prints "True" on joystick up.
        print("Down0: " + str(js0.getInput("down"))) # This prints "True" on joystick down.
        print("Left0: " + str(js0.getInput("left"))) # This prints "True" on joystick left.
        print("Right0: " + str(js0.getInput("right"))) # This prints "True" on joystick right.
        print("A0: " + str(js0.getInput("a"))) # This prints "True" on button a.
        print("B0: " + str(js0.getInput("b"))) # This prints "True" on button b.
        print("Up1: " + str(js1.getInput("up"))) # This prints "True" on joystick up.
        print("Down1: " + str(js1.getInput("down"))) # This prints "True" on joystick down.
        print("Left1: " + str(js1.getInput("left"))) # This prints "True" on joystick left.
        print("Right1: " + str(js1.getInput("right"))) # This prints "True" on joystick right.
        print("A1: " + str(js1.getInput("a"))) # This prints "True" on button a.
        print("B1: " + str(js1.getInput("b"))) # This prints "True" on button b.
        sleep(0.1) # This waits 1/10 of a second so the CPU isn't overloaded.
        i += 1 # This increases the index.
except: # This catches excpetions.
    print(0) # This does nothing.
system("clear") # This clears the screen.