import tkinter as tk
from tkinter import ttk
from character import Character

class Widgets(object):
    """ Widgetek létrehozása """
    def __init__(self, frame = None, canvas = None):
        self.frame = frame
        self.canvas = canvas
        ##### <Add Character class> ######
        self.character = Character(self.frame, self.canvas)
        ##### <Add Widgets> #####
        self.labels()
        self.txtbox()
        self.buttons()
        self.combobox()

    def labels(self):
        # Label positioning
        self.labelx = tk.Label(self.frame, text = "X:", width = 5)
        self.labelx.place(x = 10, y = 10)
        self.labely = tk.Label(self.frame, text = "Y:", width = 5)
        self.labely.place(x = 10, y = 40)
        self.labelX = tk.Label(self.frame, text = "X pos:")
        self.labelX.place(x = 10, y = 70)
        self.labelY = tk.Label(self.frame, text = "Y pos:")
        self.labelY.place(x = 10, y = 100)
        # Combobox label
        self.positionlabel = tk.Label(self.frame, text = "Positions:", width = 8)
        self.positionlabel.place(x = 230, y = 10)
        self.stylelabel = tk.Label(self.frame, text = "Styles:", width = 8)
        self.stylelabel.place(x = 230, y = 50)
        self.colorlabel = tk.Label(self.frame, text = "Colors:", width = 8)
        self.colorlabel.place(x = 230, y = 90)
        self.labelnot = tk.Label(self.frame, text = "")
        self.labelnot.place(x = 230, y = 140)

    def txtbox(self):
        # Textbox positioning
        self.txtx = tk.Entry(self.frame)
        self.txtx.bind("<Return>", self.events)
        self.txtx.insert(tk.END, "100")
        self.txtx.place(x = 50, y = 10)
        self.txty = tk.Entry(self.frame)
        self.txty.bind("<Return>", self.events)
        self.txty.insert(tk.END, "200")
        self.txty.place(x = 50, y = 40)
        self.txtposx = tk.Entry(self.frame)
        self.txtposx.bind("<Return>", self.events)
        self.txtposx.insert(tk.END, "300")
        self.txtposx.place(x = 50, y = 70)
        self.txtposy = tk.Entry(self.frame)
        self.txtposy.bind("<Return>", self.events)
        self.txtposy.insert(tk.END, "400")
        self.txtposy.place(x = 50, y = 100)

    def combobox(self):
        # Positions Combobox
        self.pos_var = tk.StringVar()
        self.positionbox = ttk.Combobox(self.frame, textvariable = self.pos_var)
        self.positionbox["values"] = (
            "Kérem válasszon pozicinálást",
            "Label",
            "Textbox",
            "Button"
        )
        self.positionbox.current(0)
        self.positionbox.bind("<<ComboboxSelected>>", self.box_events)
        self.positionbox.place(x = 300, y = 10)

        # Styles Combobox
        self.style_var = tk.StringVar()
        self.stylebox = ttk.Combobox(self.frame, textvariable = self.style_var)
        self.stylebox["values"] = (
            "Kérem válasszon stílust",
            "line",
            "oval",
            "rectangle",
            "text"
        )
        self.stylebox.current(0)
        self.stylebox.bind("<<ComboboxSelected>>", self.box_events)
        self.stylebox.place(x = 300, y = 50)
        # Color combobox
        self.color_var = tk.StringVar()
        self.colorbox = ttk.Combobox(self.frame, textvariable = self.color_var)
        self.colorbox["values"] = (
            "Kérem válasszon színt",
            "white",
            "black",
            "blue",
            "yellow",
            "red",
            "brown"
        )
        self.colorbox.current(0)
        self.colorbox.bind("<<ComboboxSelected>>", self.box_events)
        self.colorbox.bind("<Return>", self.box_events)
        self.colorbox.place(x = 300, y = 90)

    def buttons(self):
        # Button positoning
        self.rajzolas = tk.Button(self.frame, text = "Rajzolás", width = 8, command = self.character.character)
        self.rajzolas.place(x = 90, y = 140)
        self.torles = tk.Button(self.frame, text = "Törlés", width = 8, command = lambda: self.canvas.delete(tk.ALL))
        self.torles.place(x = 90, y = 180)
        self.mozgas = tk.Button(self.frame, text = "Mozgatás", width = 8, command = self.moves_button)
        self.mozgas.place(x = 90, y = 220)
        self.kilep = tk.Button(self.frame, text = "Kilépés", width = 8, command = lambda: self.frame.quit())
        self.kilep.place(x = 90, y = 260)

    def moves_button(self):
        self.up = tk.Button(self.frame, text = "Fel", width = 8, command = self.character.up)
        self.up.place(x = 250, y = 180)
        self.down = tk.Button(self.frame, text = "Le", width = 8, command = self.character.down)
        self.down.place(x = 250, y = 210)
        self.left = tk.Button(self.frame, text = "Balra", width = 8, command = self.character.left)
        self.left.place(x = 250, y = 240)
        self.right = tk.Button(self.frame, text = "Jobbra", width = 8, command = self.character.right)
        self.right.place(x = 250, y = 270)

    def events(self, event):
        # Events choice
        if self.stylebox.get() == "line":
            self.line(self.colorbox.get())
        elif self.stylebox.get() == "oval":
            self.oval(self.colorbox.get())
        elif self.stylebox.get() == "rectangle":
            self.rectangle(self.colorbox.get())

    def box_events(self, event):
        # Colors Combobox events
        if self.stylebox.get() == "line":
            self.line(self.colorbox.get())
            self.labelnot.config(text = "")
        elif self.stylebox.get() == "oval":
            self.oval(self.colorbox.get())
            self.labelnot.config(text = "")
        elif self.stylebox.get() == "rectangle":
            self.rectangle(self.colorbox.get())
            self.labelnot.config(text = "") 
        elif self.stylebox.get() == "text":
            self.labelnot.config(text = "Fejlesztés alatt, kérem válasszon egy másikat!")
        else:
            self.labelnot.config(text = "")

        if self.positionbox.get() == "Label" or self.positionbox.get() == "Textbox" or self.positionbox.get() == "Button":
            self.labelnot.config(text = "Fejlesztés alatt, kérem válasszon egy másikat!")

    def line(self, color):
        self.canvas.create_line(self.txtx.get(), self.txty.get(), self.txtposx.get(), self.txtposy.get(), fill = color)
    def oval(self, color):
        self.canvas.create_oval(self.txtx.get(), self.txty.get(), self.txtposx.get(), self.txtposy.get(), outline = color)
    def rectangle(self, color):
        self.canvas.create_rectangle(self.txtx.get(), self.txty.get(), self.txtposx.get(), self.txtposy.get(), outline = color)