#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2022 john35 <john35@john35-VivoBook-15>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from argparse import FileType
import tkinter as tk
from tkinter import filedialog
import os
from pygame import mixer

class Application(tk.Frame):
    """ Applikáció konfigurálása. """
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.program = Program(self.master)

class Program(object):
    """ Főprogram elindítása. """
    def __init__(self, master = None):
        self.master = master
        # Frame menük létrehozása
        self.frame1 = tk.Frame(self.master, width = 683, height = 768, bg = "white")
        self.frame1.place(x = 0, y = 10)
        self.frame2 = tk.Frame(self.master, width = 683, height = 768, bg = "blue")
        self.frame2.place(x = 690, y = 10)
        # Widgetek osztály beillesztése
        self.widgets = Widgets(self.frame1, self.frame2)
        self.menus = Menus(self.master)
        self.music = MusicPlaying(self.master)

class Widgets(object):
    """ Widgetek osztályának létrehozása és konfigurálása. """
    def __init__(self, frame1 = None, frame2 = None):
        self.frame1, self.frame2 = frame1, frame2
        self.locale = os.listdir("/home/john35")
        self.listbox1 = tk.Listbox(self.frame1, bg = "black", fg = "white", height = 100, width = 30)
        self.listbox2 = tk.Listbox(self.frame2, bg = "black", fg ="white", height = 100, width = 30)
        for self.files in self.locale:
            self.listbox1.insert("end", self.files)
            self.listbox2.insert("end", self.files)
        self.listbox1.place(x = 10, y = 10)
        self.listbox2.place(x = 10, y = 10)

class Menus(object):
    """ Menü osztályának létrehozása és konfigurálása. """
    def __init__(self, master = None):
        self.master = master
        # Menu create
        self.menu = tk.Menu(self.master)
        # Menu integrate in the Main class
        self.master.config(menu=self.menu)

        # File menu create
        self.file = tk.Menu(self.menu, tearoff = 0)
        # File almenu create
        self.file.add_command(label = "New")
        self.file.add_command(label = "Open")
        self.file.add_command(label = "Open Folder")
        self.file.add_separator()
        self.file.add_command(label = "Exit", command = lambda: self.master.destroy())
        # File menu integrate
        self.menu.add_cascade(label = "File", menu = self.file)

        # Music menu create
        self.music = tk.Menu(self.menu, tearoff = 0)
        # Music almenu create
        self.music.add_command(label = "Megnyitás", command = lambda: MusicPlaying(self))
        # Music menu integrate
        self.menu.add_cascade(label = "Music", menu = self.music)


class MusicPlaying(object):
    """ Zeneosztály létrehozása és konfigurálása. """
    def __init__(self, master = None):
        self.master = master
        # Mixer starting
        mixer.init()

        # Declare the track and status
        self.track = tk.StringVar()
        self.status = tk.StringVar()

        # Creating track frame for Song label & status label
        self.trackFrame = tk.LabelFrame(self.master, text = "Zenék", font = ("times new roman", 15, "bold"), bg = "grey", fg = "white", bd = 5, relief = tk.GROOVE)
        self.trackFrame.place(x = 150, y = 0, width = 600, height = 300)
        # Inserting song track label and song status label
        self.soundtrack = tk.Label(self.trackFrame, textvariable=self.track, width = 20, font = ("times new roman", 15, "bold"))
        self.soundtrack.grid(row = 0, column = 1, padx = 10, pady = 5)
        self.trackstatus = tk.Label(self.trackFrame, textvariable=self.status)
        self.trackstatus.grid(row = 0, column = 1, padx = 10, pady = 5)

        # Creating button frame
        self.buttonFrame = tk.LabelFrame(self.master, text = "Control Panel", font = ("times new roman", 15, "bold"), bg = "grey", fg = "white", bd = 5, relief = tk.GROOVE)
        self.buttonFrame.place(x = 150, y = 100, width = 600, height = 300)
        # Inserting play, resume, pause, stop button
        self.playbtn = tk.Button(self.buttonFrame, text = "Play", font = ("times new roman", 16, "bold"), bg = "gold", fg = "navyblue", command = self.playsong)
        self.playbtn.grid(row = 0, column = 0, padx = 10, pady = 5)
        self.playbtn = tk.Button(self.buttonFrame, text = "Pause", font = ("times new roman", 16, "bold"), bg = "gold", fg = "navyblue")
        self.playbtn.grid(row = 0, column = 1, padx = 10, pady = 5)
        self.playbtn = tk.Button(self.buttonFrame, text = "Resume", font = ("times new roman", 16, "bold"), bg = "gold", fg = "navyblue")
        self.playbtn.grid(row = 0, column = 2, padx = 10, pady = 5)
        self.playbtn = tk.Button(self.buttonFrame, text = "Stop", font = ("times new roman", 16, "bold"), bg = "gold", fg = "navyblue")
        self.playbtn.grid(row = 0, column = 3, padx = 10, pady = 5)

        # Creating playlist frame
        self.songFrame = tk.LabelFrame(self.master, text = "Lejátszólista", font = ("times new roman", 15, "bold"), bg = "grey", fg = "white", bd = 5, relief = tk.GROOVE)
        self.songFrame.place(x = 750, y = 0, width = 400, height = 200)

        # Creating to playlist
        self.playlist = tk.Listbox(self.songFrame, selectmode = tk.SINGLE, font = ("times new roman", 15, "bold"), bg = "silver", fg = "navyblue")
        self.playlist.pack(fill = tk.BOTH)

        # Changing directory song playlist
        os.chdir("/home/john35/Letöltések")
        # Inserting to playlist
        self.songtracks = os.listdir()
        for track in self.songtracks:
            self.playlist.insert(tk.END, track)

    def playsong(self):
        self.track.set(self.playlist.get(tk.ACTIVE))
        self.status.set("-Playing")
        mixer.music.load(self.playlist.get(tk.ACTIVE))
        mixer.music.play()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1366x768+0+0")
    root.title("Total Commander 0.0.1")
    app = Application(master=root)
    app.mainloop()