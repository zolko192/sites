#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from tkinter import*
from kigyojatek import Snake
from messages import Messages
from teglalap import Teglalap
from teknos_rajz import Turtle_draw
from download import Download

class Application(object):
    """ Fő alkalmazás tkinterrel """
    def __init__(self):
        self.root = Tk();
        self.root.title("My_projects");
        self.rootWidth = self.root.winfo_width();
        self.rootHeight = self.root.winfo_height();
        self.root.geometry("640x480");
        self.root.configure(bg = "ivory");
        self.button_exit = Button(self.root, command = self.do_exit, text = "Kilépés");
        self.button_exit.pack();
        Frames(self.root);
        self.root.mainloop();

    def do_exit(self):
        self.root.destroy();
        Console.button_exit(self);

class Frames(object):
    """ Frame keret létrehozása és beillesztése a fő alkalmazásba """
    def __init__(self, master):
        self.frame = Frame(master);
        self.frame.configure(bg = "blue");
        self.buttons();
        self.frame.pack();

    def buttons(self):
        self.button1 = Button(self.frame, text = "elso");
        self.button1.pack();
        self.button2 = Button(self.frame, text = "Második");
        self.button2.pack();

        
    
class Console(object):
    """ Fő alkalmazás """
    def __init__(self):
        print("A projekteim listába rendezve:\n");
        # A fő lista létrehozása és kiíratása
        self.lista = [(1, "download.py"),
                      (2, "editor.py"),
                      (3, "elso.py"),
                      (4, "ember.py"),
                      (5, "english_hungary.py"),
                      (6, "file_kezeles.py"),
                      (7, "ftp_connect.py"),
                      (8, "kigyojatek.py"),
                      (9, "messages.py"),
                      (10, "proba.py"),
                      (11, "survival.py"),
                      (12, "tanulas.py"),
                      (13, "teglalap.py"),
                      (14, "teknos_rajz.py"),
                      (15, "grafikus_project"),
                      (16, "Kilépés")];

        for (self.szam, self.name) in self.lista:
            print("{0}, {1}".format(self.szam, self.name));

        self.choice();

    def button_exit(self):
        self.logical = False;

    def choice_do_exit(self):
        # Feltétel ellenőrzése
        self.kilepes = str(input("Biztosan ki szeretne lépni?I/n "));
        if self.kilepes == "I" or self.kilepes == "i":
            self.logical = False;
        elif self.kilepes == "N" or self.kilepes == "n":
            self.choice();
        else:
            print("Kérem írja be megfelelően a választ!");
            self.valaszt();

    def choice(self):
        # Kiválaszthatja melyik projectet töltse be
        self.logical = True;
        while(self.logical):
            self.number = int(input("Kérem írja be a megfelelő számot: "));
            if self.number == 1:
                print("Javítás alatt.....");
                Download();
            
            elif self.number == 2:
                print("Feltöltés alatt.....");
            
            elif self.number == 3:
                print("Feltöltés alatt.....");
            
            elif self.number == 4:
                print("Feltöltés alatt.....");
            
            elif self.number == 5:
                print("Feltöltés alatt.....");
            
            elif self.number == 6:
                print("Feltöltés alatt.....");
            
            elif self.number == 7:
                print("Feltöltés alatt.....");
            
            elif self.number == 8:
                Snake();
            
            elif self.number == 9:
                Messages();

            elif self.number == 10:
                print("Feltöltés alatt.....");

            elif self.number == 11:
                print("Feltöltés alatt.....");

            elif self.number == 12:
                print("Feltöltés alatt.....");

            elif self.number == 13:
                Teglalap(10, 10);

            elif self.number == 14:
                Turtle_draw();

            elif self.number == 15:
                print("Feltöltés alatt.....");
                Application();

            elif self.number == 16:
                self.choice_do_exit();

            else:
                print("Kérem válasszon egy másik számot!");
                self.choice();

            


    
Application()
