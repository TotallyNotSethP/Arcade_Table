from pixel import Pixel

class Grid:
    def __init__(self, height, width, gpio_pin):
        self.height   = height
        self.width    = width
        self.gpio_pin = gpio_pin
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
    