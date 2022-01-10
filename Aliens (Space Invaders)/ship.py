import pygame

class Ship:
	# TO MANAGE SHIP
	def __init__(self, ai_game):

		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# LOAD SHIP IMAGE AND GET ITS RECT
		images_path = 'C:/Users/silvas5/Desktop/COSAS MÍAS/+SUBLIME/python_projects/aliens/images'
		self.image = pygame.image.load(images_path + '/alien2.png')
		self.rect = self.image.get_rect()

		# START EACH SHIP AT BOTTOM CENTER OF SCREEN
		self.rect.midbottom = self.screen_rect.midbottom

		# STORE DECIMAL VALUE FOR SHIP HORIZ POSIT
		self.x = float(self.rect.x)

		# MOVEMENT FLAG
		self.moving_right = False
		self.moving_left = False

	def update(self):
		# UPDATE SHIP POSITION BASED ON MOVEMENT FLAG
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		# UPDATE RECT OBJ FROM SELF X
		self.rect.x = self.x

	def blitme(self):
		# DRAW SHIP AT CURRENT LOCATION
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)