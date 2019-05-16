from __future__ import print_function # This function prints to the screen. The __future__ version is used in lambdas.
from time import sleep # This function causes the program to wait a specified amount of seconds. 
from joystick_class import Joystick # This class reads the data from the joysticks.
from os import system # This function runs a bash command.

# ".inputListener" method (uncomment to try)

#try: # This gets ready to catch exceptions.
#    system("clear") # This clears the screen.
#    js = Joystick(0) # This initializes joystick 0.
#    js.inputListener("up", lambda: print("UP!")) # This prints a message on joystick up.
#    js.inputListener("down", lambda: print("DOWN!")) # This prints a message on joystick down.
#    js.inputListener("left", lambda: print("LEFT!")) # This prints a message on joystick left.
#    js.inputListener("right", lambda: print("RIGHT!")) # This prints a message on joystick right.
#    js.inputListener("a", lambda: print("A!")) # This prints a message on a button.
#    js.inputListener("b", lambda: print("B!")) # This prints a message on b button.
#except: # This catches excpetions.
#    sleep(0) # This acts as a placeholder (so Python won't get mad at an empty "except:"). It doesn't do anything.
#js.endListeners() # This ends the listeners (so the threads end and the program will exit).
#system("clear") # This clears the screen.

# ".getInput" method (uncomment to try)

#try: # This gets ready to catch exceptions.
#    js = Joystick(0)
#    while(True):
#        system("clear") # This clears the screen.
#        print("Up: " + str(js.getInput("up"))) # This prints "True" on joystick up.
#        print("Down: " + str(js.getInput("down"))) # This prints "True" on joystick down.
#        print("Left: " + str(js.getInput("left"))) # This prints "True" on joystick left.
#        print("Right: " + str(js.getInput("right"))) # This prints "True" on joystick right.
#        print("A: " + str(js.getInput("a"))) # This prints "True" on button a.
#        print("B: " + str(js.getInput("b"))) # This prints "True" on button b.
#        sleep(0.1) # This waits 1/10 of a second so the CPU isn't overloaded.
#except: # This catches excpetions.
#    sleep(0) # This acts as a placeholder (so Python won't get mad at an empty "except:"). It doesn't do anything.
#system("clear") # This clears the screen.