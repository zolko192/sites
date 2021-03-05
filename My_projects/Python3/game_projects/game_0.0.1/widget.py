from tkinter import*
from canvas import*

class Widgets(Frame):
    """ Widgetek létrehozása a jobb oldali keretbe """
    def __init__(self, master):
        Frame.__init__(self, width = 556, height = 700, bg = "gray")
        self.place(x = 810, y = 55)
        self.proba = Vaszon(master)
    
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
        self.kilep = Button(self, text = "Kilépés", width = 8, command = lambda: quit())
        self.kilep.place(x = 100, y = 310)

    def scales(self):
        self.a, self.b, self.c, self.d = 30, 35, 40, 45
        self.scale1 = Scale(self, command = self.success)
        self.scale1.set(self.a)
        self.scale1.place(x = 250, y = 50)
        self.scale2 = Scale(self, command = self.success)
        self.scale2.set(self.b)
        self.scale2.place(x = 310, y = 50)
        self.scale3 = Scale(self, command = self.success)
        self.scale3.set(self.c)
        self.scale3.place(x = 370, y = 50)
        self.scale4 = Scale(self, command = self.success)
        self.scale4.set(self.d)
        self.scale4.place(x = 430, y = 50)
        self.siker()
          

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

    def siker(self):
        self.label1 = Label(self, text = "")
        self.label1.place(x = 250, y = 30)
        self.label2 = Label(self, text = "")
        self.label2.place(x = 300, y = 30)
        self.label3 = Label(self, text = "")
        self.label3.place(x = 350, y = 30)
        self.label4 = Label(self, text = "")
        self.label4.place(x = 400, y = 30)

    def success(self, e):
        self.label1.config(text = "Sikeres: " + e)
        self.proba.circles(self.scale1.get(), self.scale2.get(), self.scale3.get(), self.scale4.get())