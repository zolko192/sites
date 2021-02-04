#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

def mappa_files():
	dirname = "__pycache__";
	dirlist = os.scandir(dirname);
	for e in dirlist:
		print(e.name, e.path, e.is_dir(), e.is_file());
