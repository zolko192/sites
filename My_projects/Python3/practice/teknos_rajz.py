#!/usr/bin/env python3
# -*- coding: Utf-8 -*-
import turtle

class Turtle_draw(object):
	
	def __init__(self):
		self.ablak = turtle.Screen();
		self.ablak.title("Szia, Zoli & Eszti");
		self.zoli = turtle.Turtle();
		self.zoli.forward(90);

		self.ablak.mainloop();
