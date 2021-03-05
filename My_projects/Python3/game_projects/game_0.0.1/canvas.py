from tkinter import*

class Vaszon(Canvas):
    """ Canvas vászonon rajzolás """
    def __init__(self, master):
        Canvas.__init__(self, width = 800, height = 700, bg = "White")
        self.place(x = 10, y = 55)

    def canvas_del(self):
        self.delete(ALL)

    def lines(self, x, y, posx, posy):
        self.line = self.create_line(x, y, posx, posy)

    def rects(self, x, y, posx, posy):
        self.rect = self.create_rectangle(x, y, posx, posy)

    def circles(self, x, y, posx, posy, width, color):
        self.circle = self.create_oval(x, y, posx, posy, width = width, fill = color)