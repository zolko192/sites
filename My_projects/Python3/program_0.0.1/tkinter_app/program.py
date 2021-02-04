#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import*

class Program(Frame):
	""" A főprogram betöltése és megjelenítése """
	
	def __init__(self, boss = None):
		Frame.__init__(self, borderwidth = 2);
		self.mezo1 = Entry(self);
		self.mezo1.bind("<Return>", boss.no);
		self.mezo1.pack();
		self.label1 = Label(self);
		self.label1.pack();
		self.button1 = Button(self, text = "siker", command = boss.yes);
		self.button1.pack(side=BOTTOM);
		
	def elso(self):
		self.label1.configure(text = "sikeres");	
		
	def mezos(self):	
		self.mezo1 = Entry(self);
		self.mezo1.bind("<Return>", self.jelenit);
		self.mezo1.pack(side=TOP);
		self.label1 = Label(self)
		self.label1.pack(side=TOP);
		self.mezo2 = Entry(self);
		self.mezo2.bind("<Return>", self.kiertekel);
		self.mezo2.pack(side=TOP);
		
	def buttons(self):
		self.button1 = Button(self, text = "Háttérszín megváltoztatása", command = lambda: self.canvas.configure(bg = self.mezo2.get())).pack(side=TOP);
			
		self.button2 = Button(self, text = "Parancssor indítása").pack(side=TOP, pady = 5);
		self.button3 = Button(self, text = "Kiíratás", command = lambda: self.label1.configure(text = self.mezo1.get()));
		self.button4 = Button(self, text = "Törlés", command = lambda: self.label1.configure(text = ""));
		
		self.button3.pack(side=TOP, pady = 5);
		self.button4.pack(side=TOP);
		self.button10 = Button(self, text = "Kilépés").pack(side=TOP);
		
	def jelenit(self, event):
		self.label1.configure(text = str(self.mezo1.get()));
		self.mezo1.delete(0, END);
