from Minimax import *
import pygame
import time
pygame.init()

class Circle(pygame.sprite.Sprite):
	def __init__(self, positionX: int, positionY: int, color: tuple = WHITE) -> None:
		super().__init__()
		self.position = (positionX, positionY)
		self.color = color
		
		self.image = pygame.Surface(self.getScaledDimension()).convert_alpha()
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
	
	def update(self) -> None:
		pygame.draw.circle(self.image, self.color, self.getScaledCenter(), CIRCLE_RADIUS)
		
class Engine():
	def __init__(self) -> None:
		self.sprite_group = pygame.sprite.Group()
		self.all_pieces = {}
		self.board = {}
		self.current_color = YELLOW
		self.initScreen()

	def	initScreen(self) -> None:
		self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		self.screen.fill(BLUE)
		for height in range(GAME_HEIGHT):
			for width in range(GAME_WIDTH):
				new_circle = Circle(width, height)
				self.sprite_group.add(new_circle)
				self.all_pieces[(width, height)] = new_circle
				self.board[(width, height)] = WHITE
				self.screen.blit(new_circle.image, new_circle.rect)
		pygame.display.flip()
	
	def runGame(self) -> None:
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				if event.type == pygame.MOUSEBUTTONDOWN:
					self.click = True
			
			if not self.play():
				running = False
			self.click = False
		pygame.quit()

	def updateScreen(self) -> None:
		for piece in self.sprite_group:
			piece.update()
			self.screen.blit(piece.image, piece.rect)
		pygame.display.flip()
	
	def play(self) -> bool:
		if self.current_color == RED:
			return self.AI_play()
		if not pygame.mouse.get_pressed()[0] or not self.click:
			return True
		
		return self.player_play()
	
	def	AI_play(self) -> bool:
		print("\rI'm thinking     ", end="")
		ai_position, val = minimax(copy_dict(self.board), RED, -INFINITY, INFINITY)
		self.all_pieces[ai_position].color = RED
		self.board[ai_position] = RED
		self.current_color = swap_color(self.current_color)
		self.updateScreen()
		print("\rI've made my move", end="")

		if check_win(self.board, ai_position, RED):
			print("\nYou loose!")
			time.sleep(10)
			return False
		return True
	
	def	player_play(self) -> bool:
		position = pygame.mouse.get_pos()
		width = position[X] // (SCREEN_WIDTH / GAME_WIDTH)

		for height in range(GAME_HEIGHT - 1, -1, -1):
			piece = self.all_pieces[(width, height)]
			if piece.color != WHITE:
				continue
			piece.color = self.current_color
			self.board[piece.position] = self.current_color
			self.updateScreen()
			if check_win(self.board, (width, height), piece.color):
				print("\nYou win")
				time.sleep(10)
				return False
			self.current_color = swap_color(self.current_color)
			break

		return True