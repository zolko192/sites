#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
from tkinter import*

class Menubar():
	""" A legördülő menük sora """
	
	def __init__(self):	
		##### Menu <File> #####
		self.fileMenu = Menubutton(self.root, text = "File");
		self.fileMenu.pack(side=LEFT);
		# Menu <File> legördülő része
		self.fileMenu1 = Menu(self.fileMenu);
		self.fileMenu1.add_command(label = "New", underline = 0);
		self.fileMenu1.add_command(label = "Törlés", underline = 0, command = boss.erase);
		self.fileMenu1.add_command(label = "Kilépés", underline = 0, command = boss.quit);
		
		# Menu <File> integrálása
		self.fileMenu.configure(menu = self.fileMenu1);
		
		##### Menu <Zenészek> #####
		self.musicMenu = Menubutton(self, text = "Zenészek");
		self.musicMenu.pack(side=LEFT);
		# Menu <Zenészek> legördülő része
		self.musicMenu1 = Menu(self.musicMenu);
		self.musicMenu1.add_command(label = "17. század", underline = 1, foreground = "red", background = "yellow", font = ("Comic Sans Ms", 11), command = boss.music17);
		self.musicMenu1.add_command(label = "18. század", underline = 1, foreground = "royalblue", background = "white", font = ("Comic Sans Ms", 11, "bold"), command = boss.music18);
		
		# Menu <Zenészek> integrálása
		self.musicMenu.configure(menu = self.musicMenu1);
		
		##### Menu <Festők> #####
		self.paintMenu = Menubutton(self, text = "Festők");
		self.paintMenu.pack(side=LEFT, padx = 3);
		# Menu <Festők> legördülő része
		self.paintMenu1 = Menu(self.paintMenu);
		self.paintMenu1.add_command(label = "klasszikusok", state = DISABLED);
		self.paintMenu1.add_command(label = "romantikusok", underline = 0, command = boss.romantic);
		# Almenü az impresszionista festőknek
		self.paintMenu2 = Menu(self.paintMenu1);
		self.paintMenu2.add_command(label = "Claude Monet", underline = 7, command = boss.monet);
		self.paintMenu2.add_command(label = "Auguste Renoir", underline = 8, command = boss.renoir);
		self.paintMenu2.add_command(label = "Edgar Degas", underline = 6, command = boss.degas);
		
		# Almenü <Festők> integrálása
		self.paintMenu1.add_cascade(label = "impresszionisták", underline = 0, menu = self.paintMenu2);
		# Menu <Festők> integrálása
		self.paintMenu.configure(menu = self.paintMenu1);
		
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
