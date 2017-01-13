import pygame

class Ship():
	
	def __init__(self, window, x, y):
		self.window = window
		self.x = x
		self.y = y
		self.img = pygame.image.load('space.png')
		self.width = 50
		
	def draw(self):
		self.window.blit(self.img, (self.x, self.y))
		
	def move(self, dx):
		if self.x + dx < 0:
			self.x = 0
		elif self.x + dx > self.window.get_width() - self.width:
			self.x = self.window.get_width() - self.width
		else:
			self.x += dx
		self.draw()
		
	def collision(self, block):
		if self.x + self.width >= block.x and self.x <= block.x + block.size:
			if self.y + self.width >= block.y and self.y <= block.y + block.size:
				return True		
		return False
	
		