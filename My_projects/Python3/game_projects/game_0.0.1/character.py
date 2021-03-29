import tkinter as tk

class Character(object):
    """ Karakter létrehozása """
    def __init__(self, frame = None, canvas = None):
        self.frame = frame
        self.canvas = canvas

    def character(self):
        self.lista = []
        self.x, self.y = 10, 10
        self.rectangle = self.canvas.create_rectangle(self.x, self.y, self.x + 10, self.y + 10)
        self.oval = self.canvas.create_oval(self.x, self.y, self.x + 10, self.y + 10)
        self.lista.append(self.rectangle)
        self.lista.append(self.oval)
        print(self.lista[0], self.lista[1])

    def right(self):
        for self.i in self.lista:
            self.canvas.move(self.i, 10, 0)
    def left(self):
        for self.i in self.lista:
            self.canvas.move(self.i, -10, 0)
    def up(self):
        for self.i in self.lista:
            self.canvas.move(self.i, 0, -10)
    def down(self):
        for self.i in self.lista:
            self.canvas.move(self.i, 0, 10)