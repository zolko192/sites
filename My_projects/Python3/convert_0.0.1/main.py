#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import*

class Application(Frame):
	""" Főalkalmazás """
	def __init__(self):
		Frame.__init__(self);
		self.width = 640;
		self.height = 480;
		self.menu = self.Menus();
		self.pack();
		
	def Menus(self):
		""" Menü létrehozása """
		##### Menu <File> #####
		self.fileMenu = Menubutton(self, text = "File");
		self.fileMenu.pack(side=LEFT);
		# Menu <File> legördülő része
		self.fileMenu1 = Menu(self.fileMenu);
		self.fileMenu1.add_command(label = "New", underline = 0);
		self.fileMenu1.add_command(label = "Törlés", underline = 0, command = boss.erase);
		self.fileMenu1.add_command(label = "Kilépés", underline = 0, command = boss.quit);
		
		# Menu <File> integrálása
		self.fileMenu.configure(menu = self.fileMenu1);
		
		
		
if __name__ == "__main__":
	app = Application();
	app.mainloop();
