#!/usr/bin/python3

from tkinter import Tk
from tkinter import Frame
from tkinter import Menu
from tkinter import Text
from tkinter import END
from tkinter import filedialog
from tkinter import messagebox
		
				
class App(object):

    def __init__(self, master):
        frame = Frame(master);
        frame.pack();
        self.text = Text();
        self.text.pack();

        menu = Menu(master);
        root.config(menu=menu);

        # File menu
        filemenu = Menu(menu, tearoff = 0);
        filemenu.add_command(label = "Új", command = self.file_new);
        filemenu.add_command(label = "Megnyitás", command = self.file_open);
        filemenu.add_command(label = "Mentés", command = self.file_save);
        filemenu.add_separator();
        filemenu.add_command(label = "Kilépés", command = self.do_exit);

        # Help menu
        helpmenu = Menu(menu, tearoff = 0);
        helpmenu.add_command(label = "Névjegy", command = self.do_about);

        menu.add_cascade(label = "File", menu = filemenu);
        menu.add_cascade(label = "Segítség", menu = helpmenu);

    def file_new(self):
        """ Új fájl létrehozása """
        self.text.delete(0.0, END);

    def file_open(self):
        """ Fájl megnyitása """
        # Alapértelmezett könyvtár
        initial_dir = "/home/john31/Letöltések";
        
        # Fájlmaszk megadása
        mask = \
             [("Szöveges és python fájlok", "*.txt" "*.py" "*.pyw"),
              ("HTML fájlok", "*.htm" "*.html"),
              ("Minden fájl", "*")];

        fin = filedialog.askopenfile(initialdir = initial_dir, filetypes = mask, mode = 'r');
        text = fin.read();
        if text != None:
            self.text.delete(0.0, END);
            self.text.insert(END, text);

    def file_save(self):
        """ Fájl mentése """
        # Alapértelmezett kiterjesztés, ha nincs akkor automatikusan megadja
        fout = filedialog.asksaveasfile(mode = 'w', defaultextension = ".txt");
        text2save = str(self.text.get(0.0, END));
        fout.write(text2save);
        fout.close();

    def do_exit(self):
        root.destroy();

    def do_about(self):
        messagebox.showinfo("Névjegy", "Egyszerű szövegszerkesztő\nHorváth Zoltán");


root = Tk();
root.title("Egyszerű szövegszerkesztő");
app = App(root);
root.mainloop();
