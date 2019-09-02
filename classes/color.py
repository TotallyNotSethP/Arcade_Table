from os import system

class Color:
    def __init__(self, red = 0, green = 0, blue = 0):
        self.red   = red
        self.green = green
        self.blue  = blue
        
    def __str__(self):
        return str((self.red, self.green, self.blue))
    
    def __iter__(self):
        yield self.red
        yield self.green
        yield self.blue
    
if(__name__ == "__main__"):
    pixel = Pixel()
    system("clear")
    print("Pixel Class Test")
    print("---------------")
    print("")
    raw_input("Hit ENTER to test __str__.")
    system("clear")
    print(str(pixel))
    