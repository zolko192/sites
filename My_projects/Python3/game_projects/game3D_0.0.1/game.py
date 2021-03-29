import sys
import pygame
import random
# 1, Create a character and a game loop. 	DONE
# 2, Registering events for your character. 	DONE
# 3, Let’s make the world a little more interesting by adding a map. 	DONE
# 4, Adding an inventory to keep track of your resources. 	DONE
# 5, Adding a crafting system. 	DONE
# 6, Adding ambient features to your world. 	WAIT
# 7, Adding objectives to our game. 	WAIT
# 8, We are adding to our game. 	WAIT
# 9, Adding saving. 	WAIT
# 10, Adding the objective. 	WAIT
# 11, Adding scoring. 	WAIT

# 6, Adding ambient features to your world. 	WAIT
class Game(object):
	""" Játék létrehozása és konfigurálása """
	def __init__(self):
		# Definiálja a játékos maximum lépéseit
		self.tilesize = 40
		self.mapwidth = 25
		self.mapheight = 15

		# Definiálj a játékos nyersanyagait
		self.dirt, self.grass, self.water, self.coal, self.cloud, self.wood = 0, 1, 2, 3, 4, 5
		self.fire, self.sand, self.glass, self.rock, self.stone, self.brick, self.diamond = 6, 7, 8, 9, 10, 11, 12
		
		# Declare resources for inventory interface
		self.resources = [self.dirt, self.grass, self.water, self.coal, self.wood, self.fire, self.sand, self.glass, self.rock, self.stone, self.brick, self.diamond]

		# intialize an inventory
		# empty when starting
		self.inventory = {
			self.dirt: 0, 
			self.grass: 0,
			self.water: 0, 
			self.coal: 0,
			self.wood: 0,
			self.fire: 0,
			self.sand: 0,
			self.glass: 0,
			self.rock: 0, 
			self.stone: 0,
			self.brick: 0, 
			self.diamond: 0
		}

		# add controls for crafting
		# these numbers correspond to
		# number keys 1,2,...0, -, =
		self.controls = {
			self.dirt: 49, # 1
			self.grass: 50, # 2
			self.water: 51, # 3
			self.coal: 52, # 4
			self.wood: 53, # 5
			self.fire: 54, # 6
			self.sand: 55, # 7
			self.glass: 56, # 8
			self.rock: 57, # 9
			self.stone: 48, # 0
			self.brick: 45, # -
			self.diamond: 61 # =
		}

		# this tells us how many or each resource
		# we need to produce a more valuable resource
		# so 1 stone takes 1 rock
		self.craft = {
			self.stone: {self.rock: 1},
			self.sand: {self.rock: 1},
			self.fire: {self.wood: 1},
			self.glass: {self.fire: 1, self.sand: 1},
			self.diamond: {self.wood: 1, self.coal: 1},
			self.brick: {self.rock: 1, self.fire: 1}
		}

		# Importálja a képeket objektummá
		self.textures = {
			self.dirt: pygame.image.load("pictures/dirt.png"),
			self.grass: pygame.image.load("pictures/grass.png"),
			self.water: pygame.image.load("pictures/water.png"),
			self.coal: pygame.image.load("pictures/coal.png"),
			self.cloud: pygame.image.load("pictures/cloud.png"),
			self.wood: pygame.image.load("pictures/wood.png"),
			self.fire: pygame.image.load("pictures/fire.png"),
			self.sand: pygame.image.load("pictures/sand.png"),
			self.glass: pygame.image.load("pictures/glass.png"),
			self.rock: pygame.image.load("pictures/rock.png"),
			self.stone: pygame.image.load("pictures/stone.png"),
			self.brick: pygame.image.load("pictures/brick.png"),
			self.diamond: pygame.image.load("pictures/diamond.png")
		}

		# Betölti a játékos karakter képét és pozicióját
		self.player = pygame.image.load("pictures/char.png")
		self.player_pos = [0, 0]
		self.map_resources()

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
			if event.key == pygame.K_SPACE:
				# Store the current tile.
				self.current_tile = self.tilemap[self.player_pos[1]][self.player_pos[0]]
				# Add one of that resource to the inventory.
				self.inventory[self.current_tile] += 1
				# Replace the tile on the ground with dirt.
				self.tilemap[self.player_pos[1]][self.player_pos[0]] = self.dirt
			# We go through all our number keys
			for key in self.controls:
				# if one was pressed by the player
				if event.key == self.controls[key]:
					# if the mouse key was pressed in addition
					if pygame.mouse.get_pressed()[0]:
						# if this is a craftable resource
						if key in self.craft:
							# check that we have enough 
                            # ingredients to make the resource
							self.done = True
							for self.i in self.craft[key]:
								if self.craft[key][self.i] > self.inventory[self.i]:
									self.done = False
									break
							# if we can make the resource
                            # craft it and add it to our
                            # inventory
							if self.done == True:
								for self.i in self.craft[key]:
									self.inventory[self.i] -= self.craft[key][self.i]
								self.inventory[key] += 1
					# if no mouse key was pressed
                    # place this resource on the gorund
                    # and grab whatever is currently there
                    # into our inventory
					else:
						self.current_tile = self.tilemap[self.player_pos[1]][self.player_pos[0]]
						if self.inventory[key] > 0:
							self.inventory[key] -= 1
							self.inventory[self.current_tile] += 1
							self.tilemap[self.player_pos[1]][self.player_pos[0]] = key

	def map_resources(self):
		# Inicializálja a térképre a nyersanyagokat
		self.tilemap = [[self.dirt for w in range(self.mapwidth)] for h in range(self.mapheight)]
		for self.row in range(self.mapheight):
			for self.column in range(self.mapwidth):
				self.rn = random.randint(0, 15)
				if self.rn == 0:
					self.tile = self.coal
				elif self.rn in [1, 2]:
					self.tile = self.water
				elif self.rn in [3, 4, 5, 6, 7]:
					self.tile = self.grass
				elif self.rn in [7, 8, 9]:
					self.tile = self.wood
				elif self.rn in [11, 12, 13]:
					self.tile = self.rock
				else:
					self.tile = self.dirt

				# Megjeleníti a térképen a nyersanyagokat
				self.tilemap[self.row][self.column] = self.tile