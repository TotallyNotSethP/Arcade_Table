# Import External Functions
import pygame, colorama, os

# Define Internal Functions
def info(string):
    '''
Print Information To The Console
    '''
    print(colorama.Fore.BLUE + "INFO: " + string)
def error(string):
    '''
Print An Error To The Console
    '''
    print(colorama.Fore.RED + "ERROR: " + string)
def warning(string):
    '''
Print A Warning To The Console
    '''
    print(colorama.Fore.ORANGE + "WARNING: " + string)

# Set Up Colorama
print(colorama.Style.BRIGHT)
os.system("clear")

# Get Joystick Count
pygame.joystick.init()
numJoysticks = pygame.joystick.get_count()

# Alert The User That The Program Has Started
info("Program Initiated")

# Check That There Are 2 Joysticks Connected
if(numJoysticks != 2):
    error("Incorrect Joystick Number. Expected: 2, Connected: {}".format(numJoysticks))
else:
    info("2 Joysticks Connected")

    # Create Joystick Objects
    js0 = pygame.joystick.Joystick(0)
    js0.init()
    info("Joystick 0: " + str(js0))
    js1 = pygame.joystick.Joystick(1)
    js1.init()
    info("Joystick 1: " + str(js1))

    # Check Which Joystick Is Black
    if(js0.get_button(2) == True):
        info("Joystick 0: Black Joystick")
        info("Joystick 1: White Joystick")
        black = js0
        white = js1
    elif(js1.get_button(2) == True):
        info("Joystick 0: Joystick")
        info("Joystick 1: Black Joystick")
        white = js0
        black = js1
    else:
        error("No Signal on Black Joystick, Button Port 2")

# Alert The User The Program Has Ended
info("Program Ended")