class GameStats:
	# track stats for aliens

	def __init__(self, ai_game):
		# initialize
		self.settings = ai_game.settings
		self.reset_stats()
		self.game_active = True

	def reset_stats(self):
		# initilize stats that can change during the game
		self.ships_left = self.settings.ship_limit