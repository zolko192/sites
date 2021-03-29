#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  main.py
#  verzió: 0.0.1
#
#  Copyright 2020 john31 <john31@john31-Aspire-7735>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 
import sys
import pygame
import game

class Main(object):
    """ Főosztály """
    def __init__(self):
        # Game osztály példányosítása
        self.game = game.Game()
        self.mapwidth, self.mapheight, self.tilesize, self.tilemap = self.game.mapwidth, self.game.mapheight, self.game.tilesize, self.game.tilemap
        self.player, self.player_pos = self.game.player, self.game.player_pos
        self.textures, self.resources, self.inventory = self.game.textures, self.game.resources, self.game.inventory
        # Főképernyő létrehozása
        self.screen = pygame.display.set_mode((self.mapwidth * self.tilesize, self.mapheight * self.tilesize + 70))
        # Létrehozza az inventory betűkészletét
        self.inventory_font = pygame.font.Font("freesansbold.ttf", 18)
        self.title = pygame.display.set_caption("Game3D_0.0.1")
        self.clock = pygame.time.Clock()
        self.fps = 60

    def Main_loop(self):
        self.running = True
        ##### <Main loop> #####
        while self.running:
            self.screen.fill(pygame.Color("black"))
            ##### <Eseménykezelő> #####
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
                    pygame.quit()
                    sys.exit()

                # Játékos karakter mozgása
                self.game.player_event(event)
            
            # Nyersanyagok feltöltése a képernyőre
            for self.row in range(self.mapheight):
                for self.column in range(self.mapwidth):
                    self.screen.blit(self.textures[self.tilemap[self.row][self.column]], (self.column * self.tilesize, self.row * self.tilesize))
            
            # Render inventory
            self.place_pos = 10
            for self.item in self.resources:
                self.screen.blit(self.textures[self.item], (self.place_pos, self.mapheight * self.tilesize + 20))
                self.place_pos += 30
                self.text_obj = self.inventory_font.render(str(self.inventory[self.item]), True, pygame.Color("white"), pygame.Color("black"))
                self.screen.blit(self.text_obj, (self.place_pos, self.mapheight * self.tilesize + 20))
                self.place_pos += 50

            # Játékos képének feltöltése képernyőre
            self.screen.blit(self.player, (self.player_pos[0] * self.tilesize, self.player_pos[1] * self.tilesize))

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    pygame.init()
    main = Main()
    main.Main_loop()