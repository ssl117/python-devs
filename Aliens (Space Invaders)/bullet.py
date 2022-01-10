import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	# CLASS TO MANAGE BULLETS FROM SHIP

	def __init__(self, ai_game):
		# CREATE BULLET OBJ AT SHIP CURRENT POSITION
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color

		# CREATE BULLET RECT AT (0,0) and then set correct position.
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop

		# STORE BULLET POSITION DECIMAL VALUE
		self.y = float(self.rect.y)

	def update(self):
		# MOVE BULLET UP SCREEN
		# UPDATE decimal position of bullet
		self.y -= self.settings.bullet_speed
		# Update the rect position
		self.rect.y = self.y

	def draw_bullet(self):
		# draw the bullet to the screen
		pygame.draw.rect(self.screen, self.color, self.rect)