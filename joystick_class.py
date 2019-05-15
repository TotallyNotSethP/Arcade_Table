import pygame, threading, time

class Joystick:
    
    program_end = False
    
    def __init__(self, id_):
        pygame.init()
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(int(id_))
        self.joystick.init()
        print("Joystick " + str(id_) + " Has Been Initialized As " + str(self.joystick))
    
    def inputListener(self, direction, listener):
        def inputThread(self, direction, listener):
            direction = direction.lower()
            while(not self.program_end):
                pygame.event.pump()
                if((direction == "up"    and self.joystick.get_axis(0) > 0) or
                   (direction == "down"  and self.joystick.get_axis(0) < 0) or
                   (direction == "left"  and self.joystick.get_axis(1) < 0) or
                   (direction == "right" and self.joystick.get_axis(1) > 0)):
                    listener()
                time.sleep(0.1)
        thread = threading.Thread(target=inputThread, args=(self, direction, listener))
        thread.start()
        
    def endListeners(self):
        self.program_end = True