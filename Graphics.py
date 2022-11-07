from Constants import *
import pygame
pygame.init()

class Circle(pygame.sprite.Sprite):
	def __init__(self, positionX, positionY, color = WHITE) -> None:
		super().__init__()
		self.position = [positionX, positionY]
		self.color = color
		
		self.image = pygame.Surface(self.getScaledDimension())
		self.image.fill(BLUE)
		self.image.set_colorkey(BLUE, pygame.RLEACCEL)
		
		pygame.draw.circle(self.image, self.color, self.getScaledCenter(), CIRCLE_RADIUS)
		self.rect = self.image.get_rect()
		self.setRectToCenter()

	def getScaledDimension(self) -> tuple:
		return (CIRCLE_RADIUS * 2, CIRCLE_RADIUS * 2)
	
	def	getScaledCenter(self) -> tuple:
		return (CIRCLE_RADIUS, CIRCLE_RADIUS)

	def	setRectToCenter(self) -> None:
		circleMaxWidth = SCREEN_WIDTH / GAME_WIDTH
		circleMaxHeight = SCREEN_HEIGHT / GAME_HEIGHT
		scaledX = (circleMaxWidth / 2) + (circleMaxWidth * self.position[X])
		scaledY = (circleMaxHeight / 2) + (circleMaxHeight * self.position[Y])
		self.rect.x = scaledX - CIRCLE_RADIUS
		self.rect.y = scaledY - CIRCLE_RADIUS
		

class Engine():
	all_pieces = {}
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	def __init__(self) -> None:
		self.initScreen()

	def	initScreen(self) -> None:
		self.screen.fill(BLUE)
		for height in range(GAME_HEIGHT):
			for width in range(GAME_WIDTH):
				new_circle = Circle(width, height)
				self.all_pieces[(width, height)] = new_circle
				self.screen.blit(new_circle.image, new_circle.rect)
		pygame.display.flip()
	
	def runGame(self) -> None:
		pygame.event.clear()
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running == False
		pygame.quit()



