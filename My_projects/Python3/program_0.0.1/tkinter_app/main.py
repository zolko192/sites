#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  main.py
#  verzió: 0.0.1
#
#  Copyright 2020 john31 <john31@john31-Aspire-7735>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from tkinter import*
from menu import Menubar
from program import Program

class Application(Frame):
	""" Főalkalmazás """
	
	def __init__(self, boss = None):
		Frame.__init__(self);
		self.menu = Menubar();
		
	def proba(self, event):
		self.canvas.canvas1.place_configure(anchor = str(self.mezo1.get()));
			
	def no(self, event):
		self.canvas.configure(bg = str(self.mProgram.mezo1.get()));
			
	def yes(self):
		self.mProgram.label1.configure(text = "sikeres");
			
	def kiertekel(self, event):
		self.canvas.configure(bg = str(self.mprogram.mezos.mezo2.get()));
		
	def erase(self):
		self.canvas.delete(ALL);
		
	def music17(self):
		self.canvas.create_text(10, 10, anchor = NW, text = "H.Purcell", font = ("Times", 20, "bold"), fill = "yellow");
		
	def music18(self):
		self.canvas.create_text(245, 40, anchor = NE, text = "W. A. Mozart", font = ("Times", 20, "italic"), fill = "dark green");
		
	def romantic(self):
		self.canvas.create_text(245, 70, anchor =NE, text = "E. Delacroix", font =('Times', 20, 'bold italic'), fill = "blue");
	
	def monet(self):
		self.canvas.create_text(10, 100, anchor =NW, text = 'Nymphéas à Giverny', font =('Technical', 20), fill ='red');
	
	def renoir(self):
		self.canvas.create_text(10, 130, anchor =NW, text = 'Le moulin de la galette', font =('Dom Casual BT', 20), fill ='maroon');
	
	def degas(self):
		self.canvas.create_text(10, 160, anchor =NW, text = 'Danseuses au repos', font =('President', 20), fill ='purple');
		
if __name__ == "__main__":
	app = Application();
	app.mainloop();
