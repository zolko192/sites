#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  root.py
#  
#  Copyright 2021 john31 <john31@john31>
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
from tkinter import*
import main

class Root(object):
    """ Tkinter osztály létrehozása """
    def __init__(self):
        self.root = Tk()
        self.root.title("main_0.0.1")
        self.root.geometry("1366x768+0+0")
        self.application = main.Application(self.root)

        self.root.mainloop()

    def do_exit(self):
        # Exit
        quit()

Root()