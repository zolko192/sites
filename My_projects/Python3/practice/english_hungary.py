#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Menu create for loop
def menu():
	for i in range(8):
		szam = [" 1,", "Angol - magyar szó hozzáadása\n",  
		"2,", "Szótár szerkesztése\n",
		"3,", "Szótár beolvasása\n", 
		"4,", "Kilépés\n\n"];
		print(szam[i], end=" ");

# Vocabulary create and run		
def vocabulary():
	file1 = open("words.txt", "r");
	xs = file1.readlines();
	file1.close();
	file2 = open("words.txt", "w");
	english = str(input(" Kérem írja be az angol szót: "));
	xs += english + " - ";
	hungary = str(input(" Kérem írja be a magyar szót: "));
	xs += hungary + "\n";
	for v in xs:
		file2.write(v);
	file2.close();
	
def reading():
	file1 = open("words.txt", "r");
	while True:
		xs = file1.readline();
		if len(xs) == 0:
			break;
		print(xs, end="");
	file1.close();
		
# Vocabulary for new words	
def add():
	logical = True;
	while logical:
		choose = str(input(" Hozzá kíván még adni új elemet? I/n "));
		if choose == "i" or choose == "I" or choose == "Igen" or choose == "igen":
			vocabulary();
		elif choose  == "n" or choose == "N" or choose == "Nem" or choose == "nem":
			valaszt = int(input(" 1, Főmenű\n 2, Mentés\n 3, Kilépés\n"));
			if valaszt == 1:
				menu();
				logical = False;
			elif valaszt == 2:
				saves();
			elif valaszt == 3:
				print( "Sikeresen kilépett!");
				logical = False;
				quit();
			else:
				print(" Hiba! Kérem válassza ki a megfelelő számot.");
				
# Main loop
logical = True;
menu();
while logical:
	logical = True;
	bekeres = int(input("Kérem írja be a megfelelő számot: "));
	if bekeres == 1:
		vocabulary();
		add();					
	elif bekeres == 2:
		print("Készülőben van!");
	elif bekeres == 3:
		reading();
		menu();
	elif bekeres == 4:
		kilep = str(input(" Biztos ki szeretne lépni? I/n "));
		if kilep == "n" or kilep == "N" or kilep == "Nem" or kilep == "nem":
			menu();
		elif kilep == "I" or kilep == "i" or kilep == "Igen" or kilep == "igen":
			print(" Sikeresen kilépett!");
			logical = False;
	else:
		print("Hiba! Nem megfelelő számot használt, kérem próbálja újra!");
		menu();
