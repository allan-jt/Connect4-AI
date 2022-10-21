# Set up pygame: https://realpython.com/pygame-a-primer/
from asyncio import ALL_COMPLETED
from time import sleep
import utils
import random
import pygame
from pygame import (
	K_UP, K_DOWN, K_LEFT, K_RIGHT,
	K_ESCAPE, KEYDOWN, QUIT
)
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_MOVMNT = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create player
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.surf = pygame.Surface((75, 60))
		self.surf.fill(WHITE)
		self.rect = self.surf.get_rect()

	def update(self, key_pressed):
		if key_pressed[K_UP]:
			move = -PLAYER_MOVMNT if self.rect.top >= PLAYER_MOVMNT else 0
			self.rect.move_ip(0, move)
		if key_pressed[K_DOWN]:
			move = PLAYER_MOVMNT if self.rect.bottom <= SCREEN_HEIGHT - PLAYER_MOVMNT else 0
			self.rect.move_ip(0, move)
		if key_pressed[K_LEFT]:
			move = -PLAYER_MOVMNT if self.rect.left >= PLAYER_MOVMNT else 0
			self.rect.move_ip(move, 0)
		if key_pressed[K_RIGHT]:
			move = PLAYER_MOVMNT if self.rect.right <= SCREEN_WIDTH - PLAYER_MOVMNT else 0
			self.rect.move_ip(move, 0)

player = Player()

# Create enemy
class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.surf = pygame.Surface((20, 10))
		self.surf.fill(WHITE)
		self.rect = self.surf.get_rect(
			center = (
				random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
				random.randint(0, SCREEN_WIDTH),
			)
		)
		self.speed = random.randint(5, 20)
	
	def update(self):
		self.rect.move_ip(-self.speed, 0)
		if self.rect.right < 0:
			self.kill()

# Group all sprites
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Set up screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Main loop
running = True
pygame.event.clear()
while running:
	for event in pygame.event.get():
		if (event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == QUIT:
			running = False
	
	key_pressed = pygame.key.get_pressed()
	player.update(key_pressed)
	for entity in enemies:
		entity.update()

	# Update screen
	screen.fill(BLACK)
	for entity in all_sprites:
		screen.blit(entity.surf, entity.rect)
	pygame.display.flip()

pygame.quit()





