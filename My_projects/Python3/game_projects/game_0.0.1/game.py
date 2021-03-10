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
import configparser
from map import Map
pygame.init()

class Application(object):
    """ Főalkalmazás """
    def __init__(self):
        global screen, width, height, title
        self.pic = pygame.image.load("pictures/background.png")
        config = configparser.ConfigParser()
        config.read('settings.ini')
        width = int(config.get('DEFAULT', 'width'))
        height = int(config.get('DEFAULT', 'height'))
        title = str(config.get('DEFAULT', 'title'))
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        
        self.white = pygame.Color("white")
        self.black = pygame.Color("black")
        self.green = pygame.Color("green")
        self.blue = pygame.Color("blue")

        self.clock = pygame.time.Clock()
        self.fps = int(config.get('DEFAULT', 'fps'))
        self.map = Map(screen)
        self.game_loop()
        pygame.quit()
        quit()

    def game_loop(self):
        self.running = True
        while self.running:
            self.events()

            screen.fill(pygame.Color("white"))
            self.map.map1()
            self.map.map1_event()

            pygame.display.flip()
            self.clock.tick(self.fps)
        
    def events(self):
        for event in pygame.event.get():
            self.do_exit(event)
            self.mouse_event(event)

    def do_exit(self, event):
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.running = False
            pygame.quit()
            quit()

    def mouse_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.print_event(event)

    def print_event(self, event):
        print(event)

Application()