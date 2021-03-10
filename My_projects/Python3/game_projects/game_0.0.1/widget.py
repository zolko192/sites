from tkinter import*
from tkinter import colorchooser
from canvas import*

class Widgets(Frame):
    """ Widgetek létrehozása a jobb oldali keretbe """
    def __init__(self, master):
        Frame.__init__(self, width = 556, height = 700, bg = "gray")
        self.place(x = 810, y = 55)
        self.proba = Vaszon(master)

    def colors(self):
        self.color_choose = colorchooser.askcolor()
        print(self.color_choose)
    
    def labels(self):
        self.labelX = Label(self, text = "X:")
        self.labelX.place(x = 35, y = 20)
        self.labelY = Label(self, text = "Y:")
        self.labelY.place(x = 35, y = 50)
        self.label_posX = Label(self, text = "X pos:")
        self.label_posX.place(x = 10, y = 80)
        self.label_posY = Label(self, text = "Y pos:")
        self.label_posY.place(x = 10, y = 110)
        self.label_width = Label(self, text = "Width:")
        self.label_width.place(x = 10, y = 140)
        self.label_color = Label(self, text = "Color:")
        self.label_color.place(x = 10, y = 170)

    def mezos(self):
        self.posX = Entry(self)
        self.posX.bind("<Return>", self.kiertekel)
        self.posX.place(x = 60, y = 20)
        self.posY = Entry(self)
        self.posY.bind("<Return>", self.kiertekel)
        self.posY.place(x = 60, y = 50)
        self.pos_x = Entry(self)
        self.pos_x.bind("<Return>", self.kiertekel)
        self.pos_x.place(x = 60, y = 80)
        self.pos_y = Entry(self)
        self.pos_y.bind("<Return>", self.kiertekel)
        self.pos_y.place(x = 60, y = 110)
        self.mezo_width = Entry(self)
        self.mezo_width.bind("<Return>", self.kiertekel)
        self.mezo_width.place(x = 60, y = 140)
        self.mezo_color = Entry(self)
        self.mezo_color.bind("<Return>", self.kiertekel)
        self.mezo_color.place(x = 60, y = 170)

    def buttons(self):
        self.rajz = Button(self, text = "Rajzolás", width = 8, command = self.mezo_load)
        self.rajz.place(x = 100, y = 210)
        self.torles = Button(self, text = "Törlés", width = 8, command = lambda: self.proba.canvas_del())
        self.torles.place(x = 100, y = 250)
        self.szinek = Button(self, text = "Színek", width = 8, command = self.colors)
        self.szinek.place(x = 100, y = 290)
        self.kilep = Button(self, text = "Kilépés", width = 8, command = lambda: quit())
        self.kilep.place(x = 100, y = 370)

    def kiertekel(self, event):
        self.proba.circles(x = self.posX.get(), y = self.posY.get(), posx = self.pos_x.get(), posy = self.pos_y.get(), width = self.mezo_width.get(), color = self.mezo_color.get())

    def mezo_delete(self):
        self.posX.delete(0, END)
        self.posY.delete(0, END)
        self.pos_x.delete(0, END)
        self.pos_y.delete(0, END)
        self.proba.canvas_del()

    def mezo_load(self):
        self.ls = [
            self.proba.circles(20, 45, 100, 150, 3, "white"),
            self.proba.circles(40, 75, 50, 85, 1, "white"),
            self.proba.circles(70, 75, 80, 85, 1, "white"),
            self.proba.circles(41.3, 77.5, 46.5, 82.5, 0, "blue"),
            self.proba.circles(70, 75, 80, 85, 0, "blue"),
        ]