from __future__ import print_function
from pygame    import * 
from threading import Thread
from time      import sleep
from os        import system

class Joystick:
    def __init__(self, id_):
        init()
        joystick.init()
        self.joystick = joystick.Joystick(int(id_))
        self.joystick.init()
    
    def inputListener(self, input_, listener):
        self.listener_end = False
        def inputThread(self, input_, listener):
            input_ = input_.lower()
            while(not self.listener_end): 
                event.pump()
                if((input_ == "up"    and self.joystick.get_axis(0) > 0) or
                   (input_ == "down"  and self.joystick.get_axis(0) < 0) or
                   (input_ == "left"  and self.joystick.get_axis(1) < 0) or 
                   (input_ == "right" and self.joystick.get_axis(1) > 0) or 
                   (input_ == "a"     and self.joystick.get_button(0))   or 
                   (input_ == "b"     and self.joystick.get_button(1))): 
                    listener()
                sleep(0.1)
        thread = Thread(target=inputThread, args=(self, input_, listener))
        thread.start()
        
    def getInput(self, input_):
        input_ = input_.lower()
        event.pump()
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
    js0 = Joystick(0)
    js1 = Joystick(1)
    system("clear")
    print("Joystick Class Test")
    print("-------------------")
    print("")
    print("Which would you like to do?")
    print("(1) inputListener Function Test")
    print("(2) getInput Function Test")
    print("")
    try:
        selection = raw_input("Select one: ")
        system("clear")
        if(int(selection) == 1):
            try:
                system("clear")
                js0.inputListener("up",    lambda: print("UP0!"))
                js0.inputListener("down",  lambda: print("DOWN0!"))
                js0.inputListener("left",  lambda: print("LEFT0!"))
                js0.inputListener("right", lambda: print("RIGHT0!"))
                js0.inputListener("a",     lambda: print("A0!"))
                js0.inputListener("b",     lambda: print("B0!"))
                js1.inputListener("up",    lambda: print("UP1!"))
                js1.inputListener("down",  lambda: print("DOWN1!"))
                js1.inputListener("left",  lambda: print("LEFT1!"))
                js1.inputListener("right", lambda: print("RIGHT1!"))
                js1.inputListener("a",     lambda: print("A1!"))
                js1.inputListener("b",     lambda: print("B1!"))
                sleep(10)
            except KeyboardInterrupt:
                sleep(0)
            js0.endListeners()
            js1.endListeners()
            system("clear")
        elif(int(selection) == 2):
            try:
                i = 0
                while(i != 100):
                    system("clear")
                    print("Up0: "    + str(js0.getInput("up")))
                    print("Down0: "  + str(js0.getInput("down")))
                    print("Left0: "  + str(js0.getInput("left")))
                    print("Right0: " + str(js0.getInput("right")))
                    print("A0: "     + str(js0.getInput("a")))
                    print("B0: " + str(js0.getInput("b")))
                    print("Up1: " + str(js1.getInput("up")))
                    print("Down1: " + str(js1.getInput("down")))
                    print("Left1: " + str(js1.getInput("left")))
                    print("Right1: " + str(js1.getInput("right")))
                    print("A1: " + str(js1.getInput("a")))
                    print("B1: " + str(js1.getInput("b")))
                    sleep(0.1)
                    i += 1
            except KeyboardInterrupt:
                sleep(0)
            system("clear")
        else:
            print("That's not a valid option.")
    except NameError:
        system("clear")
        print("That's not a number.")
        