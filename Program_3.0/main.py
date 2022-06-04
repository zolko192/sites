#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  main.py
#  verzió: 0.0.1
#
#  Copyright 2020 john31 <john31@john31-Aspire-7735>
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
import tkinter as tk
from program import Program

class Application(tk.Frame):
    """ Tkinter inicializálása """
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.program = Program(self.master)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1366x768+0+0")
    root.title("Beta_0.0.1")
    app = Application(master=root)
    app.mainloop()