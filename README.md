# My Video Game Table
## About
Hello! My name is Seth Peace! My dad and I decided to make a table that you can play games on. This is the software for that table. It's powered by Python and PyGame on a Raspberry Pi 3 B+.
## Status
So far, we have successfully made a Joystick class to read the joysticks. It's in the file `joystick_class.py`.
## Usage
The Joystick class works as follows:
```
js = Joystick(0) # This will initialize the joystick with id 0
js.inputListener("up", lambda: print("hi!")) # This will print "hi!" on joystick up. Other valid first arguments: "down", "left", "right", "a" (mapped to button 1), and "b" (mapped to button 2).
print(js.getInput("up") # This will print "True" if joystick is up and "False" if it isn't. Other vaild first arguments: see above.
```
