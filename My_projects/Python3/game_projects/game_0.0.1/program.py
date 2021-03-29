import tkinter as tk
from widgets import Widgets

class Program(object):
    """ Főprogram """
    def __init__(self, master = None):
        self.master = master
    
        self.canvas = tk.Canvas(self.master, width = 700, height = 750, bg = "white")
        self.canvas.place(x = 10, y = 10)
    
        self.frame = tk.Frame(self.master, width = 650, height = 750, bg = "lightgray")
        self.frame.place(x = 700, y = 10)
        self.widget = Widgets(self.frame, self.canvas)