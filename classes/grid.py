from .color import Color
from os     import system

class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width  = width
        self.reset()
        
    def reset(self):
        self.pixels   = []
        for x in range(self.width):
            self.pixels.append([])
            for y in range(self.height):
                self.pixels[x].append(Color())
                
    def __str__(self):
        to_return = ""
        for x in range(self.width):
            for y in range(self.height):
                to_return = to_return + str(self.pixels[x][y]);
            to_return = to_return + "\n"
        return to_return
                
if(__name__ == "__main__"):
    grid = Grid(33, 17)
    system("clear")
    print("Grid Class Test")
    print("---------------")
    print("")
    raw_input("Hit ENTER to test __str__ with a 33x17 grid.")
    system("clear")
    print(str(grid))
    