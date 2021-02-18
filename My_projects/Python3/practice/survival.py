#!/usr/bin/python3
# -*- coding: UTF-8 -*-

class Survival(object):
	
	def __init__(self):
		self.wallPine = 5;
		self.wallStone = 5;
		self.wallStoneBrick = 40;
		self.wallIron = 10;
		self.resource = ["Pine", "Stone", "Stone Brick", "Iron"];
		self.i = 0;

	def floor():
		floorPine = 10;
		floorStoneBrick = 10;
		three = 0;
		five = 0;
		for x in range(3):
			three += floorPine * 3;
	
		for x in range(5):
			five += floorPine * 5;
	
		print("Maximális Floor nyersanyag fejlesztése (3 x 3): \n {0} {1} \n {2} {3}\n".format(three, resource[0], three, resource[2]));
		print("Maximális Floor nyersanyag fejlesztése (5 x 5): \n {0} {1} \n {2} {3}\n".format(five, resource[0], five, resource[2]));
	
	def wall():
		wallPine = 5;
		wallStone = 5;
		wallStoneBrick = 40;
		wallIron = 10;
		bekeres = int(input("Kérem írja be a megfelelő számot: "));
		wallPine = (wallPine * bekeres) * bekeres;
		wallStone = (wallStone * bekeres) * bekeres;
		wallStoneBrick = (wallStoneBrick * bekeres) * bekeres;
		wallIron = (wallIron * bekeres) * bekeres;
		print("Az összes Wall nyersanyag szükséges:\n {0} {1}\n {2} {3}\n {4} {5}\n {6} {7}\n".format(wallPine, resource[0], wallStone, resource[1], wallStoneBrick, resource[2], wallIron, resource[3]));
	
	floor();
	wall();
