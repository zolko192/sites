#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import*
import game

class Menubar(Frame):
	""" Menubar létrehozása """
	def __init__(self, master):
		Frame.__init__(self, width = 1356, height = 50)
		self.place(x = 10, y = 5)
		##### Menu <File> #####
		self.fileMenu = Menubutton(self, text = "File")
		self.fileMenu.place(x = 10, y = 10)
		# Menu <File> legördülő része
		self.fileMenu1 = Menu(self.fileMenu)
		self.fileMenu1.add_command(label = "New")
		self.fileMenu1.add_command(label = "Megnyitás")
		self.fileMenu1.add_command(label = "Törlés")
		self.fileMenu1.add_command(label = "Kilépés", command = lambda: quit())

		# Menu <File> integrálása
		self.fileMenu.configure(menu=self.fileMenu1)

		##### Menu <Edit> #####
		self.editMenu = Menubutton(self, text = "Edit")
		self.editMenu.place(x = 50, y = 10)
		# Menu <Edit> legördülő része
		self.editMenu1 = Menu(self.editMenu)
		self.editMenu1.add_command(label = "Line")

		# Menu <Edit> integrálása
		self.editMenu.configure(menu=self.editMenu1)

		##### Menu <Game> #####
		self.gameMenu = Menubutton(self, text = "Game")
		self.gameMenu.place(x = 90, y = 10)
		# Menu <Game> legördülő része
		self.gameMenu1 = Menu(self.gameMenu)
		self.gameMenu1.add_command(label = "Új játék indítása", command = lambda: game.Application())

		# Menu <Game> integrálása
		self.gameMenu.configure(menu=self.gameMenu1)

		##### Menu <Zenészek> #####
		self.musicMenu = Menubutton(self, text = "Zenészek")
		self.musicMenu.place(x = 140, y = 10)
		# Menu <Zenészek> legördülő része
		self.musicMenu1 = Menu(self.musicMenu)
		self.musicMenu1.add_command(label = "17. század", underline = 1, foreground = "red", background = "yellow", font = ("Comic Sans Ms", 11))
		self.musicMenu1.add_command(label = "18. század", underline = 1, foreground = "royalblue", background = "white", font = ("Comic Sans Ms", 11, "bold"))
		# Menu <Zenészek> integrálása
		self.musicMenu.configure(menu= self.musicMenu1)

		##### Menu <Festők> #####
		self.paintMenu = Menubutton(self, text = "Festők")
		self.paintMenu.place(x = 220, y = 10)
		# Menu <Festők> legördülő része
		self.paintMenu1 = Menu(self.paintMenu)
		self.paintMenu1.add_command(label = "Klasszikusok", state = DISABLED)
		self.paintMenu1.add_command(label = "Romantikusok", underline = 0)
		# Almenü az impresszionista festőknek
		self.paintMenu2 = Menu(self.paintMenu1)
		self.paintMenu2.add_command(label = "Claude Monet", underline = 7)
		self.paintMenu2.add_command(label = "Auguste Renoir", underline = 8)
		self.paintMenu2.add_command(label = "Edgar Degas", underline = 6)
		# Almenü <Festők> integrálása
		self.paintMenu1.add_cascade(label = "Impresszionisták", underline = 0, menu = self.paintMenu2)
		# Menu <Festők> integrálása
		self.paintMenu.configure(menu = self.paintMenu1)



class Menubars():
	""" A legördülő menük sora """
	
	def __init__(self):	
		##### Menu <Options> #####
		self.optionsMenu = Menubutton(self, text = "Options");
		self.optionsMenu.pack(side=LEFT, padx = 3);
		# Tkinter változók
		self.relief = IntVar();
		self.actMusic = IntVar();
		self.actPaint = IntVar();
		# Menu <Options> legördülő része
		self.optionsMenu1 = Menu(self.optionsMenu);
		self.optionsMenu1.add_command(label = "Aktiválás", foreground = "blue");
		self.optionsMenu1.add_checkbutton(label = "Zenészek", command = self.choiceActive, variable = self.actMusic);
		self.optionsMenu1.add_checkbutton(label = "Festők", command = self.choiceActive, variable = self.actPaint);
		self.optionsMenu1.add_separator();
		self.optionsMenu1.add_command(label = "Domborzat", foreground = "blue");
		for (v, lab) in [(0, "nincs"), (1, "kiemelkedő"), (2, "besüllyedő"), (3, "árok"), (4, "gerinc"), (5, "keret")]:
			self.optionsMenu1.add_radiobutton(label = lab, variable = self.relief, value = v, command = self.reliefBarre);
		
		# Menu <Options> integrálása
		self.optionsMenu.configure(menu = self.optionsMenu1);
		
	def reliefBarre(self):
		choice = self.relief.get();
		self.configure(relief = [FLAT, RAISED, SUNKEN, GROOVE, RIDGE, SOLID][choice]);
		
	def choiceActive(self):
		p = self.actPaint.get();
		m = self.actMusic.get();
		self.paintMenu.configure(state = [DISABLED, NORMAL][p]);
		self.musicMenu.configure(state = [DISABLED, NORMAL][m]);