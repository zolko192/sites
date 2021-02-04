#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

""" 1. Adj hozzá egy terulet metódust a Teglalap osztályhoz, amelyet ha meghívunk egy példányra, akkor
annak területét adja vissza:
r = Teglalap(Pont(0, 0), 10, 5)
teszt(r.terulet() == 50)
2. Írj egy kerulet metódust a Teglalap osztályon belül, amely segítségével meghatározhatjuk a Teglalap
példányok kerületét:
r = Teglalap(Pont(0, 0), 10, 5)
teszt(r.kerulet() == 30)
3. Írj egy forditas metódust a Teglalap osztályon belül, amellyel felcserélhetjük a Teglalap példányok
magasságát és szélességét:
r = Teglalap(Pont(100, 50), 10, 5)
teszt(r.szelesseg == 10 and r.magassag == 5)
r.forditas()
teszt(r.szelesseg == 5 and r.magassag == 10)
16.5. Szójegyzék
214Hogyan gondolkozz úgy, mint egy informatikus:
Tanulás Python 3 segítségével, 3. kiadás
4. Készíts egy új metódust a Teglalap osztályon belül annak ellenőrzésére, hogy egy Pont objektum a tégla-
lapon belülre esik-e! Ennél a feladatnál feltételezzük, hogy a téglalap a (0, 0) koordinátán van, a szélessége
10, a magassága pedig 5. A téglalap felső határai nyíltak, tehát a téglalap a [0; 10) tartományt foglalja el az x
tengelyen, ahol a 0 a tartomány része, de a 10 nem; y irányban pedig a [0; 5) tartományban áll. Szóval a (10, 2)
pontot nem tartalmazza. Ezeken a teszteken át kell, hogy menjen:
r = Teglalap(Pont(0, 0), 10, 5)
teszt(r.tartalmazza_e(Pont(0, 0)))
teszt(r.tartalmazza_e(Pont(3, 3)))
teszt(not r.tartalmazza_e(Pont(3, 7)))
teszt(not r.tartalmazza_e(Pont(3, 5)))
teszt(r.tartalmazza_e(Pont(3, 4.99999)))
teszt(not r.tartalmazza_e(Pont(-3, -3)))
5. A játékokban gyakran vesszük körül a sprite-okat befoglaló téglalapokkal. (A sprite-ok olyan objektumok,
amelyek mozoghatnak a játékban. Hamarosan látni fogjuk.) Utána már végezhetünk ütközésfigyelést, például
bombák és űrhajók között, azt vizsgálva, hogy átfednek-e valahol a téglalapjaik.
Írj egy függvényt, mely meghatározza, hogy két téglalap összeér-e! Segítség: Ez kemény dió! Gondolj át
alaposan minden lehetőséget, mielőtt kódolni kezdesz. """

""" 1. Adj hozzá egy terulet metódust a Teglalap osztályhoz, amelyet ha meghívunk egy példányra, akkor
annak területét adja vissza:
r = Teglalap(Pont(0, 0), 10, 5)
teszt(r.terulet() == 50) """

class Teglalap:
	""" Téglalap osztály létrehozása, inicializálása. """
	def __init__(self, x, y):
		self.x = x;
		self.y = y;
		
	def terulet(self,	
		
r = Teglalap();
