#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pygame

gravitacio = 0.0001;

class KiralynoSprite:
	
	def __init__(self, kep, cel_pozicio):
		""" Létrehoz és inicializál egy királynőt a tábla cél pozíciójában. """
		self.kep = kep;
		self.cel_pozicio = cel_pozicio;
		(x, y) = cel_pozicio;
		self.pozicio = (x, 0);	# Az oszlop tetejétől indul a kép
		self.y_sebesseg = 0;	# 0 kezdősebességgel.
		
	def frissites(self):
		self.y_sebesseg += gravitacio;	# A gravitáció módosítja a sebességet.
		(x, y) = self.pozicio;
		uj_y_poz = y + self.y_sebesseg;
		(cel_x, cel_y) = self.cel_pozicio;	# A cél pozició kicsomagolása.
		tav = cel_y - uj_y_poz;		# Milyen messze van a padló.
		if tav < 0:		# A padló alatt vagyunk?
			self.y_sebesseg = -0.65 * self.y_sebesseg;	# Visszapattanás
			uj_y_poz = cel_y + tav;		# Visszatérés a padló fölé.
		
		self.pozicio = (x, uj_y_poz); # A sebesség új pozicióba mozgatja a képet.
		
	def rajzolas(self, cel_felulet):
		cel_felulet.blit(self.kep, self.pozicio);
		

def tabla_rajzolas(kiralynok):
	""" Egy sakktábla rajzolása a kiralynok listával adott királynőkkel együtt. """
	
	pygame.init();
	szinek = [(255, 0, 0), (0, 0, 0)];	# A színek beállítása (red, black)
	
	n = len(kiralynok);	# A tábla mérete: nxn.
	felulet_meret = 960;	# A felület javasolt fizikai mérete.
	mezo_meret = felulet_meret // n;	# A négyzetek oldalhosszúsága.
	felulet_meret = n * mezo_meret;	# Az n négyzet méretéhez igazítjuk a felületet
	
	# Elkészítjük a felületet (szélesség, magasság) és a hozzá tartozó ablakot
	felulet = pygame.display.set_mode((felulet_meret, felulet_meret));
	
	# A csajos kép betöltése és a méret kicsinyítése
	mezo_meret_change = mezo_meret - 5;
	csaj = pygame.transform.scale(pygame.image.load("csaj.png"), (mezo_meret_change, mezo_meret_change));
	
	# A labda négyzeten belüli középre igazításhoz szükséges eltolás.
	# Ha a négyzet túl kicsi, az eltolás negatív lesz, de akkor is középre kerül a labda :-).
	csaj_eltolas=(mezo_meret - csaj.get_width()) // 2;
	
	osszes_sprite = [];	# Lista a játék összes sprite-ja részére.
	
	# Egy-egy sprite készítése minden királynőhöz, és a sprite hozzáadása a listához.
	for (oszlop, sor) in enumerate(kiralynok):
		kiralyno = KiralynoSprite(csaj, (oszlop * mezo_meret + csaj_eltolas, sor * mezo_meret + csaj_eltolas));
		osszes_sprite.append(kiralyno);
	
	while True:
		# A billentyűzet, egér stb események figyelése
		esemeny = pygame.event.poll();
		if esemeny.type == pygame.QUIT:
			break;
			
		# Minden sprite-ot megkérünk, hogy frissítse magát.
		for sprite in osszes_sprite:
			sprite.frissites();
			
		# Egy új háttér rajzolása(egy üres sakktábla). 
		for sor in range(n):	# Az összes sor megrajzolása.
			szin_index = sor % 2;	# A kezdőszín megváltoztatása minden sorban.
			for oszlop in range(n):	# Az oszlopokat bejárva kirajzoljuk a mezőket.
				mezo = (oszlop * mezo_meret, sor * mezo_meret, mezo_meret, mezo_meret);
				felulet.fill(szinek[szin_index], mezo);
				# A következő mező rajzolása előtt megváltoztatjuk a szín indexét
				szin_index = (szin_index + 1) % 2;
	
		for (oszlop, sor) in enumerate(kiralynok):
			# Egy királynő rajzolása az oszlop, sor pozícióra
			felulet.blit(csaj, (oszlop * mezo_meret + csaj_eltolas, sor * mezo_meret + csaj_eltolas));
			
		# Minden sprite-ot megkérünk, hogy rajzolja ki magát.
		for sprite in osszes_sprite:
			sprite.rajzolas(felulet);
			
		pygame.display.flip();
		
	pygame.quit();
