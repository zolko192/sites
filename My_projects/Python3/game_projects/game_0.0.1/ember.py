import pygame
from canvas import*

class Ember(object):
    """ Character ember létrehozása """
    def __init__(self, master):
        self.ember = Vaszon(master)
        self.ls = [
            self.ember.circles(20, 45, 100, 150, 3, "white"),
            self.ember.circles(40, 75, 50, 85, 1, "white"),
            self.ember.circles(70, 75, 80, 85, 1, "white"),
            self.ember.circles(41.3, 77.5, 46.5, 82.5, 0, "blue"),
            self.ember.circles(70, 75, 80, 85, 0, "blue"),
        ]