#!/usr/bin/env python3
# -*- coding: UTF-8 -*- 
import pygame
 
# Define some colors
BLACK = (0, 0, 0);
WHITE = (255, 255, 255);
BLUE = (0, 0, 255);
GREEN = (0, 255, 0);
RED = (255, 0, 0);
 
pygame.init();
 
# Set the width and height of the screen [width, height]
size = (1600, 900);
screen = pygame.display.set_mode(size);
bg_choice = pygame.Color("white");
 
pygame.display.set_caption("Game_0.0.1");
 
# Loop until the user clicks the close button.
done = False;
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock();
x_speed = 0;
				
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # User pressed down on a key
            
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
				x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(bg_choice);
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip();
 
    # --- Limit to 60 frames per second
    clock.tick(60);
 
# Close the window and quit.
pygame.quit();
