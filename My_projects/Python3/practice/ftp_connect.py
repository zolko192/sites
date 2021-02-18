#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from ftplib import FTP

class Ftp_connected(object):
	
	def __init__(self):
		self.ftp = FTP('files.000webhost.com');
		self.ftp.login(user='alinke', passwd='jeanelan22');
		self.ftp.cwd("/public_html");
		self.ftp.retrlines("LIST");
		self.ftp.quit();

Ftp_connected();
