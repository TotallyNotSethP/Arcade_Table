# Import External Functions
from __future__     import print_function
from time           import sleep
from joystick_class import Joystick

js = Joystick(0)
js.inputListener("up",    lambda: print("UP!"))
js.inputListener("down",  lambda: print("DOWN!"))
js.inputListener("left",  lambda: print("LEFT!"))
js.inputListener("right", lambda: print("RIGHT!"))
sleep(10)
js.endListeners()