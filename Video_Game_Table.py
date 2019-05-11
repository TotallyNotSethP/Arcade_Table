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
info("The program has started.")

# Check That There Are 2 Joysticks Connected
if(numJoysticks < 2):
    error("Not enough joysticks connected. Expected: 2, Connected: {}.".format(numJoysticks))
elif(numJoysticks > 2):
    error("Too many joysticks connected. Expected: 2, Connected: {}.".format(numJoysticks))
else:
    info("2 joysticks connected.")
    
