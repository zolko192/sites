#!/usr/b/in/env python3
# -*- coding: utf-8 -*-
from tkinter import*
from dir_file import*

class Application(object):
        """ Főprogram """
        def __init__(self, root = None):
                # Tkinter ablak létrehozása és konfigurálása.
                self.root = Tk();
                self.root.title("Főprogram");
                self.root.geometry("800x600");
                self.root.configure(bg = "Blue");
                
                self.vaszon();
                self.ablak();

                # Kilépés gomb létrehozása és konfigurálása
                self.button_exit = Button(self.frame, text = "Kilépés", command = lambda: self.root.destroy());
                self.button_exit.place(x = 20, y = 140);

                # Mappa listázó gomb létrehozása és konfigurálása
                self.button_dir = Button(self.frame, text = "Mappa listázása", command = lambda: mappa_files());
                self.button_dir.place(x = 20, y = 20);

                # Menü osztály hozzáadása
                Menubar();

                # Üres mezők hozzáadása
                self.mezos();

                # Tkinter lefutása
                self.root.mainloop();


        def vaszon(self):
                # Canvas vászon létrehozása
                self.canvas = Canvas(self.root, width = "400", height = "550", bg = "Yellow");
                self.canvas.place(x = 0, y = 50);

        def ablak(self):
                # Frame ablak hozzáadása
                self.frame = Frame(self.root, width = "400", height = "550", bg = "gray");
                self.frame.place(x = 400, y = 50);

        def mezos(self):
                self.mezo1 = Entry(self.frame);
                self.mezo1.bind("<Return>", self.kiertekel);
                self.mezo1.place(x = 100, y = 100);
                self.mezo2 = Entry(self.frame);
                self.mezo2.bind("<Return>", self.kiertekel);
                self.mezo2.place(x = 100, y = 120);

        def kiertekel(self, event):
                self.canvas.place(x = self.mezo1.get(), y = self.mezo2.get());
                self.mezo1.delete(0, END);
                self.mezo2.delete(0, END);



class Menubar(object):

        def __init__(self, root = None):
                self.root = root;
                ##### Menu <File> #####
                self.fileMenu = Menubutton(self.root, text = "File");
                self.fileMenu.place(x = 10, y = 10);
                # Menu <File> legördülő része
                self.fileMenu1 = Menu(self.fileMenu);
                self.fileMenu1.add_command(label = "New");
                self.fileMenu1.add_command(label = "Törlés");
                self.fileMenu1.add_command(label = "Kilépés");

                # Menu <File> integrálása
                self.fileMenu.configure(menu = self.fileMenu1);
                

if __name__ == "__main__":
        Application();
