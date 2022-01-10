class Settings:
	# A CLASS TO STORE ALL SETTINGS IN PYTHON
	def __init__(self):
		# INITIALIZE THE GAME'S SETTINGS
		# SCREEN SETTINGS
		self.screen_width = 800
		self.screen_height = 400
		self.bg_color = (230, 230, 230)

		# SHIP SETTINGS
		self.ship_speed = 1.5
		self.ship_limit = 3

		# BULLET SETTINGS
		self.bullet_speed = 1.0
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		# ALIENS SETTINGS
		self.alien_speed = 0.5
		self.fleet_drop_speed = 1
		# fleet_direction of 1 represents right, -1 left
		self.fleet_direction = 0.5