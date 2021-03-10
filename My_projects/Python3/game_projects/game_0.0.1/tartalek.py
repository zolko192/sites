#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  game.py
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
import pygame

class Map(object):
    """ Térképrács elkészítése """
    def __init__(self):
        self.map_width = 20
        self.map_height = 20
        self.margin = 5
        self.black = pygame.Color("black")
        self.green = pygame.Color("green")
        self.grid = [[0 for x in range(24)] for y in range(32)]
        self.grid[1][5] = 1
        for self.row in range(32):
            for self.column in range(24):
                self.color = self.black
                if self.grid[self.row][self.column] == 1:
                    self.color = self.green
                
                pygame.draw.rect(screen, self.color, ((self.margin + self.map_width) * self.row + self.margin, (self.margin + self.map_height) * self.column + self.margin, self.map_width, self.map_height))

    def print_map(self):
        # Térképrács mezőinek kiíratása
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.pos = pygame.mouse.get_pos()
                self.row = self.pos[0] // (self.map_width + self.margin)
                self.column = self.pos[1] // (self.map_height + self.margin)
                print("Click: ", self.pos, "Grid coordinates: Row: {0} Column: {1}".format(self.row, self.column))
                self.blue = pygame.Color("blue")
                self.grid[self.row][self.column] = 1
                for self.row in range(32):
                    for self.column in range(24):
                        self.color = self.black
                        if self.grid[self.row][self.column] == 1:
                            self.color = self.blue
                        pygame.draw.rect(screen, self.color, ((self.margin + self.map_width) * self.row + self.margin, (self.margin + self.map_height) * self.column + self.margin, self.map_width, self.map_height))



class Background(object):
    """ Háttérkép osztály létrehozása """
    def __init__(self):
        screen.fill(pygame.Color("#48ac30"))


class Window(object):
    """ Ablak létrehozása és szabályozása """
    def __init__(self):
        pass 

    def setScreen(self, fullscreen = False):
        global screen, width, height
        width, height = 800, 600
        if fullscreen:
            screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
        else:
            screen = pygame.display.set_mode((width, height))
        
        self.setTitle("Game_0.0.1")

    def setTitle(self, tiles):
        self.tiles = tiles
        self.titles = pygame.display.set_caption(tiles)

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
            Background()
            ##### <Eseménykezelő> #####
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.waiting = False
                    pygame.quit()
                    quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.ls = Map()
                    self.ls.print_map()
                    self.pos = pygame.mouse.get_pos()
                    self.row = self.pos[0] // (self.ls.map_width + self.ls.margin)
                    self.column = self.pos[1] // (self.ls.map_height + self.ls.margin)
                    print("Click: ", self.pos, "Grid coordinates: Row: {0} Column: {1}".format(self.row, self.column))
                    self.blue = pygame.Color("blue")
                    self.ls.grid[self.row][self.column] = 1
                    for self.row in range(32):
                        for self.column in range(24):
                            self.color = self.ls.black
                            if self.ls.grid[self.row][self.column] == 1:
                                self.color = self.blue
                            pygame.draw.rect(screen, self.color, ((self.ls.margin + self.ls.map_width) * self.row + self.ls.margin, (self.ls.margin + self.ls.map_height) * self.column + self.ls.margin, self.ls.map_width, self.ls.map_height))

            # Rajzolás
            Map()
            # Képernyő és fps beillesztése
            self.setUpdate()
            self.setFps(60)

        # Bezárás
        pygame.quit()
        quit()


class Application(object):
    """ Fő alkalmazás """
    def __init__(self):
        pygame.init()
        self.root = Window()
        self.root.setScreen()
        self.root.endWait()

Application()

import pygame

class Player(object):
    def __init__(self):
        self.x = 20
        self.y = 20
        self.rect = pygame.rect.Rect((0, 0, self.x, self.y))

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
           self.rect.move_ip(-1, 0)
        if key[pygame.K_RIGHT]:
           self.rect.move_ip(1, 0)
        if key[pygame.K_UP]:
           self.rect.move_ip(0, -1)
        if key[pygame.K_DOWN]:
           self.rect.move_ip(0, 1)

    def draw(self, surface):
        pygame.draw.rect(screen, (0, 0, 128), self.rect)

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
player = Player()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

    screen.fill((255, 255, 255))

    player.draw(screen)
    player.handle_keys()
    pygame.display.update()

    clock.tick(60)

import pygame

class Rect_move(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)

    def draw(self, rect):
        pygame.draw.rect(screen, (0, 0, 128), self.rect)


class Player(object):
    def __init__(self, surface):
        self.rect = pygame.rect.Rect((0, 0, 20, 20))

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
           self.rect.move_ip(-1, 0)
        if key[pygame.K_RIGHT]:
           self.rect.move_ip(1, 0)
        if key[pygame.K_UP]:
           self.rect.move_ip(0, -1)
        if key[pygame.K_DOWN]:
           self.rect.move_ip(0, 1)

    def draw(self, surface):
        pygame.draw.rect(screen, (0, 0, 128), self.rect)
        

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
x = 20
margin = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                margin += 1
                x -= 1
            if event.key == pygame.K_LEFT:
                margin -= 1
                x += 1

    screen.fill((255, 255, 255))
    rect_move = Rect_move(0, 0, 20, 20)
    for row in range(10):
        rect_move = Rect_move((margin + x) * row + margin, 0, 20, 20)
        rect_move.draw(screen)
        
    pygame.display.update()

    clock.tick(60)

class Rect_move(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)

    def draw(self, rect):
        pygame.draw.rect(screen, (0, 0, 128), self.rect)