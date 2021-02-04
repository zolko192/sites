#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Fájl kezelős függvények
def file_read(file_name):
	""" A teljes fájl beolvasása terminálba """
	file1 = open(file_name, "r");
	while True:
		line1 = file1.read();
		if len(line1) == 0:
			break;
		file1.close();
		return line1;
	
def file_read_words(file_name_read):
	""" Szavak olvasása a megadott fájlból, visszatér a szavak listájával. """
	file1 = open(file_name_read, "r");
	line1 = file1.read();
	file1.close();
	words = line1.split();
	print("A szókincsben {0} szó található".format(len(words)));
	
def szovegbol_szavak(szoveg):
	""" Visszaadja a szavak listáját, eltávolítva az összes írásjelt és
	minden szót kisbetűssé alakít. """
	helyettesites = szoveg.maketrans(
	# Ha bármelyikükkel találkozol
	"AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ0123456789!\"#$%&()*+,./:;<=>?@[]^_`{|}~'\\",
	# Cseréld őket ezekre
	"aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz");
	# Most alakítsd át a szöveget
	tisztitott_szoveg = szoveg.translate(helyettesites);
	szavak = tisztitott_szoveg.split();
	return szavak;
	
def szomszedos_dupl_eltovolit(xs):
	""" Visszatér egy új listával, amelyben a szomszédos
		duplikátumok el vannak távolítva az xs listából. """
	eredmeny = [];
	aktualis_elem = None;
	for e in xs:
		if e != aktualis_elem:
			eredmeny.append(e);
			aktualis_elem = e;
	return eredmeny;
