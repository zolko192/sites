import sys
import pygame
# 1, Create a character and a game loop.	DONE
# 2, Registering events for your character.
# 3, Let’s make the world a little more interesting by adding a map.
# 4, Adding an inventory to keep track of your resources.
# 5, Adding a crafting system.
# 6, Adding ambient features to your world.
# 7, Adding objectives to our game.
# 8, We are adding to our game.
# 9, Adding saving.
# 10, Adding the objective.
# 11, Adding scoring.

# 2, Registering events for your character. 	WAIT
class Game(object):
	""" Játék létrehozása és konfigurálása """
	def __init__(self):
		# Definiálja a játékos maximum lépéseit
		self.tilesize = 40
		self.mapwidth = 25
		self.mapheight = 15
		# Betölti a játékos karakter képét és pozicióját
		self.player = pygame.image.load("pictures/char.png")
		self.player_pos = [0, 0]

	def player_event(self, event):
		# Játékos karakter mozgása
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT and self.player_pos[0] < self.mapwidth - 1:
				self.player_pos[0] += 1
			if event.key == pygame.K_LEFT and self.player_pos[0] > 0:
				self.player_pos[0] -= 1
			if event.key == pygame.K_DOWN and self.player_pos[1] < self.mapheight - 1:
				self.player_pos[1] += 1
			if event.key == pygame.K_UP and self.player_pos[1] > 0:
				self.player_pos[1] -= 1