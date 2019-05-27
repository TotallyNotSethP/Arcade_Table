from __future__ import print_function
import pygame
from threading  import Thread
from time       import sleep
from os         import system

class Joystick:
    def __init__(self, id_):
        pygame.init()
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(int(id_))
        self.joystick.init()
    
    def inputListener(self, input_, listener):
        self.listener_end = False
        def inputThread(self, input_, listener):
            input_ = input_.lower()
            try:
                while(not self.listener_end): 
                    pygame.event.pump()
                    if((input_ == "up"    and self.joystick.get_axis(0) > 0) or
                       (input_ == "down"  and self.joystick.get_axis(0) < 0) or
                       (input_ == "left"  and self.joystick.get_axis(1) < 0) or 
                       (input_ == "right" and self.joystick.get_axis(1) > 0)): 
                        listener()
                    elif(input_ == "a" and self.joystick.get_button(0)):
                        listener()
                        while(self.joystick.get_button(0)):
                            sleep(0.1)
                    elif(input_ == "b" and self.joystick.get_button(1)):
                        listener()
                        while(self.joystick.get_button(1)):
                            sleep(0.1)
                    sleep(0.1)
            except:
                sleep(0)
        thread = Thread(target=inputThread, args=(self, input_, listener))
        thread.start()
        
    def getInput(self, input_):
        input_ = input_.lower()
        pygame.event.pump()
        if((input_ == "up"    and self.joystick.get_axis(0) > 0) or
           (input_ == "down"  and self.joystick.get_axis(0) < 0) or 
           (input_ == "left"  and self.joystick.get_axis(1) < 0) or 
           (input_ == "right" and self.joystick.get_axis(1) > 0) or 
           (input_ == "a"     and self.joystick.get_button(0))   or 
           (input_ == "b"     and self.joystick.get_button(1))): 
            return True
        else:
            return False
        
    def endListeners(self):
        self.listener_end = True
        
if(__name__ == "__main__"):
    joystick0 = Joystick(0)
    joystick1 = Joystick(1)
    system("clear")
    print("Joystick Class Test")
    print("-------------------")
    print("")
    print("Which would you like to test?")
    print("(1) inputListener")
    print("(2) getInput")
    print("")
    try:
        selection = raw_input("Select one: ")
        system("clear")
        if(int(selection) == 1):
            try:
                system("clear")
                joystick0.inputListener("up",    lambda: print("UP0!"))
                joystick0.inputListener("down",  lambda: print("DOWN0!"))
                joystick0.inputListener("left",  lambda: print("LEFT0!"))
                joystick0.inputListener("right", lambda: print("RIGHT0!"))
                joystick0.inputListener("a",     lambda: print("A0!"))
                joystick0.inputListener("b",     lambda: print("B0!"))
                joystick1.inputListener("up",    lambda: print("UP1!"))
                joystick1.inputListener("down",  lambda: print("DOWN1!"))
                joystick1.inputListener("left",  lambda: print("LEFT1!"))
                joystick1.inputListener("right", lambda: print("RIGHT1!"))
                joystick1.inputListener("a",     lambda: print("A1!"))
                joystick1.inputListener("b",     lambda: print("B1!"))
                while(True):
                    sleep(0.1)
            except KeyboardInterrupt:
                sleep(0)
            joystick0.endListeners()
            joystick1.endListeners()
            system("clear")
        elif(int(selection) == 2):
            try:
                while(True):
                    system("clear")
                    print("Up0: "    + str(joystick0.getInput("up")))
                    print("Down0: "  + str(joystick0.getInput("down")))
                    print("Left0: "  + str(joystick0.getInput("left")))
                    print("Right0: " + str(joystick0.getInput("right")))
                    print("A0: "     + str(joystick0.getInput("a")))
                    print("B0: " + str(joystick0.getInput("b")))
                    print("Up1: " + str(joystick1.getInput("up")))
                    print("Down1: " + str(joystick1.getInput("down")))
                    print("Left1: " + str(joystick1.getInput("left")))
                    print("Right1: " + str(joystick1.getInput("right")))
                    print("A1: " + str(joystick1.getInput("a")))
                    print("B1: " + str(joystick1.getInput("b")))
                    sleep(0.1)
            except KeyboardInterrupt:
                sleep(0)
            system("clear")
        else:
            print("That's not a valid option.")
    except ValueError:
        system("clear")
        print("That's not a number.")
        