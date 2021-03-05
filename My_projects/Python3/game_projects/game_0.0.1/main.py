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
from tkinter import*
from menu import*
from canvas import*
from widget import*

class Application(object):
    """ Főprogram """
    def __init__(self, master):
        # Menu class read
        self.menus = Menubar(master)

        # Canvas class read
        self.vaszon = Vaszon(master)
        
        # Widgets class read
        self.widget = Widgets(master)
        self.widget.labels()
        self.widget.mezos()
        self.widget.buttons()
        self.widget.scales()