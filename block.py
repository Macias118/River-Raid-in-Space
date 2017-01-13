import pygame
from colors import *
import random
class Block():
	
	def __init__(self, window, x, y, size):
		self.window = window
		self.x = x
		self.y = y
		self.size = size
		
	def draw(self):
		pygame.draw.rect(self.window, white, (self.x, self.y, self.size, self.size))
		
	