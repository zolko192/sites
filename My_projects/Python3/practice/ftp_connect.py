#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from ftplib import FTP

ftp = FTP('files.000webhost.com');
ftp.login(user='alinke', passwd='jeanelan22');
ftp.cwd("/public_html");
ftp.retrlines("LIST");
ftp.quit();
