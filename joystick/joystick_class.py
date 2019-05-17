from pygame import * # These functions read the joystick data
from threading import Thread # This class creates a thread.
from time import sleep # This function causes the program to wait a specified amount of seconds. 

class Joystick: # This class reads the data from the joysticks.
    def __init__(self, id_): # This function runs when the class initializes.
        init() # This prepares pygame to read events.
        joystick.init() # This prepares pygame to read joystick events.
        self.joystick = joystick.Joystick(int(id_)) # This tells pygame what joystick we want to read data from.
        self.joystick.init() # This prepares pygame to read this joystick's events
    
    def inputListener(self, input_, listener): # This function runs a lambda when certain input is recieved.
        self.listener_end = False # This makes sure that the thread won't die when it starts.
        def inputThread(self, input_, listener): # This function acts as the container of the alternate thread's contents.
            input_ = input_.lower() # This makes sure that there are no capital letters in the input.
            while(not self.listener_end): # This loops the if statement until the listeners are ended.
                event.pump() # This gets all current joystick events from pygame.
                if((input_ == "up" and self.joystick.get_axis(0) > 0) or # This checks if the user asked for joystick up and the joystick is up.
                   (input_ == "down" and self.joystick.get_axis(0) < 0) or # This checks if the user asked for joystick down and the joystick is down.
                   (input_ == "left" and self.joystick.get_axis(1) < 0) or # This checks if the user asked for joystick left and the joystick is left.
                   (input_ == "right" and self.joystick.get_axis(1) > 0) or # This checks if the user asked for joystick right and the joystick is right.
                   (input_ == "a" and self.joystick.get_button(0)) or # This checks if the user asked for button a and the button a is pressed.
                   (input_ == "b" and self.joystick.get_button(1))): # This checks if the user asked for button b and the button b is pressed.
                    listener() # This runs the lambda if any of the above is true.
                sleep(0.1) # This waits 1/10 of a second so it doesn'r overload the CPU.
        thread = Thread(target=inputThread, args=(self, input_, listener)) # This creates a thread.
        thread.start() # This starts the thread.
        
    def getInput(self, input_): # This function returns the current input from any input point on the joystick.
        input_ = input_.lower() # This makes sure that there are no capital letters in the input.
        event.pump() # This gets all current joystick events from pygame.
        if((input_ == "up" and self.joystick.get_axis(0) > 0) or # This checks if the user asked for joystick up and the joystick is up.
           (input_ == "down" and self.joystick.get_axis(0) < 0) or # This checks if the user asked for joystick down and the joystick is down.
           (input_ == "left" and self.joystick.get_axis(1) < 0) or # This checks if the user asked for joystick left and the joystick is left.
           (input_ == "right" and self.joystick.get_axis(1) > 0) or # This checks if the user asked for joystick right and the joystick is right.
           (input_ == "a" and self.joystick.get_button(0)) or # This checks if the user asked for button a and the button a is pressed.
           (input_ == "b" and self.joystick.get_button(1))): # This checks if the user asked for button b and the button b is pressed.
            return True # This returns true if any of the above are true.
        else: # This checks if none of the above are true.
            return False # This returns false if none of the above are true.
        
    def endListeners(self): # This function ends all of the listeners.
        self.listener_end = True # This ends all of the listeners.