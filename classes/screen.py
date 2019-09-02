import pygame, sys
from pygame.locals import *
from threading     import Thread
from time          import sleep
from os            import system
from random        import randint
from .grid         import Grid
from .color        import Color
from board         import D18
from neopixel      import NeoPixel

with open("/home/pi/Arcade_Table/classes/screen_running.txt", "r") as file:
	if(file.read() == "Running"):
		raise SystemError("The screen is already in use somewhere else.")

with open("/home/pi/Arcade_Table/classes/screen_running.txt", "w") as file:
	file.write("Running")

class Screen:
	def __init__(self, grid_height, grid_width, size = 10, sim = False):
		self.grid         = Grid(grid_height, grid_width)
		self.threadEnded  = False
		if(sim):
			def PygameThread(self, grid_height, grid_width):
				width             = grid_width  * size
				height            = grid_height * size
				self.display      = pygame.display.set_mode((width, height))
				self.pixel_width  = int(width/grid_width)
				self.pixel_height = int(height/grid_height)
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
			print("INIT")
			#self.num_pixels = grid_height*grid_width
			#self.pixels     = NeoPixel(D18, self.num_pixels)
			#self.pixels.fill((0,0,0))
			#def ScreenThread(self, grid_height, grid_width):
			#	while(not self.threadEnded):
			#		for x in range(grid_width):
			#			for y in range(grid_height):
			#				h = grid_height-1
			#				if(x%2==0):
			#					newy = h-y
			#				else:
			#					newy = y
			#				index = (x*h)+newy
			#				self.pixels[index] = tuple(self.grid.pixels[x][y])
			#				print(index)
			#		sleep(0.1)
			#thread = Thread(target=ScreenThread, args=(self, grid_height, grid_width))
			#thread.start()
		
	def changePixel(self, x, y, red, green, blue):
		#self.grid.pixels[x][y] = Color(red, green, blue)
		print(str((x, y)) + " PIX CHANGED TO " + str((red, green, blue)))
		
	def endThread(self):
		#self.threadEnded = True
		print("THREAD END")
	
	def deinit(self):
		#self.pixels.fill((0, 0, 0))]
		print("PIX RESET TO BLANK")
		#self.pixels.deinit()
		print("DEINIT")
		with open("/home/pi/Arcade_Table/classes/screen_running.txt", "w") as file:
			file.write("")
		
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
		selection = input("Select one: ")
		system("clear")
		if(int(selection) == 1):
			screen = Screen(17, 33, sim = True)
			for x in range(33):
				for y in range(17):
					screen.changePixel(x, y, randint(0, 255), randint(0, 255), randint(0, 255))
			while(not screen.threadEnded):
				sleep(0.1)
			screen.endThread()
		elif(int(selection) == 2):
			screen = screen = Screen(4, 6, sim = False)
			for x in range(6):
				for y in range(4):
					screen.changePixel(x, y, randint(0, 255), randint(0, 255), randint(0, 255))
			while(True):
				sleep(0.1)
			screen.endThread()
		else:
			print("That's not a valid option.")
	except ValueError:
		print("That's not a number.")
	
	
