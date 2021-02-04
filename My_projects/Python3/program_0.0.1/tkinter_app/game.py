#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import*

# Tk könyvtár inicializálása			
root = Tk();
root.title("Game_0.0.1");
root.geometry("1600x900");

class Application:
	""" Főprogram """
	def __init__(self, boss = None):
		self.root = root;
				##### Menu <File> #####
		self.fileMenu = Menubutton(self.root, bg = "yellow", text = "File");
		self.fileMenu.place(x = 20, y = 10);
		# Menu <File> legördülő része
		self.fileMenu1 = Menu(self.fileMenu);
		self.fileMenu1.add_command(label = "New");
		self.fileMenu1.add_command(label = "Törlés", command = self.canvas_delete);
		self.fileMenu1.add_command(label = "Kilépés", command = boss.destroy);
		# Menu <File> integrálása
		self.fileMenu.configure(menu = self.fileMenu1);
		
		# Canvas Létrehozása
		self.canvas = Canvas(self.root, bg = "ivory", width = 1300, height = 800);
		self.canvas.place(x = 20, y = 40);
	
		# Entry
		self.mezo1 = Entry(self.root);
		self.mezo1.bind("<Return>", self.kiertekel);
		self.mezo1.place(x = 1400, y = 100);
		self.mezo2 = Entry(self.root);
		self.mezo2.bind("<Return>", self.kiertekel);
		self.mezo2.place(x = 1400, y = 125);
		
		# Button
		self.button1 = Button(self.root, text = "sikeres");
		self.button1.place(x = 1400, y = 200);
		
		# Game osztály példányosítása és elhelyezése a vásznon
		Game.__init__(self);
		self.canvas.create_image(15, 15, image = self.player);
		
	def kiertekel(self, event):
		# Entry kiértékelése
		self.canvas.place_configure(x = self.mezo1.get(), y = self.mezo2.get());
		self.mezo1.delete(0, END) or self.mezo2.delete(0, END);
		
	def canvas_delete(self):
		# Canvas képernyő törlése
		self.canvas.delete(ALL);
		
class Game(Application):
	""" A játék inicializálása """
	def __init__(self, boss = None, root = None):
		self.root = root;
		# Definiálja a játékos maximum lépéseit és a térkép méretet
		self.tilesize = 40;
		self.mapwidth = 30;
		self.mapheight = 20;
		# Betölti a játékos karakter képét és a pozicióját
		self.player = PhotoImage(file = "pictures/char.png");
		self.player_pos = (0, 0);
				
		
							
app = Application(root);
root.mainloop();
