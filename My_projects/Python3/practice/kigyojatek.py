#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Snake(object):
	
	def __init__(self):
		print("Készülőben!");


width, height = 20, 20
margin = 5

for row in range(10):
        for column in range(10):
                print((margin + width) * row + margin, (margin + height) * column + margin)
