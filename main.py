import pygame
import random
from pygame import gfxdraw
from ship import *
from colors import *
from block import *
pygame.init()

pointz = 0
best_score = 0

black = (0,0,0)
white = (255,255,255)
gray = (100,100,100)

green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
clock = pygame.time.Clock()  

window_width = 1366			#window_weight
window_height = 768
window = pygame.display.set_mode((window_width, window_height), pygame.DOUBLEBUF | pygame.FULLSCREEN )

def message(content, size, x, y):

	text = pygame.font.Font('freesansbold.ttf', size)
	textSurface = text.render(content, True, white)
	textRect = textSurface.get_rect()
	textRect.center = (x,y)
	window.blit(textSurface, textRect)
	
def moveBlocks(array, dy, size, ship):
	
	global pointz
	for bl in array:
		bl.y += dy
		if ship.collision(bl) == True:
			for b in array:
				array.remove(b)
			lose()
		if ship.y >= bl.y - size and ship.y <= bl.y + size:
			pointz += 0.1
		if bl.y > window.get_height():
			bl.y = -size
			bl.x = random.randrange(0, window.get_width())
		bl.draw()

def intro():

	intro = True
	pygame.display.set_caption('Space Invaders')
	pygame.mouse.set_visible(False)
	
	while intro:
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					quit()
				if event.key == pygame.K_1:
					intro = False
					return 1
				elif event.key == pygame.K_2:
					intro = False
					return 2
				elif event.key == pygame.K_3:	
					intro = False
					return 3
				
		window.fill(black)
		message('Press 1,2,3 to START', 70, window_width/2, window_height/2)
		pygame.display.update()

		
		
def lose():
	global best_score
	global pointz
	lose = True
	while lose:
		for event in pygame.event.get():
			if event.type == pygame.QUIT :
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					quit()
				if event.key == pygame.K_r:
					lose = False
					main()
				
		window.fill(black)
		if best_score < pointz:
			best_score = pointz
		message('Best: '+str(best_score), 60, window_width/2, window_height/2)
		message('You scored '+str(pointz)+' points', 60, window_width/2, window_height/2 + 100)
		message('Press R to restart, ESC to exit', 30, window_width/2, window_height/2 + 200)
		
		pygame.display.update()		
		
	pointz = 0
		
def main():


	choice = intro()
	#ship
	ship = Ship(window, window_width/2-200, window_height - 100)
	dx = 0
	
	# stars
	stars = []
	NumberOfStars = 3000
	for s in range(NumberOfStars):
		i = random.randrange(0, window_width)
		j = random.randrange(0, window_height)
		stars.append(i)
		stars.append(j)
	
	#blocks
	block_size = 50
	dy = 5 + choice * 2
	blockCounter = 0
	blocks = []
	NumberOfBlocks = 5
	block_y = -500
	
	if choice == 1:
		difficulty = 5
	elif choice == 2:
		difficulty = 4
	elif choice == 3:
		difficulty = 3
	
	for n in range(0, window_height, difficulty*block_size):
		for i in range(NumberOfBlocks):
			blocks.append(Block(window, random.randrange(0, window.get_width()), block_y, block_size))
		block_y += difficulty*block_size
		
		
	
	while True:
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					quit()
				if event.key == pygame.K_LEFT:
					dx = -10
				if event.key == pygame.K_RIGHT:
					dx = 10
				if event.key == pygame.K_UP:
					dy = 15	
				if event.key == pygame.K_DOWN:
					dy = 3
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					dx = 0
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					dy = 7
				
		# BACKGROUND			
		window.fill(black)
		for i in range(0, NumberOfStars ,2):
			gfxdraw.pixel(window, stars[i], stars[i+1], white)
		message("Points: "+str(pointz), 20, 50, 20)
		
		
		# BLOCK
		moveBlocks(blocks, dy, block_size, ship)
		
		
		# SHIP
		ship.move(dx)
		
		
		
		
		
		pygame.display.update()
		clock.tick( 60 )



main()












