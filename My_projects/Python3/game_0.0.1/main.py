#!/usr/bin/python3
# -*- coding: iso-8859-2 -*-
import pygame

# Pygame inicializálása
pygame.init();

# Ablak létrehozása és konfigurálása
display_width = 800;
display_height = 600;
gameDisplay = pygame.display.set_mode((display_width, display_height));
pygame.display.set_caption("Game_0.0.1");

# Színek
black = (0, 0, 0);
white = (255, 255, 255);
red = (255, 0, 0);

# clock definite
clock = pygame.time.Clock();

# Kép
carImg = pygame.image.load('pictures/racecar.png');
car_width = 73;

# Koordináta függvény létrehozása
def coordinate():
    print(event);

# Kép pozicionálása a képernyőre
def car(x, y):
    gameDisplay.blit(carImg, (x, y));

##### <Főprogram> #####
def game_loop():
    x = display_width * 0.45;
    y = display_height * 0.8;

    x_change = 0;

    # Főprogram logikai változója
    gameExit = False;

    # Főprogram ciklusa
    while not gameExit:
        # Eseménykezelő
        for event in pygame.event.get():
            # Kilépés
            if event.type == pygame.QUIT:
                gameExit = True;

            #############################
            ##### Billentyű leütése #####
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5;
                elif event.key == pygame.K_RIGHT:
                    x_change = 5;

            ##### Billentyű felengedése #####
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0;
            #############################

        x += x_change;

        # Háttérszín feltöltése
        gameDisplay.fill(white);

        # Kép feltöltése a képernyőre
        car(x, y);

        # Képernyő feltöltése
        pygame.display.update();

        # FPS képernyő frissítés
        clock.tick(60);

# Főprogram indítása
game_loop();

# Pygame kilépés
pygame.quit();

# Quit
quit();
