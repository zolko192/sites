#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2021 john31 <john31@john31>
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
# Pygame inicializálása
import pygame
pygame.init()

class Background(object):
    """ Háttérkép osztály létrehozása """
    def __init__(self):
        pass


class Window(object):
    """ Ablak létrehozása és szabályozása """
    def __init__(self):
        pass

    def setScreen(self, sizex, sizey, fullscreen = False):
        global screen
        self.sizex = sizex
        self.sizey = sizey
        if fullscreen:
            screen = pygame.display.set_mode((self.sizex, self.sizey), pygame.FULLSCREEN)
        else:
            screen = pygame.display.set_mode((self.sizex, self.sizey))
        
        self.title = self.setTitle("Game3D_0.0.1")

    def setTitle(self, titles):
        self.titles = titles
        self.titles = pygame.display.set_caption(self.titles)

    def setUpdate(self):
        pygame.display.flip()

    def setFps(self, fps):
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.clock.tick(self.fps)

    def endWait(self):
        # Főképernyő végtelen ciklusa
        self.waiting = True
        while self.waiting:
            # Képernyő háttér kitöltése
            screen.fill(pygame.Color("white"))
            ##### <Eseménykezelő> #####
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.waiting = False
                    pygame.quit()
                    quit()

            # Rajzolás
            

            # Képernyő és fps beillesztése
            self.setUpdate()
            self.setFps(60)

        # Bezárás
        pygame.quit()
        quit()


class Application(object):
    """ Fő alkalmazás """
    def __init__(self):
        self.root = Window()
        self.root.setScreen(800, 600)
        self.root.endWait()


Application()