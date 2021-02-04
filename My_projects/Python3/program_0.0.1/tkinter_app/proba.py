#!/usr/b/in/env python3
# -*- coding: utf-8 -*-
from tkinter import*

class Menubar:
	
	def __init__(self, boss = None, root = None):
		self.root = root;
		self.button3 = Button(self.root, text = "király");
		self.button3.place(x = 1400, y = 150);	
