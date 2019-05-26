import pygame, sys
from pygame.locals import *
from threading     import Thread
from time          import sleep
from os            import system
from random        import randint
from grid          import Grid
from color         import Color

class Screen:
    def __init__(self, grid_height, grid_width, height = 500, width = 500, sim = True):
        self.display      = pygame.display.set_mode((width, height))
        self.grid         = Grid(grid_height, grid_width)
        self.pixel_width  = int(width/grid_width)
        self.pixel_height = int(height/grid_height)
        self.threadEnded  = False
        if(sim):
            def PygameThread(self, grid_height, grid_width):
                self.display.fill((255, 255, 255))
                pygame.display.set_caption("Simulated Grid Output")
                pygame.init()
                
                while(not self.threadEnded):
                    for x in range(grid_width):
                        for y in range(grid_height):
                            pixel = self.grid.pixels[x][y]
                            pygame.draw.rect(self.display,
                                             (pixel.red, pixel.green, pixel.blue),
                                             (self.pixel_width*x, self.pixel_height*y, self.pixel_width, self.pixel_height))
                    for event in pygame.event.get():
                        if(event.type == QUIT):
                            pygame.quit()
                            self.threadEnded = True
                            sys.exit()
                    pygame.display.update()
                
            thread = Thread(target=PygameThread, args=(self, grid_height, grid_width))
            thread.start()
        else:
            print("Physical output is not currently supported.")
        
    def changePixel(self, x, y, red, green, blue):
        self.grid.pixels[x][y] = Color(red, green, blue)
        
    def endThread(self):
        self.threadEnded = True
        
if(__name__ == "__main__"):
    system("clear")
    print("Screen Class Test")
    print("-----------------")
    print("")
    print("Which would you like to test (w/ grid size 33x17)?")
    print("(1) Simulated Grid Output")
    print("(2) Physical Grid Output")
    print("")
    try:
        selection = raw_input("Select one: ")
        system("clear")
        if(int(selection) == 1):
            screen = Screen(17, 33, height = 400, sim = True)
            for x in range(33):
                for y in range(17):
                    screen.changePixel(x, y, randint(0, 255), randint(0, 255), randint(0, 255))
            while(True):
                sleep(0.1)
            screen.endThread()
        elif(int(selection) == 2):
            screen = screen = Screen(17, 33, sim = False)
            for x in range(33):
                for y in range(17):
                    screen.changePixel(x, y, randint(0, 255), randint(0, 255), randint(0, 255))
            while(True):
                sleep(0.1)
            screen.endThread()
        else:
            print("That's not a valid option.")
    except ValueError:
        print("That's not a number.")
        