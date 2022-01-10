import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats 
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
	# OVERALL CLASS TO MANAGE GAME ASSETS AND BEHAVIOURS

	def __init__(self):
		# INITIALIZE THE GAME, CREATE GAME RESOURCES
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		# create instance to store game stats
		self.stats = GameStats(self)

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

		# BACKGROUND COLOR
		self.bg_color = (230, 230, 230)

	def run_game(self):
		# START MAIN LOOP
		while True:
			self._check_events()

			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_aliens()

			self._update_screen()


	def _check_events(self):
		# WATCH KEYBOARD AND MOUSE EVENTS
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		# RESPOND TO KEYPRESSES
		if event.key == pygame.K_RIGHT:
			# MOVE SHIP TO RIGHT
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			# MOVE SHIP TO LEFT
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		# CREATE NEW BULLET AND ADD TO GROUP
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		# bullets update pos and remove old bullets
		# update pos
		self.bullets.update()

		# GET RID OF OLD BULLETS
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

		self._check_bullet_alien_collisions()

	def _check_bullet_alien_collisions(self):
		
		# check any bullets hitting aliens
		# if so, get rid bullets and aliens
		collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)

		if not self.aliens:
			# destroy existing bullets and create new fleet
			self.bullets.empty()
			self._create_fleet()

	def	_create_fleet(self):
		# create fleet of aliens
		# create one alien and determine # of aliens in a row
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)

		# determine number of rows fit on screen
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
		number_rows = available_space_y // (2 * alien_height)

		# create first row
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)


	def _create_alien(self, alien_number, row_number):
		# create an alien and place it in row
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)

	def _update_aliens(self):
		# update positions of aliens in fleet
		self._check_fleet_edges()
		self.aliens.update()

		# look for alien-ship collisions
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()

		self._check_aliens_bottom()

	def _ship_hit(self):
		# respond to ship hit by alien
		# decrease ships left
		if self.stats.ships_left > 0:
			self.stats.ships_left -= 1

			# get rid of remaining aliens and bulls
			self.aliens.empty()
			self.bullets.empty()

			# create new fleet and center the ship
			self._create_fleet()
			self.ship.center_ship()

			# pause
			sleep(0.5)

		else:
			self.stats.game_active = False

	def _check_aliens_bottom(self):
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				# treat this same as ship hit
				self._ship_hit()
				break

	def _check_fleet_edges(self):
		# if aliens reached edge
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		# drop entire fleet and change direction
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

	def _update_screen(self):
		# REDRAW SCREEN DURING EACH PASS THROUGH LOOP
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)

		# MOST RECENTLY DRAWN SCREEN VISIBLE
		pygame.display.flip()


if __name__ == '__main__':
	# MAKE A GAME INSTANCE AND RUN THE GAME
	ai = AlienInvasion()
	ai.run_game()