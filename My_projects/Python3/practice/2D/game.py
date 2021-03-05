#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys
import random
import pygame

# 1, Create a character and a game loop.
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

# Létrehozzuk a nyersanyagokat
dirt, grass, water, coal, cloud, wood = 0, 1, 2, 3, 4, 5;
# Létrehozzuk az értékes nyersanyagokat
fire, sand, glass, rock, stone, brick, diamond = 6, 7, 8, 9, 10, 11, 12;	
# Declare resources for inventory interface
resources = [dirt, grass, water, coal, wood, fire, sand, glass, rock, stone, brick, diamond];
 
# Define some colors
BLACK = (0, 0, 0);
WHITE = (255, 255, 255);
BLUE = (0, 0, 255);
GREEN = (0, 255, 0);
RED = (255, 0, 0);

# Definiálja a játékos maximum lépéseit.
tilesize = 40;
mapwidth = 25;
mapheight = 15;

# intialize an inventory
# empty when starting
inventory = {
	dirt: 0,
	grass: 0,
	water: 0,
	coal: 0,
	wood: 0,
	fire: 0,
	sand: 0,
	glass: 0,
	rock: 0,
	stone: 0,
	brick: 0,
	diamond: 0
	};
	
# add controls for crafting
# these numbers correspond to
# number keys 1,2,...0, -, =
controls = {
	dirt: 49, # 1
	grass: 50, # 2
	water: 51, # 3
	coal: 52, # 4
	wood: 53, # 5
	fire: 54, # 6
	sand: 55, # 7
	glass: 56, # 8
	rock: 57, # 9
	stone: 48, # 0
	brick: 45, # -
	diamond: 61 # =
	};
	
# this tells us how many or each resource
# we need to produce a more valuable resource
# so 1 stone takes 1 rock
craft = {
	stone: {rock: 1},
	sand: {rock: 1},
	fire: {wood: 1},
	glass: {fire: 1, sand: 1},
	diamond: {wood: 1, coal: 1},
	brick: {rock: 1, fire: 1}
	};

# Importálja a képeket objektummá
textures = {
	dirt: pygame.image.load("pictures/dirt.png"),
	grass: pygame.image.load("pictures/grass.png"),
	water: pygame.image.load("pictures/water.png"),
	coal: pygame.image.load("pictures/coal.png"),
	cloud: pygame.image.load("pictures/cloud.png"),
	wood: pygame.image.load("pictures/wood.png"),
	fire: pygame.image.load("pictures/fire.png"),
	sand: pygame.image.load("pictures/sand.png"),
	glass: pygame.image.load("pictures/glass.png"),
	rock: pygame.image.load("pictures/rock.png"),
	stone: pygame.image.load("pictures/stone.png"),
	brick: pygame.image.load("pictures/brick.png"),
	diamond: pygame.image.load("pictures/diamond.png")
	};

# Betölti a játékos karakter képét és pozicióját
player = pygame.image.load("pictures/char.png");
player_pos = [0, 0];

# Inicializálja a térképre a nyersanyagokat
tilemap = [[dirt for w in range(mapwidth)] for h in range(mapheight)];

# for each row
for row in range(mapheight):
	# for each column
	for col in range(mapwidth):
		# Generálja a random számokat
		rn = random.randint(0, 15);
		# Random számú értékek beállítása
		if rn == 0:
			tile = coal;
		elif rn in [1, 2]:
			tile = water;
		elif rn in [3, 4, 5, 6, 7]:
			tile = grass;
		elif rn in [7, 8, 9]:
			tile = wood;
		elif rn in [9, 10, 11]:
			tile = rock;
		else:
			tile = dirt;
		# Megjeleníti a térképen a nyersanyagokat
		tilemap[row][col] = tile;

# Inicializálja a pygame-et. 
pygame.init();
 
# Set the width and height of the screen [width, height]
screen = pygame.display.set_mode((mapwidth * tilesize, mapheight * tilesize + 50));
screen_color = pygame.Color("black");
pygame.display.set_caption("Game_0.0.1");
# Létrehozza az inventory betűkészletét.
inventory_font = pygame.font.Font("freesansbold.ttf", 18);
 
# -------- Main Program Loop -----------
while True:
	# If you want a background image, replace this clear with blit'ing the
    # background image.
	screen.fill(screen_color);
	# ----- Main loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit();
			sys.exit();
		elif event.type == pygame.KEYDOWN:
			# Játékos karakter mozgatása
			if event.key == pygame.K_RIGHT and player_pos[0] < mapwidth - 1:
				player_pos[0] += 1;
			if event.key == pygame.K_LEFT and player_pos[0] > 0:
				player_pos[0] -= 1;
			if event.key == pygame.K_DOWN and player_pos[1] < mapheight - 1:
				player_pos[1] += 1;
			if event.key == pygame.K_UP and player_pos[1] > 0:
				player_pos[1] -= 1;
			if event.key == pygame.K_SPACE:
				# Store the current tile.
				currentTile = tilemap[player_pos[1]][player_pos[0]];
				# Add one of that resource to the inventory.
				inventory[currentTile] += 1;
				# Replace the tile on the ground with dirt.
				tilemap[player_pos[1]][player_pos[0]] = dirt;
			# We go through all our number keys
			for key in controls:
				# if one was pressed by the player
				if event.key == controls[key]:
					# if the mouse key was pressed in addition
					if pygame.mouse.get_pressed()[0]:
						# if this is a craftable resource
						if key in craft:
							# check that we have enough 
                            # ingredients to make the resource
							done = True;
							for i in craft[key]:
								if craft[key][i] > inventory[i]:
									done = False;
									break;
							# if we can make the resource
                            # craft it and add it to our
                            # inventory
							if done == True:
								for i in craft[key]:
									inventory[i] -= craft[key][i];
								inventory[key] += 1;
					# if no mouse key was pressed
                    # place this resource on the gorund
                    # and grab whatever is currently there
                    # into our inventory
					else:
						currentTile = tilemap[player_pos[1]][player_pos[0]];
						if inventory[key] > 0:
							inventory[key] -= 1;
							inventory[currentTile] += 1;
							tilemap[player_pos[1]][player_pos[0]] = key;
	
	# Render tilemap			
	for row in range(mapheight):
		for column in range(mapwidth):
			screen.blit(textures[tilemap[row][column]], (column * tilesize, row * tilesize));
			
	# Render inventory.
	place_pos = 10;
	for item in resources:
		screen.blit(textures[item], (place_pos, mapheight * tilesize + 20));
		place_pos += 30;
		text_obj = inventory_font.render(str(inventory[item]), True, WHITE, BLACK);
		screen.blit(text_obj, (place_pos, mapheight * tilesize + 20));
		place_pos += 50;		
 
    # --- Drawing code should go here
	screen.blit(player, (player_pos[0] * tilesize, player_pos[1] * tilesize));
 
    # --- Go ahead and update the screen with what we've drawn.
	pygame.display.update();
 
# Close the window and quit.
pygame.quit();
