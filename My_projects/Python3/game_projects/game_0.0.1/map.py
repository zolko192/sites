import pygame

class Map(object):
    """ Térképrács elkészítése és konfigurálása """
    def __init__(self, screen):
        self.screen = screen
        self.map_width, self.map_height = 20, 20
        self.margin = 5
        self.white = pygame.Color("white")
        self.black = pygame.Color("black")
        self.blue = pygame.Color("blue")

    def map1(self):
        for self.row in range(10):
            for self.column in range(10):
                self.color = self.black
                pygame.draw.rect(self.screen, self.black, ((self.margin + self.map_width) * self.row + self.margin, (self.margin + self.map_height) * self.column + self.margin, 20, 20))

    def map1_event(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.margin -= 1
            self.map_width += 1
            self.map_height += 1
        if key[pygame.K_RIGHT]:
            self.margin += 1
            self.map_width -= 1
            self.map_height -= 1
        if key[pygame.K_UP]:
            self.margin -= 1
            self.map_width += 1
            self.map_height += 1
        if key[pygame.K_DOWN]:
            pass

    def map2(self):
        for self.row in range(10):
            for self.column in range(10):
                self.color = self.blue
                pygame.draw.rect(self.screen, self.color, ((self.margin + self.map_width) * self.row + self.margin, (self.margin + self.map_height) * self.column + self.margin, self.map_width, self.map_height))